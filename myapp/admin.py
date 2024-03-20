from django.contrib import admin

from .models import Menu,Inventory,Recipe,Order

# Register your models here.



admin.site.register(Menu)
admin.site.register(Inventory)
admin.site.register(Recipe)
admin.site.register(Order)

