from rest_framework.viewsets import ModelViewSet
from empapp.models import Organization, Department, JobTitle, Employee
from empapp.serializers import OrganizationSerializer, DepartmentSerializer, JobTitleSerializer, OrgChartSerializer


class OrganizationViewSet(ModelViewSet):
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()


class DepartmentViewSet(ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class JobTitleViewSet(ModelViewSet):
    serializer_class = JobTitleSerializer
    queryset = JobTitle.objects.all()


class OrgChartViewSet(ModelViewSet):
    serializer_class = OrgChartSerializer
    queryset = Employee.objects.all()
