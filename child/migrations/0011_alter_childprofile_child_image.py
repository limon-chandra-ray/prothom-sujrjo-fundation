# Generated by Django 4.2.7 on 2023-12-08 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('child', '0010_alter_childprofile_child_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='childprofile',
            name='child_image',
            field=models.ImageField(blank=True, null=True, upload_to='children/2023-12-08/'),
        ),
    ]
