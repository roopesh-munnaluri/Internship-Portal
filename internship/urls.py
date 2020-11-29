"""
urls.py
"""
from django.urls import path, re_path
from . import views
from internship.views import FileuploadView, HomepageView, StudentListView,InternshipListView,InternshipassignmentListView, remove_all_data


urlpatterns = [
        path('', HomepageView.as_view(), name='home'),
        path('Upload/', FileuploadView.import_file, name='import_file' ),
        path('students_list/', StudentListView.display_students, name='display_students' ),
        path('internship_list/', InternshipListView.display_internship, name='display_internship' ),
        path('internshipassignment_list/', InternshipassignmentListView.display_internshipassignment, name='display_internshipassignment' ),
        path('remove-data/', remove_all_data, name='remove-data' ),
    ]
