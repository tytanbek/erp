from django.urls import path
from . import views

urlpatterns = [
    path('', views.application_form, name='application_form'),
    path('success/', views.success_page, name='success'),
    path('3f8f1c5e-7c3e-4d6a-9e6a-2b0b3d9a8c1f/', views.statistics, name='statistics'),
    path('application/<int:pk>/', views.application_detail, name='application_detail'),
]
