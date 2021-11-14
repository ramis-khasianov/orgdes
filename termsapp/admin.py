from django.contrib import admin
from termsapp.models import SalaryTerms, BonusTerms


class SalaryTermsAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee', 'salary')


class BonusTermsAdmin(admin.ModelAdmin):
    list_display = ('id', 'salary_terms', 'bonus_value', 'bonus_schema', 'bonus_period')


admin.site.register(SalaryTerms, SalaryTermsAdmin)
admin.site.register(BonusTerms, BonusTermsAdmin)
