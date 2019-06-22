from django.urls import path

from .views import TrainingLongList, TrainingSimpleList, TrainingLongDetail, TrainingSimpleDetail, SectionLongList, SectionSimpleList, SectionLongDetail, SectionSimpleDetail, ChapterList, ChapterDetail

app_name = "trainings"

urlpatterns = [
    # Enpoints to get trainings info
    path('from_trainings/simple/', TrainingSimpleList.as_view(), name='trainings_simple_list'),
    path('from_trainings/long/', TrainingLongList.as_view(), name='trainings_long_list'),
    path('from_trainings/simple/<int:pk>/', TrainingSimpleDetail.as_view(), name='training_simple_detail'),
    path('from_trainings/long/<int:pk>/', TrainingLongDetail.as_view(), name='training_long_detail'),
    # Endpoints to get sections info
    path('from_sections/simple/', SectionSimpleList.as_view(), name='sections_simple_list'),
    path('from_sections/long/', SectionLongList.as_view(), name='sections_long_list'),
    path('from_sections/simple/<int:pk>/', SectionSimpleDetail.as_view(), name='section_simple_detail'),
    path('from_sections/long/<int:pk>/', SectionLongDetail.as_view(), name='section_long_detail'),
    # Endpoints to get chapters info
    path('from_chapters/', ChapterList.as_view(), name='chapters_list'),
    path('from_chapters/<int:pk>/', ChapterDetail.as_view(), name='chapter_detail'),
]
