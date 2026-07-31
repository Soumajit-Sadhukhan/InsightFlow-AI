from django.urls import path
from .views import ProjectCreateView, ProjectListView,ProjectDetailView



urlpatterns = [
    path("", ProjectCreateView.as_view(), name="project-create"),
    path("all/", ProjectListView.as_view(), name="project-list"),
    path("<int:pk>/", ProjectDetailView.as_view(),name="project-detail")
    
]
