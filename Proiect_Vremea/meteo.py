import sys
from datetime import datetime
from urllib import request
import requests
from tkinter import *
import cv2 

root =Tk()
root.geometry("600x600") 
root.title("Meteo App")
root.resizable(False,False) 
root.config(background="#531CB3")

city_value = StringVar()

def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()

def showWeather():
    API_KEY = "fb7a035d54daf544f2f708b83c60be43"
    city_name=city_value.get()
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    
   # city = input("Introduceti numele orasului: ")
    request_url = f"{BASE_URL}?appid={API_KEY}&q={city_name}&units=metric"
    response = requests.get(request_url)
    txtfield.delete("1.0", "end") #to clear the text field for every new output

    if response.status_code == 200:
        data = response.json() 
        date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
        vreme = data['weather'][0]['description']        
        temperatura = round(data['main']['temp'],2)
        vant = data['wind']['speed']
        umiditate = round(data['main']['humidity'],2)
        presiune = data['main'] ['pressure']
        vizibilitate = data['visibility']
        timezone = data['timezone']
        rasarit = data['sys']['sunrise']
        apus = data['sys']['sunset']
        rasarit = time_format_for_location(rasarit + timezone)
        apus = time_format_for_location(apus + timezone) 
       
        data = f"\n Vremea in: {city_name}\n Data si ora: {date_time}\n Soarele rasare la: {rasarit}\n Apune la: {apus}\n Vremea: {vreme}\n Temperatura acum: {temperatura} °C\n Vant {vant} m/s\n Umiditate: {umiditate} %\n Presiune atmosferica: {presiune} hPa\n Vizibilitate:{vizibilitate}"" m" 
    
    else:
        data = f"\n Vremea  pentru orasul {city_name} nu a fost gasita!\n Va rugam introduceti un oras valid!!!"
        
    txtfield.insert(INSERT, data) #to insert or send value in our Text Field to display output
           

city_label= Label(root, text = 'Introduceti orasul:', font = 'Cambria 14 bold').pack(pady=20) 
 
input_city = Entry(root, textvariable = city_value,  width = 25, font='Cambria 14 bold').pack()
 
 
btn=Button(root, command = showWeather, text = "Vezi vremea", font='Cambria 12 bold' , bg='#d100d1', activebackground="#e500a4",fg='white', padx=5, pady=5 ).pack(pady= 20)
 
#to show output
 
vremea_acum = Label(root, text = "Vremea acum: ", font = 'Cambria 14 bold').pack(pady=20)

txtfield = Text(root, bg="white", font = 'Cambria 14 bold', fg="black",  width=40, height=15)
txtfield.pack()
txtfield.focus() 

root.mainloop()
 
