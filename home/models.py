from django.db import models

# Create your models here.



class Collection(models.Model):
    collection_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.collection_name



class Item(models.Model):
    item_name = models.CharField(max_length=100)
    item_price = models.IntegerField()
    item_price_offer = models.IntegerField()
    item_desc = models.TextField()
    item_image = models.ImageField(upload_to = 'items', null=True)

    collection_id= models.ForeignKey(Collection, on_delete=models.CASCADE)
 
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item_name
    

class CartItem(models.Model):
    product = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    user_session = models.CharField(max_length=32)
    