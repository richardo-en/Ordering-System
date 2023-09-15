from django import forms
from .models import OverallOrder

class OverallOrderForm(forms.ModelForm):
    class Meta:
        model = OverallOrder
        fields = ['order_type', 'name','goods', 'mobile_phone', 'note']
