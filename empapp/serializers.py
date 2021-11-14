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
    """Поддерживающий сериалайзер по сотрудникам для метода ниже"""
    employment_rate = serializers.FloatField()

    class Meta:
        model = Vacancy
        fields = '__all__'


class OrgChartSerializer(serializers.ModelSerializer):
    """Основной сериалайзер, который принимается фронтом"""
    id = serializers.CharField(source='guid')
    pid = serializers.CharField(source='manager.guid', read_only=True)
    department = serializers.CharField(source='department.title', read_only=True)
    job_title = serializers.CharField(source='job_title.title', read_only=True)
    fte_count = serializers.FloatField()
    manager_name = serializers.CharField(source='get_current_manager_name')
    employees = EmployeeSerializer(many=True)
    vacancies = VacancySerializer(many=True)

    class Meta:
        model = StaffPosition
        fields = ['id', 'pid', 'title', 'department', 'job_title', 'fte_count', 'manager_name', 'employees', 'vacancies']
