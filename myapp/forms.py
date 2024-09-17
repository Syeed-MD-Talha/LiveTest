from .models import contact_model
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = contact_model
        fields = '__all__'                           