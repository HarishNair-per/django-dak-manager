from django import forms
from . models import  Furniture

#class DateInput(forms.DateInput):
#    input_type = 'date'

class AddAssetForm(forms.ModelForm):
    class Meta:
        model= Furniture
        fields = '__all__'

        labels = {

            'furniture_type': 'Type',
            'furniture_qty': 'Quantity',
            'furniture_dt_receipt': 'Date of Receipt',
            'furniture_make': 'Make',
            'furniture_model': 'Model',
            'furniture_serial': 'Serial Number',
            'furniture_room': 'Room',
            'furniture_image': 'Image',

            'furniture_remarks': 'Remarks',
        }

        widgets = {
            'furniture_dt_receipt': forms.widgets.DateInput(attrs={'type': 'date'}),
            
            
        }