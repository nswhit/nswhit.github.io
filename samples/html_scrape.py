# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 09:42:28 2021

@author: nolyn
"""



#https://publicinterestlegal.org/county-list/


import requests  # Internet information requests
from bs4 import BeautifulSoup  # Parsing HTML

""" Access URL """
html_path = 'https://publicinterestlegal.org/county-list/'
html_doc = requests.get(html_path).content

""" Parse HTML """
parsed_html = BeautifulSoup(html_doc, 'lxml')

""" Get target rows """
target_rows = parsed_html.find_all('tr')  


""" Create List of Sublists ('td' tags) """
all_counties = []
for row in target_rows:
    new_row = []
    for x in row.find_all('td'):
        new_row.append(x.text)    #x.text.encode("ascii",'ignore')    
    all_counties.append(new_row)
    

""" Set W&M username for output print statement """
my_wm_username = 'nsdandridge'

""" Print Output """
print(my_wm_username)
print(len(all_counties))
print(all_counties)