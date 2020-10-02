from django import forms
from contacts.models import Contact


class ContactCardForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ['user']
