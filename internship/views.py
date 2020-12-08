"""
views.py
"""
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import TemplateView, ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Student, Internship_Assignment,Internship
from .forms import StudentSearchForm,InternshipSearchForm,InternshipassignmentSearchForm,NewUserForm
from .imports import import_data, import_faker
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group


class HomepageView(TemplateView): #pylint: disable = no-member
    """
    template for home page
    """
    template_name = 'base.html'

class FileuploadView(TemplateView): #pylint: disable = no-member
    """
    Template for uploading excel sheet to database
    """
    template_name = 'Upload.html'

    def import_file(request): #pylint: disable = no-self-argument
        """
        getting file name from template
        """
        if request.method=='POST' : #pylint: disable = no-member
            if 'docfile' in request.FILES: #pylint: disable = no-member
                files = request.FILES['docfile'] #pylint: disable = no-member
                import_data.import_data(files)
            else:
                import_faker.import_faker()
        return render(request, 'Upload.html')


class StudentListView(ListView): # pylint: disable=too-many-ancestors
    """
    listing all the details of Student table
    """
    model = Student

    @allowed_users(allowed_roles=['upcoming'])
    def display_students(request): #pylint: disable = no-self-argument
        """
        searching Student table based on first_name and last_name provided by user
        """
        button = "students"
        student_items = Student.objects.all() #pylint: disable = no-member
        form = StudentSearchForm(request.POST or None) #pylint: disable = no-member
        context = {
            'button' : button,
            'student_items' : student_items,
            'form' : form
        }
        if request.method == 'POST': #pylint: disable = no-member
            student_items = Student.objects.filter(last_name__icontains=form['last_name'].value()) #pylint: disable = no-member
            context = {
                "student_items" : student_items,
                "form": form
            }
        return render(request, 'students_list.html', context)


class InternshipListView(ListView): # pylint: disable=too-many-ancestors
    """
    listing all the details of Internship table
    """

    def display_internship(request): #pylint: disable = no-self-argument
        """
        displaying and searching Internship table based on organization_name provided by user
        """
        button = "Internship"
        Internship_items = Internship.objects.all() #pylint: disable = no-member
        form = InternshipSearchForm(request.POST or None) #pylint: disable = no-member
        context = {
            'button' : button,
            'Internship_items' : Internship_items,
            'form' : form
        }
        if request.method == 'POST':
            Internship_items = Internship.objects.filter(
            organization_name__icontains=form['organization_name'].value()) #pylint: disable = no-member
            context = {
                "Internship_items" : Internship_items,
                "form": form
            }
        return render(request, 'internship_list.html', context)

class InternshipassignmentListView(ListView): # pylint: disable=too-many-ancestors
    """
    listing all the details of Internship table
    """

    def display_internshipassignment(request): #pylint: disable = no-self-argument
        """
        displaying and searching Internship_Assignment table based on year provided by user
        """
        button = "Internshipassignment"
        Internshipassignment_items = Internship_Assignment.objects.all() #pylint: disable = no-member
        form = InternshipassignmentSearchForm(request.POST or None) #pylint: disable = no-member
        year = Internship_Assignment.objects.all() #pylint: disable = no-member
        context = {
            'button' : button,
            'Internshipassignmet_items' : Internshipassignment_items ,
            'form' : form,
        }
        if request.method == 'POST':
            Internshipassignment_items = Internship_Assignment.objects.filter( #pylint: disable = no-member
            year__icontains=form['year'].value()) #pylint: disable = no-member
            context = {
                "Internshipassignment_items" : Internshipassignment_items,
                "form": form,
                'year' : year
            }
        return render(request, 'internshipassignment_list.html', context)

class Authentication(TemplateView):
    """
    For Authentication of user
    """
    @unauthenticated_user
    def login_request(request): #pylint: disable = no-self-argument
        """
        for checking username and password for login
        """
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')
        context = {}
        return render(request, 'login.html', context)
    def logout_request(request): #pylint: disable = no-self-argument
        """
        logout
        """
        logout(request)
        return redirect('login')


    @unauthenticated_user
    def register_request(request): #pylint: disable = no-self-argument
        """
        For registering user
        """
        form = NewUserForm()
        if request.method == 'POST':
            form = NewUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                group = form.cleaned_data['group']
                group = Group.objects.get(name=group)
                user.groups.add(group)
                return redirect('login')
        context = {'form':form}
        return render(request, 'register.html', context)

def remove_all_data(request):
    """
    clearing the database tables
    """
    Student.objects.all().delete() #pylint: disable = no-member
    Internship_Assignment.objects.all().delete() #pylint: disable = no-member
    Internship.objects.all().delete() #pylint: disable = no-member
    return render(request, 'base.html')
