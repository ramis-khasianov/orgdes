# Generated by Django 3.2.9 on 2021-11-14 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empapp', '0002_auto_20211114_1508'),
        ('termsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bonusterms',
            options={'verbose_name_plural': 'bonus terms'},
        ),
        migrations.AlterModelOptions(
            name='salaryterms',
            options={'verbose_name_plural': 'salary terms'},
        ),
        migrations.AlterField(
            model_name='bonusterms',
            name='bonus_period',
            field=models.CharField(choices=[('annual', 'Год'), ('semiannual', 'Полугодие'), ('quarterly', 'Квартал'), ('monthly', 'Месяц'), ('other', 'Другое')], default='annual', max_length=10),
        ),
        migrations.AlterField(
            model_name='bonusterms',
            name='bonus_schema',
            field=models.CharField(choices=[('flat', 'Фиксированная сумма'), ('percent', 'Процент от оклада'), ('complex', 'Отдельная схема премирования')], default='percent', max_length=10),
        ),
        migrations.AlterField(
            model_name='salaryterms',
            name='employee',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='salary_terms', to='empapp.employee'),
        ),
    ]