from django.urls import path
from .views import home, project, project_detail, contact

urlpatterns = [
    path("", home, name="home"),
    path("project/", project, name="project"),
    path("project/<int:pk>/", project_detail, name="project_detail"),
    path("contact/", contact, name="contact"),
]
