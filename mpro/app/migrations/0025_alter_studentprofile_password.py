# Generated by Django 3.2.4 on 2021-07-05 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_alter_attendencemodel_attendence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='password',
            field=models.CharField(default='1234', max_length=50),
        ),
    ]