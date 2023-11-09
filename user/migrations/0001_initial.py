# Generated by Django 4.2.6 on 2023-11-02 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=250, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('role', models.CharField(choices=[('ADMIN', 'Admin'), ('DONAR', 'Donar'), ('STAFF', 'Staff')], max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
