from django.urls import path

from .views import StudentList

app_name = "interactions"
urlpatterns = [
    path('students/', StudentList.as_view(), name='students_list'),
]