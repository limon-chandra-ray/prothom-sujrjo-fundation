# Generated by Django 4.2.7 on 2023-12-27 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('child', '0013_alter_childprofile_child_image_childprogress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='childprogress',
            name='progress_year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
