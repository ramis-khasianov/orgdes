from django.contrib import admin

from changeapp.models import (ChangeGroup, NewDepartment, NewJobTitle, NewStaffPosition,
                              EmployeeChange, DepartmentChange, JobTitleChange, ManagerChange,
                              SalaryChange, BonusChange, OtherChange)

admin.site.register(ChangeGroup)
admin.site.register(NewDepartment)
admin.site.register(NewJobTitle)
admin.site.register(NewStaffPosition)
admin.site.register(EmployeeChange)
admin.site.register(DepartmentChange)
admin.site.register(JobTitleChange)
admin.site.register(ManagerChange)
admin.site.register(SalaryChange)
admin.site.register(BonusChange)
admin.site.register(OtherChange)
