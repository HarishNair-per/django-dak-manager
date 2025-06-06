
from django.shortcuts import render,redirect, get_object_or_404

import os

#from django.contrib.staticfiles import finders

from django.template.loader import get_template, render_to_string # weasy render_to_string
from xhtml2pdf import pisa

from django.http import HttpResponse
from .models import Furniture, AssetDesc
from .forms import AddAssetForm
from datetime import datetime

from django.db.models import Sum 


#weasy
""" from weasyprint import HTML
import tempfile
from django.conf import settings
from urllib.parse import urljoin
from pathlib import Path """


# Create your views here.



def summarize(request):
    furniture= Furniture.objects.all()
    sum_fur= Furniture.objects.values('furniture_type__asset_name').annotate(Sum('furniture_qty')) # directly took name foreignkey
    sum_fur_room= Furniture.objects.values('furniture_room','furniture_type__asset_name').annotate(Sum('furniture_qty')).order_by('furniture_room')
    sum_fur_fur= Furniture.objects.values('furniture_type__asset_name','furniture_room').annotate(Sum('furniture_qty')).order_by('furniture_type')
    print(sum_fur)
    print()
    print(sum_fur_room)
    print()
    print(sum_fur_fur)
    date_now= datetime.now()

    #manually create display objects

    room_choices_dict = dict(Furniture.room_choices)

    for item in sum_fur_room:
        item['furniture_room_display'] = room_choices_dict.get(item['furniture_room'], item['furniture_room'])
    
    for item in sum_fur_fur:
        item['furniture_room_display'] = room_choices_dict.get(item['furniture_room'], item['furniture_room'])

    context= {"data": sum_fur, 'rooms': sum_fur_room,'by_fur': sum_fur_fur, 'date_now':date_now, 'furnitures': furniture}
    return render (request, 'furniture/asset_summary.html', context)

# pdf generation code
def render_pdf_view(request):
    data= Furniture.objects.all()
    date_now= datetime.now()
    template_path = 'furniture/asset_home_pdf.html'
    context = {'data': data, 'date_now':date_now}

    # Create a Django response object, and set content type to PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="assets.pdf"'
    #response['Content-Disposition'] = 'attachment; filename="assets.pdf"'

    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html,
       dest=response
    )

    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')

    return response
# end pdf gen.

def fur_home(request):
    data = Furniture.objects.select_related('furniture_type').all()
    
    context= {'data':data}
    return render (request, 'furniture/asset_home.html', context)


def fur_add(request):
    if request.method== "POST":
        form= AddAssetForm(request.POST, request.FILES)
        
        if form.is_valid():
            
            form.save()
            return redirect('fur:fur_home')
    context= {'form' : AddAssetForm()}

    return render(request, 'furniture/asset_add.html', context)


def fur_update(request,pk):
    ref = get_object_or_404(Furniture,id=pk)
    form = AddAssetForm(request.POST or None, request.FILES or None, instance=ref)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('fur:fur_home')
    context = {
        'form': form,
        }
    return render(request, 'furniture/asset_update.html', context)


def createAsset(request):
    
    assets = AssetDesc.objects.all()
    if request.method == 'POST':

        asset_name = request.POST.get('asset_name')
        asset, created = AssetDesc.objects.get_or_create(asset_name=asset_name)

        """ VIP.objects.create(
            
            vip=request.POST.get('vip_name'),
        ) """
        asset.asset_name=asset.asset_name.title()
        asset.save()
        #return redirect('vip:home')

    context = {'assets': assets}
    return render(request, 'furniture/asset_entry.html', context)