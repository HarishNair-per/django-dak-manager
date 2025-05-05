#from bootstrap_datepicker_plus.widgets import DatePickerInput
from django import forms
from . models import  HOD, Reference, VIP

#class DateInput(forms.DateInput):
#    input_type = 'date'

class AddDataForm(forms.ModelForm):
    class Meta:
        model= Reference
        fields = '__all__'
        widgets = {
            'reference_dt': forms.widgets.DateInput(attrs={'type': 'date'}),
            "inward_dt": forms.widgets.DateInput(attrs={'type': 'date'}),
            "outward_dt": forms.widgets.DateInput(attrs={'type': 'date'}),
            
        }