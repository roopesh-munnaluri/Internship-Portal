"""

"""
from openpyxl import load_workbook
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Student, Internship_Assignment,Internship
from django.views.generic import ListView
from .forms import StudentSearchForm


class HomepageView(TemplateView):
    template_name = 'index.html'

def display_students(request):
    button = "students"
    student_items = Student.objects.all()
    form = StudentSearchForm(request.POST or None)
    context = {
        'button' : button,
        'student_items' : student_items,
        'form' : form
    }
    if request.method == 'POST':
        student_items = Student.objects.filter(first_name__icontains=form['first_name'].value(),
                                          last_name__icontains=form['last_name'].value()
                                          )
        context = {
            "student_items" : student_items,
            "form": form
        }
    return render(request, 'index.html', context)

class FileuploadView(TemplateView):
    template_name = 'Upload.html'

    def import_data(request):
        wb = load_workbook(filename = request, data_only=True)
        sheet = wb.active
        student = []
        internship_assignment = []
        internship =[]
        id = 1
        intern_id  = 1
        intern_assing_id = 1
        for i in range(2,sheet.max_row+1):
            std = [id, sheet.cell(row=int(i), column=3).value,
                        sheet.cell(row=int(i), column=1).value,
                        sheet.cell(row=int(i), column=2).value,
                        sheet.cell(row=int(i), column=7).value,
                        sheet.cell(row=int(i), column=4).value,
                        sheet.cell(row=int(i), column=5).value,
                        sheet.cell(row=int(i), column=8).value]
            a = Student(id, sheet.cell(row=int(i), column=3).value,
                        sheet.cell(row=int(i), column=1).value,
                        sheet.cell(row=int(i), column=2).value,
                        sheet.cell(row=int(i), column=7).value,
                        sheet.cell(row=int(i), column=4).value,
                        sheet.cell(row=int(i), column=5).value,
                        sheet.cell(row=int(i), column=8).value)
            a.save()
            student.append(std)

            if i == 1:
                address = sheet.cell(row=int(i), column=20).value + " " + sheet.cell(row=int(i), column=21).value + " " + sheet.cell(row=int(i), column=22).value + " " + "Pincode"
            else:
                address = sheet.cell(row=int(i), column=20).value + " " + sheet.cell(row=int(i), column=21).value + " " + sheet.cell(row=int(i), column=22).value + " " + str(sheet.cell(row=int(i), column=23).value)

            intern = [sheet.cell(row=int(i), column=14).value,
            sheet.cell(row=int(i), column=15).value,
            sheet.cell(row=int(i), column=18).value,
            sheet.cell(row=int(i), column=19).value,
            address,
            sheet.cell(row=int(i), column=24).value,
            sheet.cell(row=int(i), column=25).value,
            sheet.cell(row=int(i), column=26).value,
            sheet.cell(row=int(i), column=27).value]
            print(intern_id,'intern_id')
            I = Internship(intern_id,sheet.cell(row=int(i), column=14).value,
            str(sheet.cell(row=int(i), column=15).value),
            sheet.cell(row=int(i), column=18).value,
            sheet.cell(row=int(i), column=19).value,
            address,
            sheet.cell(row=int(i), column=24).value,
            sheet.cell(row=int(i), column=25).value,
            sheet.cell(row=int(i), column=26).value,
            sheet.cell(row=int(i), column=27).value)
            print(I,'jdhqejf')
            I.save()
            internship.append(intern)

            intern_assign = [sheet.cell(row=int(i), column=9).value,
            str(sheet.cell(row=int(i), column=10).value),
            sheet.cell(row=int(i), column=11).value,
            str(sheet.cell(row=int(i), column=12).value),
            sheet.cell(row=int(i), column=13).value,
            str(sheet.cell(row=int(i), column=16).value),
            str(sheet.cell(row=int(i), column=17).value),]


            intern_assign = [sheet.cell(row=int(i), column=9).value,
            str(sheet.cell(row=int(i), column=10).value),
            sheet.cell(row=int(i), column=11).value,
            str(sheet.cell(row=int(i), column=12).value),
            sheet.cell(row=int(i), column=13).value,
            str(sheet.cell(row=int(i), column=16).value),
            str(sheet.cell(row=int(i), column=17).value),]

            b = Internship_Assignment(intern_assing_id,id,intern_id,
            sheet.cell(row=int(i), column=9).value,
            str(sheet.cell(row=int(i), column=10).value),
            sheet.cell(row=int(i), column=11).value,
            str(sheet.cell(row=int(i), column=12).value),
            sheet.cell(row=int(i), column=13).value,
            str(sheet.cell(row=int(i), column=16).value),
            str(sheet.cell(row=int(i), column=17).value))

            b.save()
            internship_assignment.append(intern_assign)
            id = id + 1
            intern_id = intern_id + 1
            intern_assing_id = intern_assing_id + 1

            id = id + 1
            intern_id = intern_id + 1

            a.save()
            student.append(std)

            I.save()
            internship.append(intern)

            b.save()
            internship_assignment.append(intern_assign)

    def import_file(request):
        if request.method=='POST' and 'docfile' in request.FILES:
            files = request.FILES['docfile']
            FileuploadView.import_data(files)
        return render(request, 'Upload.html')

class StudentListView(ListView):
    model = Student

class Internship_AssignmentListView(ListView):
    model = Internship_Assignment.objects.all()

class InternshipListView(ListView):
    model = Internship.objects.all()

from internship.models import *

def remove_all_data(request):

        Student.objects.all().delete()
        Internship_Assignment.objects.all().delete()
        Internship.objects.all().delete()
        return render(request, 'base.html')
