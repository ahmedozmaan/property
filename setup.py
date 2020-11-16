# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in property/__init__.py
from property import __version__ as version

setup(
	name='property',
	version=version,
	description='Property Management System',
	author='Ahmed Osman',
	author_email='ahmedozmaan@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
