from django.db import models

from empapp.models import Employee, Department, JobTitle, StaffPosition
from userapp.models import User


class ChangeGroup(models.Model):
    DRAFT = 'draft'
    FORFEITED = 'forfeited'
    PROCESSING = 'processing'
    APPROVED = 'approved'
    EXECUTED = 'executed'

    STATUSES = (
        (DRAFT, 'Черновик'),
        (FORFEITED, 'Отменено'),
        (PROCESSING, 'Согласовывается'),
        (APPROVED, 'Согласовано'),
        (EXECUTED, 'Выполнено')
    )

    title = models.CharField(max_length=255, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    status = models.CharField(choices=STATUSES, max_length=10, default=DRAFT)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'группа изменений'
        verbose_name_plural = 'группы изменений'


class Changes(models.Model):
    MANAGER_CHANGE = 'manager_change'
    SALARY_CHANGE = 'salary_change'

    BONUS_TYPE_CHOICES = (
        (MANAGER_CHANGE, 'Измегнение руководителя'),
        (SALARY_CHANGE, 'Изменение оклада')
    )

    title = models.CharField(max_length=255)
    change_group = models.ForeignKey(ChangeGroup, related_name='new_departments', on_delete=models.PROTECT)
    employee = models.ForeignKey(Employee, related_name='changes', on_delete=models.PROTECT, null=True, blank=True)
    type = models.CharField(max_length=255)
    old_value = models.IntegerField(null=True, blank=True)
    new_value = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'изменение'
        verbose_name_plural = 'изменения'
        ordering = ['-updated_date']



