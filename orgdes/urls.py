from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from empapp.views import OrgChartViewSet
from userapp.views import UsersViewSet

router = DefaultRouter()
router.register('users', UsersViewSet)
router.register('orgchart', OrgChartViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
