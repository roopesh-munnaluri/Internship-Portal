"""
urls.py
"""
from django.urls import path, re_path, include #pylint: disable = unused-import
from internship.views import * #pylint: disable = unused-wildcard-import,wildcard-import
from . import views #pylint: disable = relative-beyond-top-level,unused-import


urlpatterns = [
        path('', HomepageView.as_view(), name='home'),
        path('Upload/', FileuploadView.import_file, name='import_file' ),
        path('students_list/', StudentListView.display_students, name='display_students' ),
        path('internship_list/', InternshipListView.display_internship, name='display_internship' ),
        path('internshipassignment_list/', InternshipassignmentListView.display_internshipassignment
        , name='display_internshipassignment' ),
        path('remove-data/', remove_all_data, name='remove-data' ),
        path('login/',Authentication.login_request,name = 'login'),
        path('logout/',Authentication.logout_request,name='logout'),
        path('register/',Authentication.register_request,name = 'register')

    ]
