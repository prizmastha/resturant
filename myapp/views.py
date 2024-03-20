from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView,View,CreateView,UpdateView
from .models import Menu,Inventory
from myapp.formofmenu import MenuForm
from myapp.formofinventory import InventoryForm



# Create your views here.


      
class MenuList(ListView):
    model=Menu
    context_object_name="menu"
    template_name="resturant/menu_list.html"
    


class MenuCreate(CreateView):
    model=Menu
    form_class=MenuForm
    template_name="resturant/menu_form.html"
    success_url=reverse_lazy('myapp:indexofmenu')

    
    
class InventoryList(ListView):
    model=Inventory
    context_object_name="inventory"
    template_name="resturant/inventory_list.html"
    

class InventoryCreate(CreateView):
    model=Inventory
    form_class=InventoryForm
    template_name="resturant/inventory_form.html"
    success_url=reverse_lazy('myapp:indexofinventory')



class InventoryUpdateView(UpdateView):
    model=Inventory
    form_class=InventoryForm
    template_name="resturant/inventory_form.html"
    success_url=reverse_lazy('myapp:indexofinventory')