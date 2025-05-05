# forms.py
from django import forms
from .models import Complainant

class ComplainantForm(forms.ModelForm):
    class Meta:
        model = Complainant
        fields = ['name', 'address', 'mobile']
        widgets = {
            'name': forms.TextInput(attrs={'list': 'names', 'id': 'id_name'}),
            'address': forms.Textarea(attrs={'id': 'id_address', 'rows': 3, 'cols': 40}),
            'mobile': forms.TextInput(attrs={'id': 'id_mobile'}),
        }
