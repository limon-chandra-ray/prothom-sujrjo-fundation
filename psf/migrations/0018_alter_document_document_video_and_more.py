# Generated by Django 4.2.7 on 2024-01-01 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psf', '0017_alter_document_document_video_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document_video',
            field=models.FileField(upload_to='document/2024-01-02/'),
        ),
        migrations.AlterField(
            model_name='shelterchild',
            name='child_image',
            field=models.ImageField(upload_to='shelter-child/2024-01-02/'),
        ),
    ]
