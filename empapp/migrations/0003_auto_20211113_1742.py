# Generated by Django 3.2.9 on 2021-11-13 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empapp', '0002_auto_20211113_1738'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='parent',
        ),
        migrations.AddField(
            model_name='department',
            name='parent_department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='subdepartments', to='empapp.department'),
        ),
    ]