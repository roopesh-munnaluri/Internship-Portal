from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import Student
from .models import Internship_Assignment
from .models import Internship

class HomepageView(TemplateView):
    template_name = 'index.html'

class StudentListView(ListView):
    model = Student

class Internship_AssignmentListView(ListView):
    model = Internship_Assignment

class InternshipListView(ListView):
    model = Internship
