from django.core.management.base import BaseCommand, CommandError

from bs4 import BeautifulSoup
import requests

from als.models import Product

class Command(BaseCommand):
	def handle(self, *args, **options):
		products = requests.get("als url")
		if products.status_code == 200:
			soup = BeautifulSoup(products.text)
			product_lists = soup.findAll('row')
			created = False
			for product in product_lists:
				product_code = product.attrs['code']
				product_short_name = product.attrs['productshortname']
				product_name = product.attrs['productname']
				try:
					Product.objects.create(product_code=product_code, product_name=product_name, product_short_name=product_short_name)
					created = True
				except:
					pass
			if created:
				self.stdout.write('Successfully updated the products.')
			else:
				self.stdout.write('Nothing to update.')
		else:
			self.stdout.write('There is a problem with API.')