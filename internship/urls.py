"""
urls.py
"""
from django.urls import path
#from django.conf.urls import url
from internship.views import FileuploadView, HomepageView, StudentListView, remove_all_data


urlpatterns = [
        path('', HomepageView.as_view(), name='home'),
        path('upload/', FileuploadView.import_file, name='import_file' ),
        path('student-list/', StudentListView.display_students, name='display_students' ),
        path('remove-data/', remove_all_data, name='remove-data' ),
    ]
