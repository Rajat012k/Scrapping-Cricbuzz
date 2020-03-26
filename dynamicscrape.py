//CODE NOT WORKING //


from bs4 import BeautifulSoup
from selenium import webdriver
chromePath=r"D:\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chromePath)
driver.get("https://bing.com/covid")
bsObj = BeautifulSoup(driver.page_source,'html.parser')
test = bsObj.find("div", {"id": "portal"}).text
print(test)
