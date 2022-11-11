from django.urls import path
from .views import projectList, projectDetails
urlpatterns = [
    path('api', projectList.as_view()),
    path('api<int:pk>', projectDetails.as_view()),
]