from django import forms
from myapp.models import Recipe, Menu, Inventory

class RecipeForm(forms.ModelForm):
    def __init__(self,  **kwargs):
        super(RecipeForm, self).__init__( **kwargs)
       
    class Meta:
        model = Recipe
        fields = ['name', 'name_of_ingridients','qty_in_recipe']
        widgets = {
                    'qty_in_recipe':forms.TextInput(),

        }

    # Override the order_item field
    name = forms.ModelChoiceField(queryset=Menu.objects.all(), widget=forms.Select)
    name_of_ingridients = forms.ModelChoiceField(queryset=Inventory.objects.all(), widget=forms.Select)
