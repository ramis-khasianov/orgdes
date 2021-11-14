from rest_framework import serializers

from empapp.models import StaffPosition, Employee


class EmployeeSerializer(serializers.ModelSerializer):
    """Поддерживающий сериалайзер для метода ниже"""
    person_name = serializers.CharField(source='person')
    employment_rate = serializers.FloatField()

    class Meta:
        model = Employee
        fields = ['guid', 'person_name', 'employment_rate', 'is_long_absence', 'hire_date', 'exit_date']


class OrgChartSerializer(serializers.ModelSerializer):
    """Основной сериалайзер, который принимается фронтом"""
    id = serializers.CharField(source='guid')
    job_title = serializers.CharField(source='job_title.title', read_only=True)
    department = serializers.CharField(source='department.title', read_only=True)
    employees = EmployeeSerializer(many=True)
    pid = serializers.CharField(source='manager.guid', read_only=True)
    manager_name = serializers.CharField(source='get_current_manager_name')

    class Meta:
        model = StaffPosition
        fields = ['id', 'pid', 'title', 'department', 'job_title', 'manager_name', 'employees']
