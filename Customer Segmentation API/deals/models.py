from django.db import models

# Create your models here.
class Deals(models.Model):
    deal_id = models.AutoField(primary_key=True)
    deal_name = models.CharField(max_length=100)
    discount = models.IntegerField()
    category = models.CharField(max_length=50)
    discount_price = models.IntegerField()
    product_name = models.CharField(max_length=50,default=None)
    original_price = models.IntegerField()

    
    class Meta:
       db_table = "deals"
