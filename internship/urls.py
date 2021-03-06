"""
urls.py
"""
from django.urls import path, re_path, include #pylint: disable = unused-import
from internship.views import * #pylint: disable = unused-wildcard-import,wildcard-import
from . import views #pylint: disable = relative-beyond-top-level,unused-import


urlpatterns = [
        path('', HomepageView.home, name='home'),
        path('Upload/', FileuploadView.import_file, name='import_file' ),
        path('students_list/', StudentListView.display_students, name='display_students' ),
        path('internship_list/', InternshipListView.display_internship, name='display_internship' ),
        path('internshipassignment_list/', InternshipassignmentListView.display_internshipassignment
        , name='display_internshipassignment' ),
        path('remove-data/', remove_all_data, name='remove-data' ),
        path('login/',Authentication.login_request,name = 'login'),
        path('logout/',Authentication.logout_request,name='logout'),
        path('request/',Authentication.register_request,name = 'register'),
        path('update_student/<int:pk>/', UpdateView.studentupdate, name='update_student'),
        path('delete/<int:pk>/', DeleteView.deleteStudent, name="delete_student" ),
        path('register/',Authentication.register_request,name = 'register'),
        path('add_student/',AddView.add_student,name='add_student'),
        path('add_internship/',AddView.add_Intern,name='add_internship'),
        path('add_intern_assign/',AddView.add_intern_assign,name='add_intern_assign'),
        path('update_internship/<int:pk>/',UpdateView.update_internship,name = 'update_internship'),
        path('delete_internship/<int:pk>/',DeleteView.delete_internship,name='delete_internship'),
        path('update_internshipassignment/<int:pk>/',UpdateView.update_internshipassignment,name = 'update_internshipassignment'),
        path('delete_internshipassignment/<int:pk>/',DeleteView.delete_internshipassignment,name='delete_internshipassignment')


    ]
