from openpyxl import load_workbook
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Student, Internship_Assignment,Internship

class HomepageView(TemplateView):
    template_name = 'index.html'

class FileuploadView(TemplateView):
    template_name = 'Upload.html'

    def import_data(request):
        print('import_data')
        wb = load_workbook(filename = request, data_only=True)
        sheet = wb.active
        student = []
        internship_assignment = []
        internship =[]
        for i in range(2,sheet.max_row+1):
            a = Student(sheet.cell(row=int(i), column=1).value,sheet.cell(row=int(i), column=4).value,sheet.cell(row=int(i),
                 column=2).value,sheet.cell(row=int(i), column=3).value,
                 sheet.cell(row=int(i), column=8).value,
                 sheet.cell(row=int(i), column=5).value,
                 sheet.cell(row=int(i), column=6).value,
                 sheet.cell(row=int(i), column=7).value)
            a.save()


    def import_file(request):
        if request.method=='POST' and 'docfile' in request.FILES:
            print('import_file success-1')
            files = request.FILES['docfile']
            FileuploadView.import_data(files)
            print('import_file success')
        print('import_file fail')
        return render(request, 'Upload.html')


# Create your views here.
