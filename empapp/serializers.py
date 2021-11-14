from rest_framework import serializers

from empapp.models import StaffPosition, Employee, Vacancy


class EmployeeSerializer(serializers.ModelSerializer):
    """Поддерживающий сериалайзер по сотрудникам для метода ниже"""
    person_name = serializers.CharField(source='person')
    employment_rate = serializers.FloatField()
    img = serializers.URLField(source='person.photo', read_only=True)

    class Meta:
        model = Employee
        fields = ['guid', 'img', 'person_name', 'employment_rate', 'is_long_absence',
                  'hire_date', 'exit_date']


class VacancySerializer(serializers.ModelSerializer):
    """Поддерживающий сериалайзер по вакансиям для метода ниже"""
    title = serializers.CharField(source='get_vacancy_name')
    employment_rate = serializers.FloatField()

    class Meta:
        model = Vacancy
        fields = ['guid', 'title', 'employment_rate', 'is_in_search', 'approved_date']


class OrgChartSerializer(serializers.ModelSerializer):
    """Основной сериалайзер, который принимается фронтом"""
    department = serializers.CharField(source='department.title', read_only=True)
    job_title = serializers.CharField(source='job_title.title', read_only=True)
    fte_count = serializers.FloatField()
    manager_guid = serializers.CharField(source='manager.guid', read_only=True)
    manager_employee_guid = serializers.CharField(source='get_current_manager_employee_guid')
    manager_name = serializers.CharField(source='get_current_manager_name')
    employees = EmployeeSerializer(many=True)
    vacancies = VacancySerializer(many=True)

    class Meta:
        model = StaffPosition
        fields = ['guid', 'title', 'department', 'job_title', 'fte_count',
                  'manager_guid', 'manager_employee_guid', 'manager_name', 'employees', 'vacancies']
