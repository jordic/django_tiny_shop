#!/usr/bin/env python

# This will effectively place satchmo files but there needs to
# be extra work before this would work correctly
import tshop
from setuptools import setup, find_packages

# Dynamically calculate the version based on django.VERSION.
version = __import__('tshop').__version__
#packages = find_packages('tshop')

setup(name = "django-tiny-shop",
      version = tshop.__version__,
      author = "Jordi Collell",
      author_email = "jordic@gmail.com",
      url = "http://github.com/jordic/django_tshop",
      license = "BSD",
      description = "Django Tiny Shop",
      long_description = "Very simple shop system",
      include_package_data = True,
      zip_safe = False,
      packages = find_packages('tshop'),
      package_dir = {
        '' : 'tshop',
        },
      classifiers = [
      'Development Status :: 3 - Alpha',
      'License :: OSI Approved :: BSD License',
      'Operating System :: OS Independent', 
      'Topic :: Office/Business',
      ]
)
