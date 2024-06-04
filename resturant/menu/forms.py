from .models import Food, Deliveryi
from django import forms

class MenuForm(forms.ModelForm):
    class Meta:
        model = Deliveryi
        fields = '__all__'

