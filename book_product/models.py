from django.db import models

# Create your models here.
class add_product(models.Model):
    product_name= models.CharField(max_length=30)
    product_price= models.DecimalField(max_digits=6, decimal_places=2)
    tittle= models.CharField(max_length=50)
    image= models.ImageField(upload_to="pics/products/")