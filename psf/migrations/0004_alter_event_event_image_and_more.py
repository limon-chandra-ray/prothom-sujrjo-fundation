# Generated by Django 4.2.6 on 2023-11-03 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psf', '0003_rename_child_discription_shelterchild_child_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_image',
            field=models.ImageField(upload_to='event/2023-11-04/'),
        ),
        migrations.AlterField(
            model_name='shelterchild',
            name='child_image',
            field=models.ImageField(upload_to='shelter-child/2023-11-04/'),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='tm_image',
            field=models.ImageField(upload_to='team-member/2023-11-04/'),
        ),
    ]
