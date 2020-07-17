from django.urls import path
from . import views
app_name = "certifications"
urlpatterns = [
    path('', views.certifications, name="certifications"),
]
