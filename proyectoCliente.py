import requests
import urllib
from tkinter import *

api_url = "http://www.mapquestapi.com/directions/v2/route?"
key = "pmcCEtp7SwbG8Y2YGdyqUFDnb9pvtQ4F"

D50 = ["Portal Américas", "Estacion Calle 26", "Estacion Calle 34", "Estacion Calle 45", "Estacion Calle 57",
                "Estacion Calle 72", "Estacion Calle 76", "Estacion Minuto de Dios", "Estacion Granja - Carrera 77", "Portal de la 80"]

D51 = ["Estacion Portal de Usme", "Estacion Avenida Jiménez", "Estacion Calle 19",
                "Estacion Calle 26", "Estacion Avenida 39", "Estacion Escuela Militar"]


def IniDest():
    global origen
    global llegada
    global ventana_Ini
    global pestañas_color
    pestañas_color="#e9df46"
    ventana_Ini= Tk()
    origen=StringVar()
    llegada=StringVar()
    ventana_Ini.title("Inicio y Destino")
    ventana_Ini.geometry("350x400")
    ventana_Ini.resizable(False, False)
    Label(text="Bienvenido",bg="#d90a10", width="300", height="2", font=("Futura", 13)).pack()
    Label(text="").pack()
    Label(text="Origen de partida").pack()
    Entry(textvariable=origen).pack()
    Label(text="").pack()
    Label(text="Destino de llegada").pack()
    Entry(textvariable=llegada).pack()
    Label(text="").pack()
    Button(text="Continuar",command=ruta,width=12, height=2, bg=pestañas_color).pack()
    Label(text="").pack()
    ventana_Ini.mainloop()

def ruta():
    global inicio
    global destino
    global ventana_ruta

    inicio=origen.get()
    destino=llegada.get()
    url = api_url + urllib.parse.urlencode({"key":key, "from":inicio+str(",bogotá, colombia"), "to":destino+str(",bogotá, colombia")})
    json_data = requests.get(url).json()
    status_code = json_data["info"]["statuscode"]
    if status_code == 0:
        trip_duration = json_data["route"]["formattedTime"]
        Label(text="Información del viaje desde {} hasta {}.".format(inicio,destino)).pack()
        Label(text="").pack()
        Label(text="Duración del viaje: {}".format(trip_duration)).pack()
        Label(text="").pack()
        Button(text="Instrucciones",command=instrucciones, width=12, height=2, bg=pestañas_color).pack()

def instrucciones():
    global instruc

    instruc= Toplevel(ventana_Ini)
    instruc.title("Dirección")
    instruc.geometry("800x400")
    instruc.resizable(True,True)
    inicio=origen.get()
    destino=llegada.get()
    url = api_url + urllib.parse.urlencode({"key":key, "from":inicio+str(",bogotá, colombia"), "to":destino+str(",bogotá, colombia")})
    json_data = requests.get(url).json()
    Label(instruc,text="Abrir en pantalla completa si es necesario",bg="#d90a10", width="300", height="2", font=("Futura", 13)).pack()
    Label(instruc,text="Direcciones:",bg=pestañas_color, width="125", height="2", font=("Futura", 10)).pack()
    for each in json_data["route"]["legs"][0]["maneuvers"]:
        distance = json_data["route"]["distance"] * 1.61
        distance_remaining = distance - each["distance"] * 1.61
        Label(instruc,text="{} ({:.2f} Km faltantes)".format(each["narrative"],distance_remaining)).pack()
        distance = distance_remaining
    Button(instruc, text="Finalizar", width=12, height=2, bg=pestañas_color, command=terminar).pack()

def terminar():
    ventana_Ini.destroy()
IniDest()
