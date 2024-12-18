# Generated by Django 4.2.7 on 2023-11-14 14:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0003_alter_customuser_role'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('user.customuser',),
            managers=[
                ('staff', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='SponsorProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sponsor_full_name', models.CharField(max_length=250)),
                ('sponsor_phone_number', models.CharField(blank=True, max_length=11, null=True)),
                ('sponsor_image', models.ImageField(blank=True, null=True, upload_to='sponsor/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sponsor_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
