from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse

import requests
from bs4 import BeautifulSoup

# Create your views here.
class GetProducts(View):
	def get(self, request):
		products = requests.get("http://als18.dnsalias.com/oll/als_get_products.cgi")
		soup = BeautifulSoup(products.text)
		products = soup.findAll('row')
		create_file = open('als/fixtures.json', 'w+')
		json = {}
		for product in products:
			product_code = product.attrs['code']
			product_short_name = product.attrs['productshortname']
			product_name = product.attrs['productname']

		return HttpResponse('Hello world!')
