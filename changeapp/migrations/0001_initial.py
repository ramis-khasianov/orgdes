# Generated by Django 3.2.9 on 2021-11-15 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empapp', '0002_auto_20211114_1508'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChangeGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeChange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('change_group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='employee_changes', to='changeapp.changegroup')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='empapp.employee')),
            ],
        ),
        migrations.CreateModel(
            name='SalaryChange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('old_salary', models.DecimalField(decimal_places=2, max_digits=12)),
                ('new_salary', models.DecimalField(decimal_places=2, max_digits=12)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('employee_change', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='salary_change', to='changeapp.employeechange')),
            ],
        ),
        migrations.CreateModel(
            name='OtherChange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('old_value', models.CharField(max_length=255)),
                ('new_value', models.CharField(max_length=255)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('employee_change', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='other_changes', to='changeapp.employeechange')),
            ],
        ),
        migrations.CreateModel(
            name='NewStaffPosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('change_group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='new_staff_positions', to='changeapp.changegroup')),
                ('staff_position', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='empapp.staffposition')),
            ],
        ),
        migrations.CreateModel(
            name='NewJobTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('change_group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='new_job_titles', to='changeapp.changegroup')),
                ('job_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empapp.jobtitle')),
            ],
        ),
        migrations.CreateModel(
            name='NewDepartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('change_group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='new_departments', to='changeapp.changegroup')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empapp.department')),
            ],
        ),
        migrations.CreateModel(
            name='ManagerChange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('employee_change', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='manager_change', to='changeapp.employeechange')),
                ('new_manager', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='switch_to_changes', to='empapp.staffposition')),
                ('old_manager', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='switch_from_changes', to='empapp.staffposition')),
            ],
        ),
        migrations.CreateModel(
            name='JobTitleChange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('employee_change', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='job_title_change', to='changeapp.employeechange')),
                ('new_job_title', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='switch_to_changes', to='empapp.jobtitle')),
                ('old_job_title', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='switch_from_changes', to='empapp.jobtitle')),
            ],
        ),
        migrations.CreateModel(
            name='DepartmentChange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('employee_change', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='department_change', to='changeapp.employeechange')),
                ('new_department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='switch_to_changes', to='empapp.department')),
                ('old_department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='switch_from_changes', to='empapp.department')),
            ],
        ),
        migrations.CreateModel(
            name='BonusChange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('old_bonus_schema', models.CharField(choices=[('flat', 'Фиксированная сумма'), ('percent', 'Процент от оклада'), ('complex', 'Отдельная схема премирования')], default='percent', max_length=10)),
                ('old_bonus_period', models.CharField(choices=[('annual', 'Год'), ('semiannual', 'Полугодие'), ('quarterly', 'Квартал'), ('monthly', 'Месяц'), ('other', 'Другое')], default='annual', max_length=10)),
                ('old_bonus_value', models.DecimalField(decimal_places=2, max_digits=12)),
                ('new_bonus_schema', models.CharField(choices=[('flat', 'Фиксированная сумма'), ('percent', 'Процент от оклада'), ('complex', 'Отдельная схема премирования')], default='percent', max_length=10)),
                ('new_bonus_period', models.CharField(choices=[('annual', 'Год'), ('semiannual', 'Полугодие'), ('quarterly', 'Квартал'), ('monthly', 'Месяц'), ('other', 'Другое')], default='annual', max_length=10)),
                ('new_bonus_value', models.DecimalField(decimal_places=2, max_digits=12)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('employee_change', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='bonus_change', to='changeapp.employeechange')),
            ],
        ),
    ]
