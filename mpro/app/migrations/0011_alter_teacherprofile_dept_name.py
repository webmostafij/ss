# Generated by Django 3.2.4 on 2021-06-22 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_teacherprofile_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherprofile',
            name='dept_name',
            field=models.CharField(default='CSE', max_length=10),
        ),
    ]