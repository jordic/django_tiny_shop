#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: jordi collell <jordi@tempointeractiu.cat>
# http://tempointeractiu.cat
# -------------------------------------------------------------------
'''
'''


from django.db import models
from django.db import connection


class StatsManager(models.Manager):


    def total(self, s, e):
        query = '''SELECT sum(b.total), sum(b.total)
        FROM order_order as a 
            LEFT JOIN order_line as b on a.id = b.order_id
            WHERE status IN ('pendiente', 'enviado')
            AND a.date BETWEEN %s AND %s'''

        cursor = connection.cursor()
        cursor.execute(query, [s, e])
        res = cursor.fetchall()
        return res


    def facturas_dia(self, start, e):
        query = '''SELECT a.date as data, 
                   sum(b.total)
            FROM order_order as a 
            LEFT JOIN   order_line as b on a.id = b.order_id
            WHERE a.status IN ('pendiente', 'enviado') 
            AND  a.date BETWEEN %s AND %s
            GROUP BY YEAR(a.date), MONTH(a.date), DAY(a.date) '''

        cursor = connection.cursor()
        cursor.execute(query, [start, e])
        res = cursor.fetchall()
        return res

    def pedidos_dia(self, s, e):
        query = '''SELECT a.date as data, count(a.id) 
            FROM order_order as a 
            WHERE status IN ('pendiente', 'enviado') 
            AND a.date BETWEEN %s AND %s
            GROUP BY YEAR(a.date), MONTH(a.date), DAY(a.date)'''
        cursor = connection.cursor()
        cursor.execute(query, [s, e])
        res = cursor.fetchall()
        return res

    def rendiment_producte(self, s, e):
        query = '''SELECT sum(b.quantity) as num, c.title_es, sum(b.total)  
            FROM order_order as a 
                LEFT JOIN order_line as b on a.id = b.order_id
                LEFT JOIN product_product as c on b.product_id = c.id
            WHERE status IN ('pendiente', 'enviado') 
            AND b.types = 'product'
            AND a.date BETWEEN %s AND %s
            GROUP BY b.product_id'''
        cursor = connection.cursor()
        cursor.execute(query, [s, e])
        res = cursor.fetchall()
        return res

    def productes_per_dia(self, s, e):
        query = '''SELECT a.date as data, a.id, 
            sum(b.total), count(a.id), c.title_es
            FROM order_order as a 
                LEFT JOIN order_line as b on a.id = b.order_id
                LEFT JOIN product_product as c on b.product_id = c.id
            WHERE status IN ('pendiente', 'enviado')
            AND b.types = 'product'
            AND a.date BETWEEN %s AND %s
            GROUP BY YEAR(a.date), MONTH(a.date), DAY(a.date), b.product_id'''
        cursor = connection.cursor()
        cursor.execute(query, [s, e])
        res = cursor.fetchall()
        return res

