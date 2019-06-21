from django.urls import path

from .views import TrainingList, TrainingDetail

app_name = "trainings"

urlpatterns = [
    path('', TrainingList.as_view(), name='trainings_list'),
    path('<int:pk>/', TrainingDetail.as_view(), name='training_detail'),
]
