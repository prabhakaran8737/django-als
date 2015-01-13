from django.db import models

class Product(models.Model):
	product_code = models.IntegerField(unique=True, null=True, blank=False, default='')
	product_short_name = models.CharField(max_length=126, null=True, blank=True, default='')
	product_name = models.CharField(max_length=256, null=True, blank=True, default='')
