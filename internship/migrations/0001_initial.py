# Generated by Django 3.1.2 on 2020-11-30 02:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Internship',
            fields=[
                ('internship_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Internship_Id')),
                ('position', models.CharField(max_length=100, verbose_name='Position')),
                ('pay', models.CharField(max_length=5, verbose_name='Pay per Hour')),
                ('organization_name', models.CharField(max_length=255, verbose_name='Organization_Name')),
                ('organization_url', models.CharField(max_length=255, verbose_name='Organization_url')),
                ('organization_address', models.CharField(max_length=255, verbose_name='Organization_Address')),
                ('supervisor_name', models.CharField(max_length=255, verbose_name='SuperVisor Name')),
                ('supervisor_position', models.CharField(max_length=255, verbose_name='Supervisor Position')),
                ('supervisor_email', models.CharField(max_length=255, verbose_name='Supervisor Email')),
                ('supervisor_phone', models.CharField(max_length=255, verbose_name='SuperVisor Phone')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Student_id')),
                ('unh_id', models.CharField(max_length=15, unique=True, verbose_name='UNH_id')),
                ('last_name', models.CharField(max_length=255, verbose_name='Last Name')),
                ('first_name', models.CharField(max_length=255, verbose_name='First Name')),
                ('school_email', models.EmailField(max_length=255, verbose_name='School Mail_Id')),
                ('major', models.CharField(max_length=255, verbose_name='Major')),
                ('degree', models.CharField(max_length=255, verbose_name='Degree')),
                ('linkedin', models.CharField(max_length=255, verbose_name='Linkedin URL')),
            ],
        ),
        migrations.CreateModel(
            name='Internship_Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(max_length=20, verbose_name='Couse_id')),
                ('credits', models.CharField(max_length=10, verbose_name='Credits')),
                ('semester', models.CharField(max_length=10, verbose_name='Semester')),
                ('year', models.CharField(max_length=10, verbose_name='Year')),
                ('instructor', models.CharField(max_length=36, verbose_name='Instructor')),
                ('start_date', models.CharField(max_length=36, verbose_name='Start Date')),
                ('end_date', models.CharField(max_length=36, verbose_name='End Date')),
                ('internship_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='internship.internship')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='internship.student')),
            ],
        ),
    ]
