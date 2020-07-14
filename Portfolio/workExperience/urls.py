from django.urls import path
from . import views
app_name = "workExperience"
urlpatterns = [
    path('', views.work_experience, name="workExperience"),
]
