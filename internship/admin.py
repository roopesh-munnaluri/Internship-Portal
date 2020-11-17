"""
Names of tables in admin page
"""


from django.contrib import admin
from .models import Student, Internship, Internship_Assignment

admin.site.register(Student)
admin.site.register(Internship_Assignment)
admin.site.register(Internship)


# Register your models here.
