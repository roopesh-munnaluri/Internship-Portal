# Generated by Django 3.1.2 on 2020-11-14 02:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Internship',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('internship_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Internship_Id')),
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
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('student_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Student_id')),
                ('unh_id', models.CharField(max_length=15, verbose_name='UNH_id')),
                ('last_name', models.CharField(max_length=255, verbose_name='Last Name')),
                ('first_name', models.CharField(max_length=255, verbose_name='First Name')),
                ('school_email', models.EmailField(max_length=255, verbose_name='School Mail_Id')),
                ('major', models.CharField(max_length=255, verbose_name='Major')),
                ('degree', models.CharField(max_length=255, verbose_name='Degree')),
                ('linkedin', models.CharField(max_length=255, verbose_name='Linkedin URL')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Internship_Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('course_id', models.CharField(max_length=20, verbose_name='Couse_id')),
                ('credits', models.CharField(max_length=10, verbose_name='Credits')),
                ('semester', models.CharField(max_length=10, verbose_name='Semester')),
                ('year', models.CharField(max_length=10, verbose_name='Year')),
                ('instructor', models.CharField(max_length=36, verbose_name='Instructor')),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(verbose_name='End Date')),
                ('internship_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='internship.internship')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='internship.student')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
