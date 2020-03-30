"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers
from doctor import views as views_doctor
from patient import views as views_patient
from room_patient import views as views_room_patient
from chemicals import views as view_chemicals

router = routers.DefaultRouter()
router.register(r'doctor', views_doctor.DoctorViewSet)
router.register(r'patient', views_patient.PatientViewSet)
router.register(r'room_patient', views_room_patient.RoomPatientViewSet)
router.register(r'chemicals', view_chemicals.ChemicalViewSet)
urlpatterns = [
    url('', include(router.urls)),
    url('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
