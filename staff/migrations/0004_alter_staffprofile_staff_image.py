# Generated by Django 4.2.7 on 2023-11-09 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_delete_officestaff_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffprofile',
            name='staff_image',
            field=models.ImageField(blank=True, null=True, upload_to='staff/2023-11-10/'),
        ),
    ]
