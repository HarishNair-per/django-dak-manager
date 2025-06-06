
from django.shortcuts import render, redirect,  get_object_or_404
from django.http import JsonResponse

from django.http import HttpResponse
import pandas as pd
from django.utils import timezone
from .models import Vigilance , Complainant
from vip_ref.models import HOD

from .forms import ComplainantForm, AddVigDataForm

#from .forms import AddDataForm
# Create your views here.

def vig_home(request):
    data= Vigilance.objects.select_related('vigilance_complainant').prefetch_related('vigilance_hod', 'vigilance_hod_reply')
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

def vig_to_excel(request):
    vigilances= Vigilance.objects.select_related('vigilance_complainant').prefetch_related('vigilance_hod','vigilance_hod_reply').all()


    # Get all field names from the Vigilance model
    vigilance_fields = [field.name for field in Vigilance._meta.fields]
    
    # Initialize a list to hold the data
    data = []
    
    for vigilance in vigilances:
        # Get the vigilance's data
        vigilance_data = {field: getattr(vigilance, field) for field in vigilance_fields}
        #vigilance_data['complainant_name'] = vigilance.vigilance_complainant.name # fecth the name of Foreign key but notneeded 
             
                
        vigilance_data['to_HOD'] = ', '.join(v.hod for v in vigilance.vigilance_hod.all()) # join many to many field object
        vigilance_data['from_HOD'] = ', '.join(v.hod for v in vigilance.vigilance_hod_reply.all())
        
                
        data.append(vigilance_data)
        
    
    # Convert the list of dictionaries to a pandas DataFrame
    df = pd.DataFrame(data)
    
    
    
    
    
    # Convert the queryset to a pandas DataFrame
    #df = pd.DataFrame(list(ref_data.values(*fields)))

    # Convert the queryset to a pandas DataFrame
    #df = pd.DataFrame(list(books.values('title', 'author__name')))
    
    for col in df.select_dtypes(include=['datetime64[ns, UTC]']).columns:
        df[col] = df[col].dt.tz_convert(None)

    # Create an Excel writer object
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=Vigilance_details.xlsx'
    
    # Write the DataFrame to the response
    df.to_excel(response, index=False)
    
    return response


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
