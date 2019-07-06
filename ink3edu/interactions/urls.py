from django.urls import path

from .views import StudentList, MentorList, StudentDetail, MentorDetail

app_name = "interactions"
urlpatterns = [
    path('students/', StudentList.as_view(), name='students_list'),
    path('students/<int:pk>/', StudentDetail.as_view(), name='student_detail'),
    path('mentors/', MentorList.as_view(), name='mentors_list'),
    path('mentors/<int:pk>/', MentorDetail.as_view(), name='mentor_detail'),
]