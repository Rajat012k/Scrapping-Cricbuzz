#ALL REQUIRED IMPORTS
import requests
import bs4

#URL OF THE SITES NEEDED TO BE SCRAPPED
url1="https://www.sulekha.com/yoinab-it-services-chhijarsi-colony-noida-contact-address#bizreviews"
url2="https://dir.indiamart.com/impcat/babool-wood.html"
url3="https://www.justdial.com/Mumbai/Natures-Bazzaar-Opposite-Parwana-Tower-Ram-Nagar-Borivali-West/022PXX22-XX22-190516114051-T5Q8_BZDET?xid=TXVtYmFpIEdyb2NlcnkgU3RvcmVz"

#DATASET RECEIVED
dataset1=requests.get(url1)
dataset2=requests.get(url2)
dataset3=requests.get(url3)

#SOUPS
soup1=bs4.BeautifulSoup(dataset1.content,'html.parser')
soup2=bs4.BeautifulSoup(dataset2.content,'html.parser')
soup3=bs4.BeautifulSoup(dataset3.content,'html.parser')

### USE THIS WHEN YOU WANT TO CREATE A FILE -----------------####

# with open ('data.txt','w') as f:
#     for div in soup1.find_all('div',{'class':'details'}):
#         f.write(div.text)
#         f.write("\n")
#     for div in soup2.find_all('div',{'class':'rht pnt'}):
#         f.write(div.text)
#         f.write("\n")
#       for div in soup3.find_all('div',{'class':'col-sm-12 allratingM'}):
#         print(div.text)
