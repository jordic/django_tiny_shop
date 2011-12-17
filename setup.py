#!/usr/bin/env python

# This will effectively place satchmo files but there needs to
# be extra work before this would work correctly

import ez_setup
ez_setup.use_setuptools()
from setuptools import setup, find_packages
import os, os.path
import sys

DIRNAME = os.path.dirname(__file__)
APPDIR = os.path.join(DIRNAME, 'tiny')
if not APPDIR in sys.path:
    sys.path.insert(0,APPDIR)

# Dynamically calculate the version based on django.VERSION.
version = __import__('tiny.tshop.shop').__version__
packages = find_packages('tiny')

setup(name = "Django Tiny Shop",
      version = version,
      author = "Jordi Collell",
      author_email = "jordic@gmail.com",
      url = "http://github.com/jordic/django_tshop",
      license = "BSD",
      description = "Django Tiny Shop",
      long_description = "Very simple shop system",
      include_package_data = True,
      zip_safe = False,
      package_dir = {
      '' : 'tiny',
      },
      packages = packages,
      classifiers = [
      'Development Status :: 3 - Alpha',
      'License :: OSI Approved :: BSD License',
      'Operating System :: OS Independent', 
      'Topic :: Office/Business',
      ]
)
