# Generated by Django 3.1.1 on 2020-11-08 03:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('intern_data', '0004_auto_20201108_0256'),
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
            name='InternshipAssignment',
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
                ('internship_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='intern_data.internship')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='intern_data.student')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
