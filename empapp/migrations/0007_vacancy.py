# Generated by Django 3.2.9 on 2021-11-14 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empapp', '0006_auto_20211114_0821'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('guid', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('employment_rate', models.DecimalField(decimal_places=2, default=1.0, max_digits=3)),
                ('approved_date', models.DateTimeField(null=True)),
                ('is_in_search', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('staff_position', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='vacancies', to='empapp.staffposition')),
            ],
        ),
    ]
