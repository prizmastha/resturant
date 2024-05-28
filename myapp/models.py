from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

# Create your models here.


class Menu(models.Model):
    name=models.CharField(max_length=20)
    price=models.IntegerField()
    def __str__(self):
        return self.name
    
    
class Inventory(models.Model):
    item_name=models.CharField(max_length=20)
    qty=models.IntegerField()
    unit_price=models.IntegerField()
    def __str__(self):
        return self.item_name
    

class Recipe(models.Model):
    name=models.ForeignKey(Menu, on_delete=models.CASCADE)
    name_of_ingridients=models.ForeignKey(Inventory, related_name='ingredient_recipes', on_delete=models.CASCADE)
    # price_of_ingridients=models.ForeignKey(Inventory, related_name='price_recipes', on_delete=models.CASCADE)  
    qty_in_recipe=models.IntegerField()

    def __str__(self):
        return f" {self.name}"
    

class Order(models.Model):
    order_item=models.ForeignKey(Menu, on_delete=models.CASCADE)
    qty_of_order=models.IntegerField()
    table_number=models.IntegerField()
    def __str__(self):
        return f"Order {self.id} - Table { self.table_number}"
    
   
    
# class UserManager(BaseUserManager):
#     def create_user(
#         self, email, password=None, is_staff=False, is_active=True, **extra_fields
#     ):
#         """Create a user instance with the given email and password."""
#         email = UserManager.normalize_email(email)
#         # Google OAuth2 backend send unnecessary username field
#         extra_fields.pop("username", None)

#         user = self.model(
#             email=email, is_active=is_active, is_staff=is_staff, **extra_fields
#         )
#         if password:
#             user.set_password(password)
#         user.save()
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         user = self.create_user(
#             email, password, is_staff=True, is_superuser=True, **extra_fields
#         )
#         return user


# class User(AbstractUser):
#     name=models.CharField(max_length=100, blank=True)
#     email=models.EmailField(unique=True)
#     role=models.CharField(max_length=50)
#     is_staff=models.BooleanField(default=True)


