from django.db import models

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
    price_of_ingridients=models.ForeignKey(Inventory, related_name='price_recipes', on_delete=models.CASCADE)  
    def __str__(self):
        return self.name
    

class Order(models.Model):
    order_item=models.ForeignKey(Menu, on_delete=models.CASCADE)
    qty=models.IntegerField()
    table_number=models.IntegerField()
    def __str__(self):
        return f"Order {self.id} - Table {self.table_number}"
   
    
    



