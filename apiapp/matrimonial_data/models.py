from django.db import models

# Create your models here.
class Ghar(models.Model):
    id = models.CharField(max_length=20,primary_key=True,blank=False,null=False)
    image = models.URLField(null=True)
    price = models.CharField(max_length=20,null=True)
    name = models.TextField(default="")
    # latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    # longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)

   
