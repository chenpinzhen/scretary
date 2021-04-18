# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 17:48:42 2021

@author: 陳品蓁
"""



import twstock
stock = twstock.Stock('2330')
stock


print('high', stock.date[-5:])    
print('price', stock.price[-5:])  
print('high', stock.high[-5:])    


