"""
forms.py
author: Mukesh
Date: 11/22/2020
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from .models import Student # pylint: disable=relative-beyond-top-level
from .models import Internship # pylint: disable=relative-beyond-top-level
from .models import Internship_Assignment # pylint: disable=relative-beyond-top-level

class StudentSearchForm(forms.ModelForm): # pylint: disable=too-few-public-methods
    """
    Used for searching Student Data

    """
    class Meta: # pylint: disable=too-few-public-methods
        """
        For including fields for searching
        """
        model = Student
        fields = ['last_name']


class InternshipSearchForm(forms.ModelForm): # pylint: disable=too-few-public-methods
    """
    Used for searching Internship Data

    """
    class Meta: # pylint: disable=too-few-public-methods
        """
        For including fields for searching
        """
        model = Internship
        fields = ['organization_name']

class InternshipassignmentSearchForm(forms.ModelForm): # pylint: disable=too-few-public-methods
    """
    Used for searching Internship Data

    """
    class Meta: # pylint: disable=too-few-public-methods
        """
        For including fields for searching
        """
        model = Internship_Assignment
        fields = ['year']

class NewUserForm(UserCreationForm):
    """
    Used for register account
    """
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True)
    class Meta: #pylint: disable=too-few-public-methods
        """
        For including fields for register
        """
        model = User
        fields = ("username", "email", "password1", "password2","group")

class StudentForm(forms.ModelForm):
	"""
	student form
	"""
	class Meta: # pylint: disable=R0903
		"""
		fields for student form
		"""
		model = Student
		fields = ['student_id','unh_id','last_name','first_name',
			'school_email','major','degree','linkedin']


class InternshipForm(forms.ModelForm):
	"""
	intership form
	"""
	class Meta: # pylint: disable=R0903
		"""
		fields for intership form
		"""
		model = Internship
		fields = [
			'internship_id','position','pay','organization_name',
			'organization_url', 'organization_address',
			'supervisor_name', 'supervisor_position',
			'supervisor_email', 'supervisor_phone'
		]


class InternshipAssignmentForm(forms.ModelForm):
    """
    intership Assignment form
    """
    student_id = forms.ModelChoiceField(queryset=Student.objects.all(), required=True)
    internship_id = forms.ModelChoiceField(queryset=Internship.objects.all(),required=True)


    class Meta: # pylint: disable=R0903
        """
	    fields for intership Assignment form
	    """
        model = Internship_Assignment
        fields = ['student_id', 'internship_id','course_id','credits','semester','year',
			'instructor','start_date','end_date']
