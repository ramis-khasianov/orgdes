from rest_framework import serializers

from empapp.models import Employee


class OrgChartSerializer(serializers.ModelSerializer):
    """Основной сериалайзер, который принимается фронтом"""
    pid = serializers.IntegerField(source='staff_position.manager.get_current_employee_id', read_only=True)
    name = serializers.CharField(source='get_name')
    title = serializers.CharField(source='staff_position.title')
    img = serializers.URLField(source='person.photo', read_only=True)
    full_name = serializers.CharField(source='get_full_name')

    department = serializers.CharField(source='staff_position.department.title', read_only=True)
    job_title = serializers.CharField(source='staff_position.job_title.title', read_only=True)
    manager_id = serializers.IntegerField(source='staff_position.manager.get_current_employee_id', read_only=True)
    manager_name = serializers.CharField(source='staff_position.manager.get_current_employee_name', read_only=True)


    class Meta:
        model = Employee
        fields = ['id', 'pid', 'name', 'title', 'img',
                  'full_name', 'department', 'job_title', 'employment_rate',
                  'manager_id', 'manager_name', 'is_long_absence', 'hire_date', 'exit_date',
                  'is_vacancy', 'vacancy_approved_date']
