from django.contrib import admin

from changeapp.models import ChangeGroup, Changes

admin.site.register(ChangeGroup)
admin.site.register(Changes)
