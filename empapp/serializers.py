from rest_framework import serializers

from empapp.models import StaffPosition


class OrgChartSerializer(serializers.ModelSerializer):

    class Meta:
        model = StaffPosition
        fields = '__all__'
