"""hospitalmanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from hospitalapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomePage,name=''),
    path('adminclick',views.admin_view,name='admin'),
    path('patientclick',views.patient_view,name='patient'),


    path('admin_signup',views.admin_signup_view,name='a_signup'),
    path('admin_login',views.admin_login_view,name='a_login'),

    path('patient_signup',views.patient_signup_view,name='p_signup'),
    path('patient_login',views.patient_login_view,name='p_login'),

    path('admin_dashboard',views.admin_dashboard,name='admin_dashboard'),
    path('patient_dashboard',views.patient_dashboard,name='patient_dashboard'),

    path('patient_appointment',views.patient_appointment,name='appointment'),
    path('reject/<id>',views.appointment_reject,name='reject'),
    path('accept/<id>',views.appointment_accept,name='accept'),
    path('check_status',views.check_status,name='checkstatus'),



    path('adminclick',views.admin_logout_view,name='a_logout'),
    path('patientclick',views.patient_logout_view,name='p_logout'),

]
