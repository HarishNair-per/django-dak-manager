
from django.shortcuts import render,redirect, get_object_or_404

import os

#from django.contrib.staticfiles import finders

from django.template.loader import get_template
from xhtml2pdf import pisa

from django.http import HttpResponse
from .models import Furniture, AssetDesc
from .forms import AddAssetForm

# Create your views here.


# pdf generation code

def render_pdf_view(request, *args, **kwargs):
    data= Furniture.objects.all()
    template_path = 'furniture/asset_home_pdf.html'
    context = {'data': data}

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
    data = Furniture.objects.all()
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