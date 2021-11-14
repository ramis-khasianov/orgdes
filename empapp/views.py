from rest_framework.viewsets import ModelViewSet
from empapp.models import Employee
from empapp.serializers import OrgChartSerializer


class OrgChartViewSet(ModelViewSet):
    serializer_class = OrgChartSerializer
    queryset = Employee.objects.all()
