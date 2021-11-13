from django.db import models


class Organization(models.Model):
    """Организация, Юридическое лицо"""
    guid = models.CharField(max_length=50, primary_key=True)
    title = models.CharField(max_length=150)
    short_title = models.CharField(max_length=30)
    group_name = models.CharField(max_length=30)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'


class Department(models.Model):
    """Подразделения с иерархией"""
    guid = models.CharField(max_length=50, primary_key=True)
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
    guid = models.CharField(max_length=50, primary_key=True)
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
        return f'{self.department} // {self.job_title}'


class Person(models.Model):
    """Физические лица"""
    MALE = 'M'
    FEMALE = 'W'

    GENDER_CHOICES = (
        (MALE, 'М'),
        (FEMALE, 'Ж')
    )

    guid = models.CharField(max_length=50, primary_key=True)
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
    """Сотрудники"""
    guid = models.CharField(max_length=50, primary_key=True)
    staff_position = models.ForeignKey(StaffPosition, on_delete=models.PROTECT)
    person = models.ForeignKey(Person, on_delete=models.PROTECT)
    hire_date = models.DateField()
    exit_date = models.DateField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.person.last_name} {self.person.first_name}'
