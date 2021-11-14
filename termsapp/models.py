from django.db import models
from empapp.models import Employee


class SalaryTerms(models.Model):
    """Оклад сотрудника"""
    employee = models.OneToOneField(Employee, related_name='salary_terms', on_delete=models.PROTECT)
    salary = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        verbose_name_plural = "salary terms"

    def __str__(self):
        return f'Оклад {self.employee}'

    def get_annual_payroll(self):
        total_payroll = 0
        if self.bonus_terms.count() > 0:
            for bonus_term in self.bonus_terms.all():
                total_payroll += bonus_term.get_monthly_bonus_sum()
        total_payroll = total_payroll * 1.24  # Отчисления
        return total_payroll


class BonusTerms(models.Model):
    """Премия сотрудника"""
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
    salary_terms = models.ForeignKey(SalaryTerms, related_name='bonus_terms', on_delete=models.PROTECT)
    bonus_schema = models.CharField(choices=BONUS_TYPE_CHOICES, max_length=10, default=PERCENT)
    bonus_period = models.CharField(choices=BONUS_PERIOD_CHOICES, max_length=10, default=ANNUAL)
    bonus_value = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f'{self.salary_terms.employee}: {self.bonus_value}, {self.bonus_period}, {self.bonus_schema}'

    class Meta:
        verbose_name_plural = "bonus terms"

    def get_monthly_bonus_sum(self):
        rates = {
            self.ANNUAL: 12,
            self.SEMIANNUAL: 6,
            self.QUARTERLY: 3,
            self.MONTHLY: 1,
            self.OTHER: 1
        }

        if self.bonus_schema == self.FLAT:
            bonus_sum = self.bonus_value / rates[self.bonus_period]
        elif self.bonus_schema == self.PERCENT:
            bonus_sum = self.salary_terms.salary * self.bonus_value
        else:
            bonus_sum = self.bonus_value
        return bonus_sum
