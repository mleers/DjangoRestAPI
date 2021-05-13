from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(default= 0.00, max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=False)

    def __str__(self):
        return self.name