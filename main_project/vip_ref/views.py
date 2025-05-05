import os
import pandas as pd
import mammoth 
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Reference, HOD, VIP
from .forms import AddDataForm
from django.conf import settings

# Create your views here.


def vip_home(request):
    
    return render(request, 'vip_ref/viphome.html')


def home(request):
    data= Reference.objects.all()
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
        vip.vip=vip.vip.title()
        vip.save()
        #return redirect('vip:home')

    context = {'vips': vips}
    return render(request, 'vip_ref/vip_entry.html', context)
