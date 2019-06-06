from django.urls import path

from .views import TrainingList

app_name = "trainings"
urlpatterns = [
    path('', TrainingList.as_view(), name='trainings_list'),
]