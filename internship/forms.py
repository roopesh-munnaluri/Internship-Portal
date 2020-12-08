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
from django.forms import ModelForm

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

<<<<<<< HEAD
    def save(self, commit=True):
        """
        For saving data
        """
        user = super(NewUserForm, self).save(commit=False) #pylint: disable=super-with-arguments
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
<<<<<<< .merge_file_Bn8Mw6
=======

class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ['student_id','unh_id','last_name','first_name','school_email','major','degree','linkedin']
>>>>>>> .merge_file_0RThr6
=======
    # def save(self, commit=True):
    #     """
    #     For saving data
    #     """
    #     user = super(NewUserForm, self).save(commit=False) #pylint: disable=super-with-arguments
    #     user.email = self.cleaned_data["email"]
    #     if commit:
    #         user.save()
    #     return user
>>>>>>> roopesh-sprint-5
