from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from empapp.views import OrgChartViewSet
from userapp.views import UsersViewSet

from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register('users', UsersViewSet)
router.register('orgchart', OrgChartViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
