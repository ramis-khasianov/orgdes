from django.contrib import admin
from empapp.models import Organization, Department, JobTitle, StaffPosition, Person, Employee


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('guid', 'title', 'group_name', 'created_date', 'updated_date')


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('guid', 'title', 'parent_department', 'organization', 'created_date', 'updated_date')


class StaffPositionAdmin(admin.ModelAdmin):
    list_display = ('guid', 'title', 'department', 'job_title', 'approved_date', 'fte_count', 'created_date', 'updated_date')


class PersonAdmin(admin.ModelAdmin):
    list_display = ('guid', 'login', 'created_date', 'updated_date')


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('guid', 'person', 'staff_position', 'employment_rate', 'hire_date', 'exit_date', 'created_date', 'updated_date')


class VacancyAdmin(admin.ModelAdmin):
    list_display = ('guid', 'staff_position', 'employment_rate', 'approved_date', 'is_in_search')


admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(JobTitle)
admin.site.register(StaffPosition, StaffPositionAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Employee, EmployeeAdmin)
