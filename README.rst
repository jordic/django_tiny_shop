Django Tiny Shop
==========================

Super simple and small Django Cart/shop. 
Author: Jordi Collell <jordic@gmail.com>


FEATURES
================

- Decoupled:
	. Client, order, payment, product, shipping are modules, that you can/must overwrite, 
	from your shop specs and local enviroment.
	. Payment works using django_paypal
		See <http://webcloud.se/log/Implementing-PayPal-in-Django/> for implementing it
		

- What's provided
	. Simple client modules, with contact address.
	. Simple product module, with inline variations, no stock.
	. Simple shipping modules with correos from spain.
	. Only sells to spain
	. Templates: A set of basic templates are provided, but you must overwrite them.
	. Simple set of templatetags, to work with. Using django_templatetags_sugar, you

- Features plan (Not implemented)
	- Adding signals to improve shop personalitzation
	- Better shipping module
	- Adding more shippings modules		

TRY
=============

1. Create a virtualenv
2. Install requirements.txt
	pip install -r requirements.txt
3. Sync your db
	./manage.py syncdb
	
4. launch demo site:
	./manage.py runserver
	
5. Browse your shop
	http://localhost:8000/admin
	
	User: Demo 
	Pass: demo


BASIC SHOP SETTINGS
====================
Look at demo/settings.py are full documented










