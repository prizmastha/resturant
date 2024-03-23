
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
app_name="myapp"
urlpatterns = [
    
    path('home/',views.Base.as_view(),name='base'),
    
    path('menulist/',views.MenuList.as_view(), name='indexofmenu'),
    path('menuadd/',views.MenuCreate.as_view(), name='menucreate'),
    
    path('inventorylist/',views.InventoryList.as_view(), name='indexofinventory'),
    path('inventoryadd/',views.InventoryCreate.as_view(), name='inventorycreate'),
    path('<pk>/update/',views.InventoryUpdateView.as_view(), name='inventoryupdate'),
    
    path('orderlist/',views.OrderList.as_view(), name='indexoforder'),
    path('addorder/',views.OrderCreate.as_view(), name='addorder'),
    path('<pk>/delete/',views.OrderDeleteView.as_view(), name='order_delete'),

    path('recipelist/',views.RecipeList.as_view(), name='indexofrecipe'),
    path('addrecipe/',views.RecipeCreate.as_view(), name='addrecipe'),


    path('totalsales/',views.TotalSales.as_view(), name='indexoftotal'),


]  

