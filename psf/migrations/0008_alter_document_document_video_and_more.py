# Generated by Django 4.2.7 on 2023-11-14 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psf', '0007_alter_document_document_video_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document_video',
            field=models.FileField(upload_to='document/2023-11-14/'),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_image',
            field=models.ImageField(upload_to='event/2023-11-14/'),
        ),
        migrations.AlterField(
            model_name='shelterchild',
            name='child_image',
            field=models.ImageField(upload_to='shelter-child/2023-11-14/'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='slider_image',
            field=models.ImageField(upload_to='slider/2023-11-14/'),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='tm_image',
            field=models.ImageField(upload_to='team-member/2023-11-14/'),
        ),
    ]
