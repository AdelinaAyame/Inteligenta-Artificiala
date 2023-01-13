
from datetime import datetime
from urllib import request
import requests
from tkinter import *
import tkinter as tk
from tkinter import messagebox

root =tk.Tk()
root.geometry("700x500") 
root.title("Meteo App")
root.resizable(False,False) 
root.config(background="#1789FC")

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

    if response.status_code == 200:
        data = response.json() 
       # date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
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
       
        #lable_ora.configure(text=str(date_time))
        lable_vremea.configure(text=vreme)
        lable_temperatura.configure(text=str(temperatura)+" C")
        lable_vant.configure(text=str(vant)+" m/s")
        lable_umiditate.configure(text=str(umiditate)+"%")
        lable_presiune.configure(text=str(presiune)+" hPa")
        lable_vizibilitate.configure(text=str(vizibilitate)+" m")
        lable_rasarit.configure(text=str(rasarit))
        lable_apus.configure(text=str(apus))
    else:
        messagebox.showwarning("Eroare","Orasul nu a fost gasit!")

search_bar = Entry(root,font=("cambria",16, "bold"),bg='white',textvariable=city_value,width=20)
search_bar.place(x=130,y=115)

oras = Label(root,text="Introduceti orasul",anchor='n' ,width = 16,font=("cambria",14),bg='#0F7173',fg='white',borderwidth=2,relief="raise")
oras.place(x=170,y=50)

lable_v= Label(root,text="Vremea",width = 10,font=("arial",14),fg='white',bg='#7E1F86',borderwidth=3,relief="raised")
lable_v.place(x=30,y=250)

lable_t = Label(root,text="Temperatura",width = 10,font=("arial",14),fg='white',bg='#7E1F86',borderwidth=3,relief="raised" )
lable_t.place(x=30,y=300)

lable_vn = Label(root,text="Vant",width = 10,font=("arial",14),fg='white',bg='#7E1F86',borderwidth=3,relief="raised")
lable_vn.place(x=30,y=350)

lable_u = Label(root,text="Umiditate",width = 10,font=("arial",14),fg='white',bg='#7E1F86',borderwidth=3,relief="raised")
lable_u.place(x=30,y=400)

lable_p = Label(root,text="Presiune",width = 10,font=("arial",14),fg='white',bg='#7E1F86',borderwidth=3,relief="raised")
lable_p.place(x=400,y=250)

lable_vz = Label(root,text="Vizibilitate",width = 10,font=("arial",14),fg='white',bg='#7E1F86',borderwidth=3,relief="raised")
lable_vz.place(x=400,y=300)

lable_r = Label(root,text="Rasarit",width = 10,font=("arial",14),fg='white',bg='#7E1F86',borderwidth=3,relief="raised")
lable_r.place(x=400,y=350)

lable_ap = Label(root,text="Apus",width = 10,font=("arial",14),fg='white',bg='#7E1F86',borderwidth=3,relief="raised")
lable_ap.place(x=400,y=400)

#lable_ora = Label(root,text=" ",width = 7,bg='white',font=("bold",16),fg='black')
#lable_ora.place(x=200,y=650)

lable_vremea = Label(root,text="",width = 15,bg='white',font=("arial",14,"bold"),fg='black')
lable_vremea.place(x=180,y=250)

lable_temperatura = Label(root,text="",width = 9,bg='white',font=("arial",14,"bold"),fg='black')
lable_temperatura.place(x=180,y=300)

lable_vant = Label(root,text="",width = 9,bg='white',font=("arial",14,"bold"),fg='black')
lable_vant.place(x=180,y=350)

lable_umiditate = Label(root,text="",width = 9,bg='white',font=("arial",14,"bold"),fg='black')
lable_umiditate.place(x=180,y=400)

lable_presiune = Label(root,text="",width = 9,bg='white',font=("arial",14,"bold"),fg='black')
lable_presiune.place(x=550,y=250)

lable_vizibilitate = Label(root,text="",width = 9,bg='white',font=("arial",14,"bold"),fg='black')
lable_vizibilitate.place(x=550,y=300)

lable_rasarit = Label(root,text="",width = 9,bg='white',font=("arial",14,"bold"),fg='black')
lable_rasarit.place(x=550,y=350)

lable_apus = Label(root,text="",width = 9,bg='white',font=("arial",14,"bold"),fg='black')
lable_apus.place(x=550,y=400)
 
btn=Button(root,text="Vezi vremea",width=10,font=("cambria",14 ,"bold"),bg='#B80C09',fg='white',bd=3,command=showWeather).place(x=430,y=110)

root.mainloop()