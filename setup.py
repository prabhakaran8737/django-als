import os
from setuptools import setup, find_packages

def read_me(file_name):
	return open(os.path.join(os.path.dirname(__file__), file_name)).read()

setup(
	name='django-als',
	version='1.0.0',
	description='API calls',
	long_description=read_me('README.rst'),
	url='',
	download_url='',
	author='Prabhakaran',
	install_requires=['Django >= 1.7',
					  'requests >= 2.5.1'],
	include_package_data=True,
	classifiers=[
		'Development Status :: Development',
		'Environment :: Web Environment',
		'Framework :: Django'
	]
)