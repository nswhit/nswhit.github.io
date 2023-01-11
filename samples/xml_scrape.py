# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 09:21:08 2021

@author: nolyn
"""

import requests
from lxml import objectify

''' You may use these variables with your string substitution as you create
    an appropriate URL '''

#Here is where the filter is applied. The number 5 indicates the period from Apr-Aug 2016.
num_periods = '5'
parameter = 'tavg'
state_id = 44     #The state is Virginia, but URL has a 44 which I think means VA.
climate_div = 0
month_num = '08'
year = '2016'

''' Set W&M username for output print statement '''
my_wm_username = 'nsdandridge'

''' Create an appropriate URL string '''

URL_template = 'https://www.ncdc.noaa.gov/cag/statewide/rankings/%s-%s-%s%s/data.xml'
URL = URL_template % (state_id, parameter, year, month_num)
response = requests.get(URL).content


print(my_wm_username)

root = objectify.fromstring(response)

value = root.data.value
mean = root.data.mean
departure = root.data.departure
lowRank = root.data.lowRank
highRank = root.data.highRank


print(value)
print(mean)
print(departure)
print(lowRank)
print(highRank)