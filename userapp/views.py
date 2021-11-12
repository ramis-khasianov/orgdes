from rest_framework import mixins, viewsets

from userapp.models import User
from userapp.serializers import UserSerializer


class UsersViewSet(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   viewsets.GenericViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
