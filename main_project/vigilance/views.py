
from django.shortcuts import render, redirect,  get_object_or_404
from django.http import JsonResponse

from django.http import HttpResponse
from .models import Vigilance , Complainant
from vip_ref.models import HOD

from .forms import ComplainantForm, AddVigDataForm

#from .forms import AddDataForm
# Create your views here.

def vig_home(request):
    data= Vigilance.objects.all()
    context= {'data':data}
    return render(request, 'vigilance/vig_home.html', context)

def vig_add_data(request):

    if request.method== "POST":
        form= AddVigDataForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            
            form.save()
            return redirect('vig:vig_home')
    context= {'form' : AddVigDataForm()}

    return render(request, 'vigilance/vig_Add.html', context)


def vig_update_data(request, pk):
    #ref= Reference.objects.filter(id=pk)
    
    ref = get_object_or_404(Vigilance,id=pk)
    form = AddVigDataForm(request.POST or None, request.FILES or None, instance=ref)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('vig:vig_home')
    context = {
        'form': form,
        }
    return render(request, 'vigilance/vig_update.html', context)

def vig_view_ref(request, pk):
    ref_data = Vigilance.objects.get(id=pk)
    context= {'ref_data': ref_data}
    return render(request, 'vigilance/vig_view_ref.html', context) 





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
