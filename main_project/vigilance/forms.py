# forms.py
from django import forms
from .models import Complainant, Vigilance

class ComplainantForm(forms.ModelForm):
    class Meta:
        model = Complainant
        fields = ['name', 'address', 'mobile']

        
        widgets = {
            'name': forms.TextInput(attrs={'list': 'names', 'id': 'id_name'}), # list: names--> shoud match with html datalist id=names
            'address': forms.Textarea(attrs={'id': 'id_address', 'rows': 3, 'cols': 40}),
            'mobile': forms.TextInput(attrs={'id': 'id_mobile'}),
        }


class AddVigDataForm(forms.ModelForm):
    class Meta:
        model= Vigilance
        fields = '__all__'
        

        labels = {
            'vigilance_ref_no' : 'Refeence No',
            'vigilance_dt': 'Reference Date',
            'vigilance_eoffice': 'Eoffice No',
            'vigilance_subject': 'Subject (Short)',
            'vigilance_complainant': 'Complainant',
            
            'vigilance_contents': 'Subject (Long)',
            'vigilance_inward_dt': 'Inward Date',
                   
            'vigilance_outward_ref': 'Outward Reference',
            'vigilance_outward_dt': 'Outward Date',

            'vigilance_subject_file': 'Subject File' ,
            'vigilance_reply_file': 'Reply File' ,
            'vigilance_pending': 'Status (Pending/Partial/Replied)',
            'vigilance_hod': 'to HODs',
            'vigilance_hod_reply': 'from HODs',
            'vigilance_remarks' : 'Remarks',
        }
        widgets = {
            'vigilance_dt': forms.widgets.DateInput(attrs={'type': 'date'}),
            "vigilance_inward_dt": forms.widgets.DateInput(attrs={'type': 'date'}),
            "vigilance_outward_dt": forms.widgets.DateInput(attrs={'type': 'date'}),
            
            #"vigilance_hod_reply": forms.widgets.TextInput(attrs={'type': 'text'}, label='from HODs'),
            
        }
