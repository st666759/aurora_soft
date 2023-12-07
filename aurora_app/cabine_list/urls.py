from . import views
from django.urls import path

urlpatterns = [
    path('', views.cabines, name='cabines'),
    path('status/<int:cabine_id>/', views.change_status_cabine, name='cabine_status'),
]

