from rest_framework.viewsets import ModelViewSet
from empapp.models import StaffPosition
from empapp.serializers import OrgChartSerializer


class OrgChartViewSet(ModelViewSet):
    serializer_class = OrgChartSerializer
    queryset = StaffPosition.objects.all()
