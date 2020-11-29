"""
views.py
"""
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Student, Internship_Assignment,Internship
from .forms import StudentSearchForm,InternshipSearchForm,InternshipassignmentSearchForm
from .imports import import_data, import_faker


class HomepageView(TemplateView):
    """
    template for home page
    """
    template_name = 'base.html'

class FileuploadView(TemplateView):
    """
    Template for uploading excel sheet to database
    """
    template_name = 'Upload.html'

    def import_file(request):
        """
        getting file name from template
        """
        if request.method=='POST' :
            if 'docfile' in request.FILES:
                files = request.FILES['docfile']
                import_data.import_data(files)
            else:
                import_faker.import_faker()
        return render(request, 'Upload.html')

class StudentListView(ListView): # pylint: disable=too-many-ancestors
    """
    listing all the details of Student table
    """
    model = Student

    def display_students(request):
        """
        searching Student table based on first_name and last_name provided by user
        """
        button = "students"
        student_items = Student.objects.all()
        form = StudentSearchForm(request.POST or None)
        context = {
            'button' : button,
            'student_items' : student_items,
            'form' : form
        }
        if request.method == 'POST':
            student_items = Student.objects.filter(last_name__icontains=form['last_name'].value())
            context = {
                "student_items" : student_items,
                "form": form
            }
        return render(request, 'students_list.html', context)


class InternshipListView(ListView): # pylint: disable=too-many-ancestors
    """
    listing all the details of Internship table
    """

    def display_internship(request):
        button = "Internship"
        Internship_items = Internship.objects.all()
        form = InternshipSearchForm(request.POST or None)
        context = {
            'button' : button,
            'Internship_items' : Internship_items,
            'form' : form
        }
        if request.method == 'POST':
            Internship_items = Internship.objects.filter(organization_name__icontains=form['organization_name'].value())
            context = {
                "Internship_items" : Internship_items,
                "form": form
            }
        return render(request, 'internship_list.html', context)

class InternshipassignmentListView(ListView): # pylint: disable=too-many-ancestors
    """
    listing all the details of Internship table
    """

    def display_internshipassignment(request):
        button = "Internshipassignment"
        Internshipassignment_items = Internship_Assignment.objects.all()
        form = InternshipassignmentSearchForm(request.POST or None)
        year = Internship_Assignment.objects.all()
        context = {
            'button' : button,
            'Internshipassignmet_items' : Internshipassignment_items ,
            'form' : form,
        }
        if request.method == 'POST':
            Internshipassignment_items = Internship_Assignment.objects.filter(year__icontains=form['year'].value())
            context = {
                "Internshipassignment_items" : Internshipassignment_items,
                "form": form,
                'year' : year
            }
        return render(request, 'internshipassignment_list.html', context)

def remove_all_data(request):
    """
    clearing the database tables
    """
    Student.objects.all().delete()
    Internship_Assignment.objects.all().delete()
    Internship.objects.all().delete()
    return render(request, 'base.html')
