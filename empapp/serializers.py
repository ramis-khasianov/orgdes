from rest_framework import serializers

from empapp.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    pid = serializers.IntegerField(source='manager.pk', read_only=True)
    title = serializers.CharField(source='job_title')

    class Meta:
        model = Employee
        fields = ['id', 'pid', 'name', 'title']
