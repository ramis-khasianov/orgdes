from django.db import models
from django.db.models import Sum
import locale


class Organization(models.Model):
    """Организация, Юридическое лицо"""
    guid = models.CharField(max_length=50, null=True, blank=True)
    title = models.CharField(max_length=150)
    short_title = models.CharField(max_length=30)
    group_name = models.CharField(max_length=30)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'


class Department(models.Model):
    """Подразделения с иерархией"""
    guid = models.CharField(max_length=50, null=True, blank=True)
    title = models.CharField(max_length=150)
    parent_department = models.ForeignKey('self', related_name='subdepartments', on_delete=models.PROTECT,
                                          null=True, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'


class JobTitle(models.Model):
    """Должности"""
    guid = models.CharField(max_length=50, primary_key=True)
    title = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.title}'


class StaffPosition(models.Model):
    """Штатные позиции"""
    guid = models.CharField(max_length=50, null=True, blank=True)
    title = models.CharField(max_length=150)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    job_title = models.ForeignKey(JobTitle, on_delete=models.PROTECT)
    manager = models.ForeignKey('self', related_name='subordinates', on_delete=models.PROTECT,
                                null=True, blank=True)
    fte_count = models.DecimalField(max_digits=5, decimal_places=2)
    approved_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.get_current_fte()}/{self.fte_count}, {self.department} // {self.job_title}: {self.get_current_employee_name()}'

    def get_current_employee_id(self):
        employees = self.employees.all()
        records_count = employees.count()
        if records_count == 0:
            id = 0
        elif records_count == 1:
            id = employees.first().id
        else:
            id = f'{employees.first().id}, {records_count - 1}+'
        return id

    def get_current_employee_name(self):
        employees = self.employees.all()
        records_count = employees.count()
        if records_count == 0:
            name = ''
        elif records_count == 1:
            name = employees.first().get_name()
        else:
            name = f'{employees.first().get_name()} и еще {records_count - 1}'
        return name

    def get_current_fte(self):
        if self.employees.count() > 0:
            return self.employees.aggregate(Sum('employment_rate'))['employment_rate__sum']
        return 0

    def get_current_total_fte(self):
        ids = self.get_full_tree_ids()
        qs = StaffPosition.objects.filter(id__in=ids)
        total_fte = 0
        for q in qs:
            total_fte += q.get_current_fte()
        return total_fte

    def get_full_tree_ids(self):
        """Метод проходит по всему дереву подчинения и соберет сет с прямыми и непрямыми подчиненными"""
        # Все айдишники набьем в сет, начиная с самого себя
        all_tree_ids = set()

        # Берем список id прямых подчиненных. Теперь это потенциальные менеджеры, по которым проверямем подчиненных
        potential_managers_list = list(StaffPosition.objects.filter(manager_id=self.id).values_list('id', flat=True))

        # Если он не пустой то начинаем ходить по нему, pop'ая по одному элементу и пока список не закончится
        if len(potential_managers_list) > 0:
            while len(potential_managers_list) > 0:

                # Берем первый элемент из списка потенциальных менеджеров
                next_potential_manager_id = potential_managers_list.pop(0)

                # Добавляем его в итоговый лист, т.к. он в любом случае в общем списке подчиненных
                all_tree_ids.add(next_potential_manager_id)

                # Получаем список их прямых подчиненных
                potential_managers_subordinates = StaffPosition.objects.filter(manager_id=next_potential_manager_id)

                # Если он не пустой, то работаем с ним дальше
                if potential_managers_subordinates:

                    # Список новых прямых подчиненных добавляем в общий список
                    new_indirect_reports = potential_managers_subordinates.values_list('id', flat=True)
                    all_tree_ids.update(new_indirect_reports)

                    # Дальше проверяем, может в списке есть новые потенциальные менеджеры. Проходимся по списку
                    for sub_subordinate in potential_managers_subordinates:

                        # Для каждого проверяем, есть ли подчиненные
                        sub_sub_subordinates = StaffPosition.objects.filter(manager_id=sub_subordinate.id)

                        # Если все же есть подчиненные
                        if sub_sub_subordinates.count() > 0:

                            # Формируем из этого добра список
                            new_potential_managers = list(sub_sub_subordinates.values_list('id', flat=True))

                            # Добавляем их в общий список
                            potential_managers_list.append(new_potential_managers)

        # Возвращаем сет. Каждый сет будет для объекта будет содержать айдишник самого себя и всех подчиненных
        return all_tree_ids

    def get_current_total_fte2(self):
        direct_subordinates = self.subordinates.all()
        total_fte = 0
        for sub in direct_subordinates:
            total_fte = total_fte + sub.employees.aggregate(Sum('employment_rate'))['employment_rate__sum']
        return total_fte



class Person(models.Model):
    """Физические лица"""
    MALE = 'M'
    FEMALE = 'W'

    GENDER_CHOICES = (
        (MALE, 'М'),
        (FEMALE, 'Ж')
    )

    guid = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='person_photos', blank=True)
    birth_date = models.DateField(null=True)
    gender = models.CharField(choices=GENDER_CHOICES, blank=True, max_length=1)
    social_hash = models.CharField(max_length=20)
    login = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=120, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'


class Employee(models.Model):
    """Сотрудники и вакансии"""
    guid = models.CharField(max_length=50, null=True, blank=True)
    staff_position = models.ForeignKey(StaffPosition, related_name='employees', on_delete=models.PROTECT)
    employment_rate = models.DecimalField(max_digits=3, decimal_places=2, default=1.00)
    is_vacancy = models.IntegerField(default=0)
    person = models.ForeignKey(Person, on_delete=models.PROTECT, null=True, blank=True)
    hire_date = models.DateField(null=True, blank=True)
    exit_date = models.DateField(null=True, blank=True)
    is_long_absence = models.IntegerField(default=0)
    long_absence_type = models.CharField(max_length=50, null=True, blank=True)
    vacancy_approved_date = models.DateTimeField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.person:
            return f'{self.person.last_name} {self.person.first_name}'
        return f'Вакансия: {self.staff_position.title}'

    class Meta:
        ordering = ('staff_position__department', 'id')

    def get_name(self):
        if self.person:
            return f'{self.person.last_name} {self.person.first_name}'
        return f'Вакансия'

    def get_full_name(self):
        if self.person:
            return f'{self.person.last_name} {self.person.first_name} {self.person.middle_name}'
        return f'Вакансия: {self.staff_position.title}'

    def get_photo_url(self):
        base_url = 'http://127.0.0.1:8000/media/'
        if self.person:
            return f'{base_url}{self.person.photo}'
        return f'{base_url}profile_placeholder.jpg'

    def get_vacancy_approved_date(self):
        if self.vacancy_approved_date:
            return self.vacancy_approved_date.date()

    def get_all_subordinates_fte(self):
        total_fte = self.employment_rate
        subordinates_staff_ids = self.staff_position.get_full_tree_ids()
        qs = Employee.objects.filter(staff_position__id__in=subordinates_staff_ids)
        subordinates_fte = qs.aggregate(Sum('employment_rate'))['employment_rate__sum']
        if subordinates_fte:
            total_fte += subordinates_fte
        return total_fte

    def get_all_subordinates_payroll(self):
        total_payroll = self.salary_terms.get_total_monthly_payroll()
        subordinates_staff_ids = self.staff_position.get_full_tree_ids()
        qs = Employee.objects.filter(staff_position__id__in=subordinates_staff_ids)
        for q in qs:
            total_payroll += q.salary_terms.get_total_monthly_payroll()
        return total_payroll

    def get_all_subordinates_payroll_text(self):
        total_payroll = int(self.get_all_subordinates_payroll())
        return f'{total_payroll:,}'.replace(',', '\u00A0')




