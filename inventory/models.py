from django.db import models
from vendor.models import Vendor

class Product(models.Model):
    vendor = models.ForeignKey(Vendor,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=32)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    description=models.TextField()
    image=models.ImageField(upload_to='images/')
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    stock=models.PositiveIntegerField()
    def __str__(self):
        return self.name
