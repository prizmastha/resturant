from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView,View,CreateView,UpdateView,DeleteView
from .models import Menu,Inventory,Order,Recipe
from myapp.formofmenu import MenuForm
from myapp.formofinventory import InventoryForm
from myapp.formsoforder import OrderForm
from myapp.formsofrecipe import RecipeForm


# Create your views here.


class Base(View):
    def get(self, request, *args, **kwargs):
        return render(request,'resturant/base.html')

      
      
      
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
    
    
    
      
class OrderList(ListView):
    model=Order
    context_object_name="order"
    template_name="resturant/order_list.html"
    
    
     
class OrderCreate(CreateView):
    model=Order
    form_class=OrderForm
    template_name="resturant/order_form.html"
    success_url=reverse_lazy('myapp:indexoforder')
    
    


class OrderDeleteView(DeleteView):
    model=Order
    success_url=reverse_lazy('myapp:indexoforder')

    
class RecipeList(ListView):
    model=Recipe
    context_object_name="recipe"
    template_name="resturant/recipe_list.html"
    
    
    
class RecipeCreate(CreateView):
    model=Recipe
    form_class=RecipeForm
    template_name="resturant/recipe_form.html"
    success_url=reverse_lazy('myapp:indexofrecipe')
    
    