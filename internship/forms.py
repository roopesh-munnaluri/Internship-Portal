from django import forms
from .models import Student


class StudentSearchForm(forms.ModelForm):
   class Meta:
     model = Student
     fields = ['first_name', 'last_name']
