
"""
Contains tables of database
"""

from django.db import models

from model_utils.models import TimeStampedModel

class Student(models.Model):
    """
    database columns for student table
    """
    student_id = models.IntegerField("Student_id", primary_key = True)
    unh_id = models.CharField("UNH_id", unique = True, blank = False, max_length=15)
    last_name = models.CharField("Last Name", max_length=255)
    first_name = models.CharField("First Name", max_length=255)
    school_email = models.EmailField("School Mail_Id", max_length=255)
    major = models.CharField("Major", max_length=255)
    degree = models.CharField("Degree", max_length=255)
    linkedin = models.CharField("Linkedin URL", max_length=255)

    def __str__(self):
        name = self.last_name + " " +  self.first_name
        return name

class Internship(models.Model):
    """
    database columns for Internship table
    """
    internship_id = models.IntegerField("Internship_Id", primary_key = True)
    position = models.CharField("Position", max_length = 100)
    pay = models.CharField("Pay per Hour", max_length = 5)
    organization_name = models.CharField("Organization_Name", max_length = 255)
    organization_url = models.CharField("Organization_url", max_length = 255, null = False)
    organization_address = models.CharField("Organization_Address",max_length = 255)
    supervisor_name = models.CharField("SuperVisor Name", max_length = 255)
    supervisor_position = models.CharField("Supervisor Position" ,max_length = 255)
    supervisor_email = models.CharField("Supervisor Email", max_length = 255)
    supervisor_phone = models.CharField("SuperVisor Phone", max_length = 255)

    def __str__(self):
        return self.position + self.organization_name


class Internship_Assignment(models.Model):
    """
    database columns for InternshipAssignment table
    """
    Student_id = models.ForeignKey('Student', on_delete=models.CASCADE)
    internship_id = models.ForeignKey('Internship', on_delete=models.CASCADE)
    course_id = models.CharField("Couse_id", max_length = 20)
    credits = models.CharField("Credits", max_length = 10)
    semester = models.CharField("Semester", max_length = 10)
    year = models.CharField("Year", max_length = 10)
    instructor = models.CharField("Instructor", max_length = 36)
    start_date = models.CharField("Start Date", max_length = 36)
    end_date = models.CharField("End Date", max_length = 36)

    def __str__(self):
        return self.course_id
