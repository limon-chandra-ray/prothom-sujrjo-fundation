# Generated by Django 4.2.6 on 2023-11-04 07:08

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Staff',
        ),
        migrations.CreateModel(
            name='OfficeStaff',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('user.customuser',),
            managers=[
                ('office_staff', django.db.models.manager.Manager()),
            ],
        ),
    ]
