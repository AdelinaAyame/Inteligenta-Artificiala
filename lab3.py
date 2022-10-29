from http import server
from haslib import new
import requests
from bs4 import BeautifulSoup
import smtplib

def trimitere_email():
    server = starttls()
    server.login("data_scraping@adelina.ro", "stiinte216_2022")
    server.sendmail("data_scraping@adelina.ro", "EMAILUL_TAU_AICI", "Subject: Pretul a scazut\n\nPretul a scazut la 1000 lei")
    print("Email trimis")
    server.quit()

def data_scraping():
    req = requests.get("https://www.emag.ro/telefon-mobil-apple-iphone-14-pro-max-256gb-5g-space-black-mq9u3rx-a/pd/D9DY4LMBM/?ref=fam#256-GB")
    soup = BeautifulSoup(req.text, 'html.parser')
    price = soup.find('p', attrs={'class':'product-new-price'}).text
    new_price=price[0:5]
    new_price=new_price.replace(".","")
    new_price=int(new_price)
    if(new_price<7799):
        trimitere_email()
        print("Avem o modificare de pret!!!")
    else:
        print("Pretul nu a scazut")