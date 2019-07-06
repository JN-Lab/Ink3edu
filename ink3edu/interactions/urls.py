from django.urls import path

from .views import StudentList, MentorList

app_name = "interactions"
urlpatterns = [
    path('students/', StudentList.as_view(), name='students_list'),
    path('mentors/', MentorList.as_view(), name='mentors_list'),
]