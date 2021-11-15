from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from empapp.views import OrganizationViewSet, DepartmentViewSet, JobTitleViewSet, OrgChartViewSet
from userapp.views import UsersViewSet

from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register('users', UsersViewSet)
router.register('organizations', OrganizationViewSet)
router.register('departments', DepartmentViewSet)
router.register('job_titles', JobTitleViewSet)
router.register('orgchart', OrgChartViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token-auth/', obtain_auth_token),
    path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
