from rest_framework import serializers

from empapp.models import Employee, Organization, Department, JobTitle


class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = '__all__'


class JobTitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobTitle
        fields = '__all__'


class OrgChartSerializer(serializers.ModelSerializer):
    """Основной сериалайзер, который принимается фронтом"""
    pid = serializers.IntegerField(source='staff_position.manager.get_current_employee_id', read_only=True)
    name = serializers.CharField(source='get_name')
    title = serializers.CharField(source='staff_position.title')
    img = serializers.URLField(source='get_photo_url')

    full_name = serializers.CharField(source='get_full_name')
    department = serializers.CharField(source='staff_position.department.title', read_only=True)
    job_title = serializers.CharField(source='staff_position.job_title.title', read_only=True)
    employment_rate = serializers.FloatField()

    manager_id = serializers.IntegerField(source='staff_position.manager.get_current_employee_id', read_only=True)
    manager_name = serializers.CharField(source='staff_position.manager.get_current_employee_name', read_only=True)
    vacancy_approved_date = serializers.DateField(source='get_vacancy_approved_date')

    salary = serializers.FloatField(source='salary_terms.salary')
    bonus = serializers.FloatField(source='salary_terms.get_bonus_sum')
    bonus_description = serializers.CharField(source='salary_terms.get_bonus_description')
    total_payroll = serializers.FloatField(source='salary_terms.get_total_monthly_payroll')

    all_subordinates_fte = serializers.FloatField(source='get_all_subordinates_fte')
    all_subordinates_payroll = serializers.FloatField(source='get_all_subordinates_payroll')
    all_subordinates_payroll_text = serializers.CharField(source='get_all_subordinates_payroll_text')

    class Meta:
        model = Employee
        fields = ['id', 'pid', 'name', 'title', 'img',
                  'full_name', 'department', 'job_title', 'employment_rate',
                  'manager_id', 'manager_name', 'is_long_absence', 'hire_date', 'exit_date',
                  'is_vacancy', 'vacancy_approved_date',
                  'salary', 'bonus', 'bonus_description', 'total_payroll',
                  'all_subordinates_fte', 'all_subordinates_payroll', 'all_subordinates_payroll_text']
