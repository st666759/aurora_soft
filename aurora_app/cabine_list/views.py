from django.shortcuts import render,redirect 
from cabine_list.models import cabine

# Create your views here.

def cabines(request):
    cabines_list = cabine.object.all()
    return render(request, 'cabine_list/cabines.html', {'cabines_list':cabines_list})

def change_status_cabine(request, cabine_id):
    cabine = cabine.objects.get(pk=cabine_id)
    cabine.status = not cabine.status
    cabine.save()
    return redirect('cabines')