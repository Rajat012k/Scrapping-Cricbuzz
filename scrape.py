print("Scrapping Using Python")
import requests
from bs4 import BeautifulSoup
import urllib.request

# site to be scrapped

Site=requests.get("https://www.cricbuzz.com/")
# Using BS to parse the html code and javascript
soup = BeautifulSoup(Site.content, 'html.parser')
# Fetching that random div using find
# You can check various other function according to ur scraaping need like findAll()
mydiv = soup.find("div", {"class": "cb-col cb-col-25 cb-mtch-blk"})

# Printing the text under that div only
print(mydiv.text)
