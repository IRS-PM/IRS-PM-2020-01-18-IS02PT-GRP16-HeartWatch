# Generated by Django 3.0.3 on 2020-03-05 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0006_auto_20200305_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialservice',
            name='household_income',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='socialservice',
            name='program',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='socialservice',
            name='support_type',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
