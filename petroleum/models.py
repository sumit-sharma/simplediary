from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=225)
    status = models.BooleanField(default=1)

    def __str__(self):
        return self.name


class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField('date published')

