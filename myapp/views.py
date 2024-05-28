from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView,View,CreateView,UpdateView,DeleteView
from .models import Menu,Inventory,Order,Recipe
from myapp.formofmenu import MenuForm
from myapp.formofinventory import InventoryForm
from myapp.formsoforder import OrderForm
from myapp.formsofrecipe import RecipeForm
from django.db.models import Sum
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm





# Create your views here.


class Base(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        return render(request,'resturant/base.html')

      
      
      
class MenuList(LoginRequiredMixin,ListView):
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
    
    def form_valid(self, form):
        order = form.save(commit=False)
        order.save()
        
        try:
            order_items = Recipe.objects.filter(name=order.order_item)
            
            
            for order_item in order_items:
                qty_used = order.qty_of_order * order_item.qty_in_recipe
                inventory_item = Inventory.objects.get(item_name=order_item.name_of_ingridients.item_name)
                if inventory_item.qty > 0:
                    inventory_item.qty -= qty_used
                    inventory_item.save()
                    
                else:
                    print("no")
        except order_items.DoesNotExist:
            return HttpResponse("orderitem doesnot exists!!!")

        return super().form_valid(form)
       
        

    


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
    
    
class TotalSales(ListView):
    model=Order
    template_name="resturant/total_sales.html"
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Calculate total sales
        total_sales = self.calculate_total_sales()
        context['total_sales'] = total_sales
        
        return context

    def calculate_total_sales(self):
        try:
            # Query the Order table to calculate the total sales
            total_sales = Order.objects.aggregate(total_sales=Sum('qty_of_order'))['total_sales']

            # If total sales is None, set it to 0
            if total_sales is None:
                total_sales = 0
            
            return total_sales
        except Order.DoesNotExist:
            # Handle the case where there are no orders
            return 0
class LoginView(LoginView):
    """
    Display the login form and handle the login action.
    """

    form_class = AuthenticationForm
    authentication_form = None
    template_name = "registration/login.html"
    redirect_authenticated_user = False
    extra_context = None
    

