from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from empapp.views import EmployeesViewSet
from userapp.views import UsersViewSet

router = DefaultRouter()
router.register('users', UsersViewSet)
router.register('employees', EmployeesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
