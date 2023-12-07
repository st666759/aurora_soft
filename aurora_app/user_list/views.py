from django.shortcuts import render, redirect
from django.urls import path 
from user_list.models import user
from .forms  import userForm 


# Create your views here.
def users(request):
    user_list = user.objects.all()
    return render(request, 'user_list/users.html', {'user_list': user_list})


def change_status_user(request , user_id):
        user = user.objects.get(pk=user_id)
        user.status = not user.status
        user.save()
        return  redirect('users')


def create_user(request):
      form = userForm(request.POST or None)
      if form.is_valid():
            form.save()
            return redirect('user_list')
      return render(request, 'user_list/create.html' , {'form': form})

