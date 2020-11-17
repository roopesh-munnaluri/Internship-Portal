"""

"""
from openpyxl import load_workbook
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Student, Internship_Assignment,Internship

class HomepageView(TemplateView):
    template_name = 'index.html'

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
        for i in range(2,sheet.max_row+1):
            std = [id, sheet.cell(row=int(i), column=4).value,
                        sheet.cell(row=int(i), column=2).value,
                        sheet.cell(row=int(i), column=3).value,
                        sheet.cell(row=int(i), column=8).value,
                        sheet.cell(row=int(i), column=5).value,
                        sheet.cell(row=int(i), column=6).value,
                        sheet.cell(row=int(i), column=7).value]
            a = Student(id, sheet.cell(row=int(i), column=4).value,
                        sheet.cell(row=int(i), column=2).value,
                        sheet.cell(row=int(i), column=3).value,
                        sheet.cell(row=int(i), column=8).value,
                        sheet.cell(row=int(i), column=5).value,
                        sheet.cell(row=int(i), column=6).value,
                        sheet.cell(row=int(i), column=7).value)
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

            I = Internship(intern_id,sheet.cell(row=int(i), column=14).value,
            str(sheet.cell(row=int(i), column=15).value),
            sheet.cell(row=int(i), column=18).value,
            sheet.cell(row=int(i), column=19).value,
            address,
            sheet.cell(row=int(i), column=24).value,
            sheet.cell(row=int(i), column=25).value,
            sheet.cell(row=int(i), column=26).value,
            sheet.cell(row=int(i), column=27).value)
            I.save()
            internship.append(intern)

            intern_assign = [sheet.cell(row=int(i), column=9).value,
            str(sheet.cell(row=int(i), column=10).value),
            sheet.cell(row=int(i), column=11).value,
            str(sheet.cell(row=int(i), column=12).value),
            sheet.cell(row=int(i), column=13).value,
            str(sheet.cell(row=int(i), column=16).value),
            str(sheet.cell(row=int(i), column=17).value),]

            b = Internship_Assignment(sheet.cell(row=int(i), column=9).value,
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


    def import_file(request):
        if request.method=='POST' and 'docfile' in request.FILES:
            files = request.FILES['docfile']
            FileuploadView.import_data(files)
        return render(request, 'Upload.html')

class StudentListView(ListView):
    model = Student

class Internship_AssignmentListView(ListView):
    model = Internship_Assignment

class InternshipListView(ListView):
    model = Internship
