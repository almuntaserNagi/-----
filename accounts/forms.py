from django import forms
from mirror.models  import *


class ExhibitionDetailsForm(forms.ModelForm):
    class Meta:
        model   = Exhibition
        fields = ['name','record_number','location']

class CustomerDetailsForm(forms.ModelForm):
    class Meta:
        model   = Customer
        fields = ['full_name','identifyNo','place_Birth']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'
