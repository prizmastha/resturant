
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name="myapp"
urlpatterns = [
    path('menulist/',views.MenuList.as_view(), name='indexofmenu'),
    path('menuadd/',views.MenuCreate.as_view(), name='menucreate'),
    path('inventorylist/',views.InventoryList.as_view(), name='indexofinventory'),
    path('inventoryadd/',views.InventoryCreate.as_view(), name='inventorycreate'),
    path('<pk>/update/',views.InventoryUpdateView.as_view(), name='inventoryupdate'),


]  

