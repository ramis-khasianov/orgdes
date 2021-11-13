from django.db import models


class Organization(models.Model):
    """Организация, Юридическое лицо"""
    guid = models.CharField(max_length=50, primary_key=True)
    title = models.CharField(max_length=150)
    short_title = models.CharField(max_length=30)
    group_name = models.CharField(max_length=30)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)


class Department(models.Model):
    """Подразделения с иерархией"""
    guid = models.CharField(max_length=50, primary_key=True)
    title = models.CharField(max_length=150)
    parent = models.ForeignKey('self', related_name='subdepartments', on_delete=models.PROTECT, null=True)
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)


class StaffPosition(models.Model):
    """Штатные позиции"""
    guid = models.CharField(max_length=50, primary_key=True)
    title = models.CharField(max_length=150)
    manager = models.ForeignKey('self', related_name='subordinates', on_delete=models.PROTECT, null=True)
    fte_count = models.DecimalField(max_digits=5, decimal_places=2)
    approved_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)


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
    updated_date = models.DateField(auto_now=True)


class Employee(models.Model):
    """Сотрудники"""
    guid = models.CharField(max_length=50, primary_key=True)
    staff_position = models.ForeignKey(StaffPosition, on_delete=models.PROTECT)
    person = models.ForeignKey(Person, on_delete=models.PROTECT)
    hire_date = models.DateField()
    exit_date = models.DateField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.person.first_name} {self.person.last_name}'
