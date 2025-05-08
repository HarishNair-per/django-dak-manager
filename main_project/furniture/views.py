from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .models import Furniture, AssetDesc
from .forms import AddAssetForm
# Create your views here.

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