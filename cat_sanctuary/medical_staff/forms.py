from django import forms
from .models import HealthRecord 

class HealthRecordForm(forms.ModelForm):
    class Meta:
        model = HealthRecord
        fields = ['cat', 'medical_staff', 'date', 'diagnosis', 'treatment']

    def clean_diagnosis(self):
        diagnosis = self.cleaned_data.get('diagnosis')
        if len(diagnosis) < 3:
            raise forms.ValidationError("Diagnosis must be at least 3 characters long.")
        return diagnosis
