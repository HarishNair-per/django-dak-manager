import os
import pandas as pd
import mammoth 
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

import pandas as pd
from django.utils import timezone


from .models import Reference, HOD, VIP
from .forms import AddDataForm
from django.conf import settings

# Create your views here.


def vip_home(request):
    
    return render(request, 'vip_ref/viphome.html')


def home(request):
    data= Reference.objects.select_related('vip').prefetch_related('hod')
    context= {'data':data}
    return render(request, 'vip_ref/home.html', context)


def add_data(request):

    if request.method== "POST":
        form= AddDataForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            
            form.save()
            return redirect('vip:home')
    context= {'form' : AddDataForm()}

    return render(request, 'vip_ref/Add.html', context)


def update_data(request, pk):
    #ref= Reference.objects.filter(id=pk)
    
    ref = get_object_or_404(Reference,id=pk)
    form = AddDataForm(request.POST or None, request.FILES or None, instance=ref)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('vip:home')
    context = {
        'form': form,
        }
    return render(request, 'vip_ref/update.html', context)

'''def view_ref(request, pk):
    ref_data = Reference.objects.get(id=pk)
    absolute_url = request.build_absolute_uri(ref_data.subject_file.url)
    
    
           
    context= {'ref_data': ref_data, 'excel_url': absolute_url}
    return render(request, 'vip_ref/view_ref.html', context)
'''
 

def view_ref(request, pk):
    ref_data = Reference.objects.get(id=pk)
    #absolute_url = request.build_absolute_uri(ref_data.subject_file.url)
    
    
    # This block of code with show docx and excel file  for subject part-start
    """ 
    html_table=None
    html_doc=None
    file_end=None
    file_path = os.path.join(settings.MEDIA_ROOT, ref_data.subject_file.name)
    print(file_path)
    if ref_data.subject_file.name.endswith(".xlsx"):
        file_end='excel'
        df = pd.read_excel(file_path)
        df= df.fillna("")
        html_table = df.to_html(index=False)

    
    if ref_data.subject_file.name.endswith(".docx"):
        file_end='docx'
        with open(file_path, "rb") as docx_file:
            result = mammoth.convert_to_html(docx_file)
            html_doc = result.value # The generated HTML
            #messages = result.messages # Any messages, such as warnings during conversion
    print(file_end)  """
    # context= {'ref_data': ref_data, 'table_html': html_table,  "html_doc": html_doc,"file_end": file_end}
    # This block of code with show docx and excel file -start
    

    context= {'ref_data': ref_data}
    return render(request, 'vip_ref/view_ref.html', context) 


def createVIP(request):
    
    vips = VIP.objects.all()
    if request.method == 'POST':

        vip_name = request.POST.get('vip_name')
        vip, created = VIP.objects.get_or_create(vip=vip_name)

        """ VIP.objects.create(
            
            vip=request.POST.get('vip_name'),
        ) """
        vip.vip=vip.vip.upper()
        vip.save()
        #return redirect('vip:home')

    context = {'vips': vips}
    return render(request, 'vip_ref/vip_entry.html', context)



def createHOD(request):
    
    hods = HOD.objects.all()
    if request.method == 'POST':

        hod_name = request.POST.get('hod_name')
        hod, created = HOD.objects.get_or_create(hod=hod_name)

        """ VIP.objects.create(
            
            vip=request.POST.get('vip_name'),
        ) """
        hod.hod=hod.hod.upper()
        hod.save()
        #return redirect('vip:home')

    context = {'hods': hods}
    return render(request, 'vip_ref/hod_entry.html', context)


def vip_to_excel(request):
    vips= Reference.objects.select_related('vip').prefetch_related('hod','hod_reply').all()


    # Get all field names from the Reference model
    vip_fields = [field.name for field in Reference._meta.fields]
    
    # Initialize a list to hold the data
    data = []
    
    for vip in vips:
        # Get the vip's data
        vip_data = {field: getattr(vip, field) for field in vip_fields}
        #vigilance_data['complainant_name'] = vigilance.vigilance_complainant.name # fecth the name of Foreign key but notneeded 
             
                
        vip_data['to_HOD'] = ', '.join(v.hod for v in vip.hod.all()) # join many to many field object
        vip_data['from_HOD'] = ', '.join(v.hod for v in vip.hod_reply.all())
        
                
        data.append(vip_data)
        
    
    # Convert the list of dictionaries to a pandas DataFrame
    df = pd.DataFrame(data)
    
       
    for col in df.select_dtypes(include=['datetime64[ns, UTC]']).columns:
        df[col] = df[col].dt.tz_convert(None)

    # Create an Excel writer object
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=VIP_Details.xlsx'
    
    # Write the DataFrame to the response
    df.to_excel(response, index=False)
    
    return response
