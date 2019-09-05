from django.db import models

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=120)
    description = models.TextField(blank=True,null=True)
    price       = models.DecimalField(decimal_places=2,max_digits=100)
    summery     = models.TextField(blank=False,null=True)
     #Blank is for field(how field is rendered) but Null is for DB col
    featured    = models.BooleanField(default=False)
