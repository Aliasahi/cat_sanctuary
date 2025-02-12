from django import forms
from .models import CareRecord

class CareRecordForm(forms.ModelForm):
    class Meta:
        model = CareRecord
        fields = ['cat', 'caretaker', 'date', 'notes']

    def clean_notes(self):
        notes = self.cleaned_data.get('notes')
        if len(notes) < 5:
            raise forms.ValidationError("Notes must be at least 5 characters long.")
        return notes
