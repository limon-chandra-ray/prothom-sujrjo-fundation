# Generated by Django 4.2.7 on 2023-11-14 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsorprofile',
            name='sponsor_full_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
