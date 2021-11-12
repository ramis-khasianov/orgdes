from rest_framework.viewsets import ModelViewSet
from empapp.models import Employee
from empapp.serializers import EmployeeSerializer


class EmployeesViewSet(ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
