import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url='https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'


#Opening connection and grabing the page
uClient=uReq(my_url)
page_html=uClient.read()
uClient.close()
# html parser
page_soup=soup(page_html, "html.parser")

#Grabs each product
containers=page_soup.findAll("div",{"class":"item-container"})

filename="product.csv"
f=open(filename,"w")
headers="brand, product_name, shipping\n"

f.write(headers)


for container in containers:
    brand=container.div.div.a.img["title"]

    title_container= container.findAll('a',{"class":"item-title"})
    pruduct_name= title_container[0].text

    shipping_container=container.findAll("li",{"class":"price-ship"})
    shipping=shipping_container[0].text.strip()



    f.write(brand+ "," + pruduct_name.replace(", ","|")+ "," + shipping + "\n")
f.close()
