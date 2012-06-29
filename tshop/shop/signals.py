#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# ^ la línia superior serveix per poder posar accents a l'arxiu
# Autor: jordi collell <jordi@tempointeractiu.cat>
# http://tempointeractiu.cat
# -------------------------------------------------------------------
""" 

"""


from django.dispatch import Signal


# A new user has registered.
checkout_form_created = Signal(providing_args=["form"])

# postal code clean
clean_postal_code = Signal(providing_args=["postal"])

# extra checkout form validation data
clean_checkout_form = Signal(providing_args=["data"])

# Create an order
order_created = Signal(providing_args=["order", "client", "amount"])

# Cart list 
# used for altering cart listing based on external modules/api
cart_list_created = Signal(providing_args=["list"])