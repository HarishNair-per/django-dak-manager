
from django.shortcuts import render, redirect
from django.http import JsonResponse

from django.http import HttpResponse
from .models import Vigilance , Complainant
from .forms import ComplainantForm

#from .forms import AddDataForm
# Create your views here.

def vig_home(request):
    return HttpResponse("Vigilance Home")
# Create your views here.

# views.py


def createComplainant(request):
    persons = Complainant.objects.all()

    if request.method == 'POST':
        form = ComplainantForm(request.POST)
        if form.is_valid():
            Complainant.objects.update_or_create(
                name=form.cleaned_data['name'],
                defaults={
                    'address': form.cleaned_data['address'],
                    'mobile': form.cleaned_data['mobile']
                }
            )
            form = ComplainantForm()
            #return redirect('person_form')  # reload or redirect as needed
    else:
        form = ComplainantForm()

    return render(request, 'vigilance/complainant_entry.html', { 'form': form,  'persons': persons })


# JSON Data fetching from URL

def get_person_details(request):
    name = request.GET.get('name')
    try:
        person = Complainant.objects.get(name=name)
        return JsonResponse({
            'address': person.address,
            'mobile': person.mobile
        })
    except Complainant.DoesNotExist:
        return JsonResponse({'address': '', 'mobile': ''})


""" def createComplainant(request):
    
    complainants = Complainant.objects.all()
    if request.method == 'POST':

        complainant_name = request.POST.get('complainant_name')
        complainant_obj, created = Complainant.objects.get_or_create(name=complainant_name.title()   )

         #VIP.objects.create(
            
            #vip=request.POST.get('vip_name'),
        

        complainant_obj.name=complainant_obj.name.title()
        complainant_obj.address= request.POST.get('address')
        complainant_obj.mobile= request.POST.get('mobile')
        

        complainant_obj.save()
        print(complainant_obj, created)
        #return redirect('vip:home')

    context = {'complainants': complainants}
    return render(request, 'vigilance/complainant_entry.html', context)
 """
