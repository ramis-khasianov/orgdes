# Generated by Django 3.2.9 on 2021-11-15 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('termsapp', '0002_auto_20211114_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bonusterms',
            name='salary_terms',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bonus_terms', to='termsapp.salaryterms'),
        ),
    ]
