# Generated by Django 3.2.9 on 2021-11-13 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empapp', '0004_auto_20211113_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffposition',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='empapp.department'),
        ),
        migrations.AlterField(
            model_name='staffposition',
            name='job_title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='empapp.jobtitle'),
        ),
    ]