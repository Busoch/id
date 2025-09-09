from django import forms
from .models import FoundID, LostIDReport

class FoundIDForm(forms.ModelForm):
    class Meta:
        model = FoundID
        fields = ['name_on_id', 'location_found', 'date_found', 'image', 'contact']
        widgets = {
            'date_found': forms.DateInput(attrs={'type': 'date'}),
        }

class LostIDReportForm(forms.ModelForm):
    class Meta:
        model = LostIDReport
        fields = ['name', 'id_number', 'last_seen_location', 'contact_info']
