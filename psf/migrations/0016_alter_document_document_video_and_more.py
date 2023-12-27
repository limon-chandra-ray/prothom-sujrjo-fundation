# Generated by Django 4.2.7 on 2023-12-27 16:55

from django.db import migrations, models
import psf.models


class Migration(migrations.Migration):

    dependencies = [
        ('psf', '0015_alter_document_document_video_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document_video',
            field=models.FileField(upload_to='document/2023-12-27/'),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_image',
            field=models.ImageField(upload_to=psf.models.event_image_path),
        ),
        migrations.AlterField(
            model_name='galleryimage',
            name='gallery_image',
            field=models.ImageField(upload_to=psf.models.gallery_image_path),
        ),
        migrations.AlterField(
            model_name='shelterchild',
            name='child_image',
            field=models.ImageField(upload_to='shelter-child/2023-12-27/'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='slider_image',
            field=models.ImageField(upload_to=psf.models.slider_image_path),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='tm_image',
            field=models.ImageField(upload_to=psf.models.member_image_path),
        ),
        migrations.AlterField(
            model_name='usercontact',
            name='uc_status',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
