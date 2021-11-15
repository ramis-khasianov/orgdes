from django.db import models

from empapp.models import Employee, Department, JobTitle, StaffPosition


class ChangeGroup(models.Model):
    title = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'группа изменений'
        verbose_name_plural = 'группы изменений'


class NewDepartment(models.Model):
    change_group = models.ForeignKey(ChangeGroup, related_name='new_departments', on_delete=models.PROTECT)
    department = models.ForeignKey(Department, related_name='created_by_changes', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'новое подразделение'
        verbose_name_plural = 'новые подразделения'


class NewJobTitle(models.Model):
    change_group = models.ForeignKey(ChangeGroup, related_name='new_job_titles', on_delete=models.PROTECT)
    job_title = models.ForeignKey(JobTitle, related_name='created_by_changes', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'новая должность'
        verbose_name_plural = 'новые должности'


class NewStaffPosition(models.Model):
    change_group = models.ForeignKey(ChangeGroup, related_name='new_staff_positions', on_delete=models.PROTECT)
    staff_position = models.ForeignKey(StaffPosition, related_name='created_by_changes', on_delete=models.PROTECT)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'новые штатные позиции'
        verbose_name_plural = 'новые штатные позиции'


class EmployeeChange(models.Model):
    title = models.CharField(max_length=255)
    employee = models.ForeignKey(Employee, related_name='changes', on_delete=models.PROTECT)
    change_group = models.ForeignKey(ChangeGroup, related_name='employee_changes', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'изменение условий сотрудника'
        verbose_name_plural = 'изменения условий сотрудников'


class ManagerChange(models.Model):
    employee_change = models.OneToOneField(EmployeeChange, related_name='manager_change', on_delete=models.PROTECT)
    old_manager = models.ForeignKey(StaffPosition, related_name='switch_from_changes',  on_delete=models.PROTECT)
    new_manager = models.ForeignKey(StaffPosition, related_name='switch_to_changes', on_delete=models.PROTECT)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'изменение руководителя'
        verbose_name_plural = 'изменения руководителя'


class JobTitleChange(models.Model):
    employee_change = models.OneToOneField(EmployeeChange, related_name='job_title_change', on_delete=models.PROTECT)
    old_job_title = models.ForeignKey(JobTitle, related_name='switch_from_changes', on_delete=models.PROTECT)
    new_job_title = models.ForeignKey(JobTitle, related_name='switch_to_changes', on_delete=models.PROTECT)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'изменения должности'
        verbose_name_plural = 'изменения должности'


class DepartmentChange(models.Model):
    employee_change = models.OneToOneField(EmployeeChange, related_name='department_change', on_delete=models.PROTECT)
    old_department = models.ForeignKey(Department, related_name='switch_from_changes',  on_delete=models.PROTECT)
    new_department = models.ForeignKey(Department, related_name='switch_to_changes', on_delete=models.PROTECT)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'изменение подразделения'
        verbose_name_plural = 'изменения подразделения'


class SalaryChange(models.Model):
    employee_change = models.OneToOneField(EmployeeChange, related_name='salary_change', on_delete=models.PROTECT)
    old_salary = models.DecimalField(max_digits=12, decimal_places=2)
    new_salary = models.DecimalField(max_digits=12, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'изменение оклада'
        verbose_name_plural = 'изменения оклада'


class BonusChange(models.Model):
    FLAT = 'flat'
    PERCENT = 'percent'
    COMPLEX = 'complex'

    BONUS_TYPE_CHOICES = (
        (FLAT, 'Фиксированная сумма'),
        (PERCENT, 'Процент от оклада'),
        (COMPLEX, 'Отдельная схема премирования')
    )

    ANNUAL = 'annual'
    SEMIANNUAL = 'semiannual'
    QUARTERLY = 'quarterly'
    MONTHLY = 'monthly'
    OTHER = 'other'

    BONUS_PERIOD_CHOICES = (
        (ANNUAL, 'Год'),
        (SEMIANNUAL, 'Полугодие'),
        (QUARTERLY, 'Квартал'),
        (MONTHLY, 'Месяц'),
        (OTHER, 'Другое')
    )

    employee_change = models.OneToOneField(EmployeeChange, related_name='bonus_change', on_delete=models.PROTECT)
    old_bonus_schema = models.CharField(choices=BONUS_TYPE_CHOICES, max_length=10, default=PERCENT)
    old_bonus_period = models.CharField(choices=BONUS_PERIOD_CHOICES, max_length=10, default=ANNUAL)
    old_bonus_value = models.DecimalField(max_digits=12, decimal_places=2)
    new_bonus_schema = models.CharField(choices=BONUS_TYPE_CHOICES, max_length=10, default=PERCENT)
    new_bonus_period = models.CharField(choices=BONUS_PERIOD_CHOICES, max_length=10, default=ANNUAL)
    new_bonus_value = models.DecimalField(max_digits=12, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'изменение условий премии'
        verbose_name_plural = 'изменения условий премии'


class OtherChange(models.Model):
    employee_change = models.ForeignKey(EmployeeChange, related_name='other_changes', on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    old_value = models.CharField(max_length=255)
    new_value = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'изменения других условий'
        verbose_name_plural = 'изменения других условий'
