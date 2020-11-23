"""
forms.py
author: Mukesh
Date: 11/22/2020
"""
from django import forms
from .models import Student


class StudentSearchForm(forms.ModelForm): # pylint: disable=too-few-public-methods
    """
    Used for searching Student Data

    """
    class Meta: # pylint: disable=too-few-public-methods
        """
        For including fields for searching
        """
        model = Student
        fields = ['first_name', 'last_name']
