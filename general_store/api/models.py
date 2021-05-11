from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=200)
    in_stock = models.BooleanField(default=False)

    def __str__(self):
        return self.name