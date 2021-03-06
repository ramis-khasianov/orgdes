# Generated by Django 3.2.9 on 2021-11-15 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empapp', '0002_auto_20211114_1508'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'verbose_name': 'подразделение', 'verbose_name_plural': 'подразделения'},
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ('staff_position__department', 'id'), 'verbose_name': 'сотрудник', 'verbose_name_plural': 'сотрудники'},
        ),
        migrations.AlterModelOptions(
            name='jobtitle',
            options={'verbose_name': 'должность', 'verbose_name_plural': 'должности'},
        ),
        migrations.AlterModelOptions(
            name='organization',
            options={'verbose_name': 'организация', 'verbose_name_plural': 'организации'},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'физическое лицо', 'verbose_name_plural': 'физические лица'},
        ),
        migrations.AlterModelOptions(
            name='staffposition',
            options={'verbose_name': 'штатная позиция', 'verbose_name_plural': 'штатные позиции'},
        ),
        migrations.AddField(
            model_name='department',
            name='is_actual',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='is_actual',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organization',
            name='is_actual',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='is_actual',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staffposition',
            name='is_actual',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
