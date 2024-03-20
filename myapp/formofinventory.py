from django import forms
from myapp.models import Inventory


class InventoryForm(forms.ModelForm):
    class Meta:
        model=Inventory
        fields=['item_name','qty','unit_price']
        widgets={
            'item_name':forms.TextInput(),
            'qty':forms.TextInput(),
            'unit_price':forms.TextInput(),
           
        
        
        }
