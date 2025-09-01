from django.db import models


class BitcoinPrice(models.Model):
    date = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.DecimalField(max_digits=10, decimal_places=2)
