from django.conf.urls import url, include
from . import views
urlpatterns = [
    url('doctor/', views.DoctorViewSet),
]