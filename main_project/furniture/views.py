from django.shortcuts import render
from django.http import HttpResponse
#from .models import Reference, HOD
#from .forms import AddDataForm
# Create your views here.

def fur_home(request):
    return HttpResponse("Furniture Home")