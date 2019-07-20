from django.urls import path

from .views import ContentList, ContentDetail

app_name = "content"
urlpatterns = [
    path('from_contents/', ContentList.as_view(), name='contents_list'),
    path('from_contents/<int:pk>/', ContentDetail.as_view(), name="content_detail" ),
]