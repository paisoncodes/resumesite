from django import forms
from .models import Contact

# Create your forms here.


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('full_name', 'email', 'message', 'subject')
