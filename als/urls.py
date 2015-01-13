from django.conf.urls import url, patterns, include
from django.utils import importlib

from .views import GetProducts

urlpatterns = patterns(
	'', url('^get-products/', GetProducts.as_view(), name="als_get_products")
	)