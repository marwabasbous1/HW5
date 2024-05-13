# forms.py
from itertools import product

from django.forms import forms

class ProductForm(forms.ModelForm):
    class Meta:
        model = product
        fields = '__all__'
