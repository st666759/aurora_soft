from . import views
from django.urls import path

urlpatterns = [      
    path('', views.users),    
    path('user_status_/<int:user_id>/', views.change_status_user, name='user_status' ) ,
    path('create/', views.create_user, name='create_author'),      
]