# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 20:53:40 2021

@author: nolyn
"""

# =============================================================================
# Scrape JSON data for Stephen Curry of the Golden State Warriors NBA team for the 2015–16 
# year from this web page:
# o http://buckets.peterbeshai.com/app/#/playerView/201939_2015
#  The JSON data structure can be observed in the Network item listed as 
# ?player=201939&season=2015 in Google Chrome’s Developer Tools.
#  Write Python code, in a file entitled json_scrape.py, to retrieve the JSON data for this 
# Network item, and print these items, making computations that are necessary:
# o Your W&M username (this doesn’t come from the web page)
# o Number of shots categorized exactly as “Jump Shot”
# o The number of those jump shots that were made; that is, those shots classified as a 
# “Made Shot”
# o The percentage of the attempted “Jump Shots” that were classified as a “Made Shot” 
#  Write your Python code so that it prints out only the results for the three computations 
# mentioned in the bullet points above without any other text. 
#  Use the template provided to write your code, which is entitled json_scrape.py. Submit 
# your code in a file with this same filename
# =============================================================================


import requests

my_wm_username = 'nsdandridge'
search_url = 'https://buckets.peterbeshai.com/api/?player=201939&season=2015'
response = requests.get(search_url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}) 

# Write your program here to populate the appropriate variables

root = response.json()
shots = root

numJumpShotsAttempt = 0
numJumpShotsMade = 0
percJumpShotMade = 0.0

for shot in shots:
    for k, v in shot.items():
        if v == 'Jump Shot':
            numJumpShotsAttempt += 1


for shot in shots:
    for k, v in shot.items():
        if v == 'Jump Shot':
            for j, w in shot.items():
                if j == 'SHOT_MADE_FLAG':
                    numJumpShotsMade += w


percJumpShotMade = round(numJumpShotsMade/numJumpShotsAttempt * 100, 1)
            
           
            
print(my_wm_username)
print(numJumpShotsAttempt)
print(numJumpShotsMade)
print(percJumpShotMade)