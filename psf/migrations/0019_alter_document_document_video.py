# Generated by Django 4.2.7 on 2024-01-02 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psf', '0018_alter_document_document_video_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document_video',
            field=models.TextField(blank=True, null=True),
        ),
    ]
