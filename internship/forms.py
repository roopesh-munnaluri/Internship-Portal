"""
forms.py
author: Mukesh
Date: 11/22/2020
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Student # pylint: disable=relative-beyond-top-level
from .models import Internship
from .models import Internship_Assignment

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
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
