from django import forms
from .models import Restaurant
from phonenumber_field.formfields import PhoneNumberField

class RestaurantForm(forms.ModelForm):
    name = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Restaurant name'}))
    url = forms.CharField(label='',required=False,widget=forms.URLInput(attrs={'class':'form-control','placeholder':'Website'}))
    phone_number = PhoneNumberField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Phone'}))
    notes = forms.CharField(label='',required=False, widget=forms.Textarea(attrs={'class': 'form-control','rows':3 ,'placeholder':'Notes'}))

    class Meta:
        model = Restaurant
        fields = ['name','url','phone_number','notes']