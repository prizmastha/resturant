from django import forms
from myapp.models import Order, Menu

class OrderForm(forms.ModelForm):
    def __init__(self,  **kwargs):
        super(OrderForm, self).__init__( **kwargs)
        # Set initial value for order_item
        default_menu_item = Menu.objects.first()  # Get the first menu item
        if default_menu_item:
            self.fields['order_item'].initial = default_menu_item

    class Meta:
        model = Order
        fields = ['order_item', 'qty', 'table_number']
        widgets = {
            'qty': forms.TextInput(),
            'table_number': forms.TextInput(),
        }

    # Override the order_item field
    order_item = forms.ModelChoiceField(queryset=Menu.objects.all(), widget=forms.Select)
