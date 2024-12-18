# Generated by Django 4.2.6 on 2023-11-02 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_title', models.CharField(max_length=250)),
                ('event_image', models.ImageField(upload_to='event/2023-11-02/')),
                ('event_date', models.DateField()),
                ('event_time', models.TimeField()),
                ('event_status', models.BooleanField()),
                ('event_type', models.CharField(max_length=40)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank_name', models.CharField(max_length=50, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShelterChild',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('child_name', models.CharField(max_length=250)),
                ('child_full_name', models.CharField(max_length=250)),
                ('child_image', models.ImageField(upload_to='shelter-child/2023-11-02/')),
                ('child_father_name', models.CharField(max_length=250)),
                ('child_mother_name', models.CharField(max_length=250)),
                ('child_date_of_birth', models.DateField()),
                ('child_birth_certificate_number', models.CharField(max_length=250, unique=True)),
                ('child_blood', models.CharField(max_length=250)),
                ('child_weight', models.FloatField()),
                ('child_height', models.FloatField()),
                ('child_present_address', models.TextField()),
                ('child_parmanent_address', models.TextField()),
                ('child_discription', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tm_name', models.CharField(max_length=250, unique=True)),
                ('tm_email', models.EmailField(max_length=254, unique=True)),
                ('tm_phone', models.CharField(max_length=11, unique=True)),
                ('tm_image', models.ImageField(upload_to='team-member/2023-11-02/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MemberRank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mr_start_date', models.DateField(blank=True, null=True)),
                ('mr_end_date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('mr_level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='psf.rank')),
                ('mr_team_member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='psf.teammember')),
            ],
        ),
        migrations.CreateModel(
            name='ChildProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cp_education', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cp_child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='psf.shelterchild')),
            ],
        ),
    ]
