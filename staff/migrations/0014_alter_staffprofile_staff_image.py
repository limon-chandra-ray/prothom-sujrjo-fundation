# Generated by Django 4.2.7 on 2024-01-01 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0013_alter_staffprofile_staff_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffprofile',
            name='staff_image',
            field=models.ImageField(blank=True, null=True, upload_to='staff/2024-01-02/'),
        ),
    ]
