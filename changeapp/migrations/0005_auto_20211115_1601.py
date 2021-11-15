# Generated by Django 3.2.9 on 2021-11-15 16:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('empapp', '0004_auto_20211115_1503'),
        ('changeapp', '0004_auto_20211115_1551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='changes',
            name='new_manager',
        ),
        migrations.RemoveField(
            model_name='changes',
            name='old_manager',
        ),
        migrations.AddField(
            model_name='changes',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='changes', to='empapp.employee'),
        ),
        migrations.AddField(
            model_name='changes',
            name='new_value',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='changes',
            name='old_value',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='changegroup',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='changegroup',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]