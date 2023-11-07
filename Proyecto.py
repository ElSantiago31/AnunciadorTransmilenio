    # Proyecto simulador de alerta paraderos de Transmilenio
# 1. instalación de la librería pyttsx3

import pyttsx3
from tkinter import *
import os


listaTM1D50 = ["Portal Américas", "Calle 26", "Calle 34", "Calle 45", "Calle 57",
                "Calle 72", "Calle 76", "Minuto de Dios", "Granja - Carrera 77", "Portal de la 80"]

listaTM2D51 = ["Portal de Usme", "Avenida Jiménez", "Calle 19",
                "Calle 26", "Avenida 39", "Escuela Militar"]



def ventana():
    global ventana_prin
    global pestañas_color
    pestañas_color="#e9df46"
    ventana_prin=Tk()
    ventana_prin.geometry ("300x250")
    ventana_prin.title("TransmiConduc")
    Label (text="TransmiConduc", bg="#d90a10", width="300", height="2", font=("Futura", 13)).pack()
    Label (text="").pack()
    Button (text="Iniciar Sesion", height="2", width="30", bg=pestañas_color, command=login) .pack()
    Label (text="").pack()
    Button (text="Registrar Conductor", height="2",width="30", bg=pestañas_color, command=registro) .pack()
    Label (text="").pack()
    ventana_prin.mainloop()

def registro_user():
    usuario_info = nombre_usuario.get()
    clave_info = contra.get()

    carpeta = open(usuario_info, "w")
    carpeta.write(usuario_info + "\n")
    carpeta.write (clave_info)
    carpeta.close()
    entrada_nombre.delete(0, END)
    entrada_clave.delete(0, END)
    Label(ventana_registro, text="Usuario registrado", fg="green", font=("calibri", 11)).pack()

def registro():
    global ventana_registro
    ventana_registro = Toplevel(ventana_prin)
    ventana_registro.title("Registro")
    ventana_registro.geometry ("300x250")
    global nombre_usuario
    global contra
    global entrada_nombre
    global entrada_clave
    nombre_usuario = StringVar()
    contra = StringVar()

    Label(ventana_registro, text="Enter data", bg="LightGreen") .pack()
    Label(ventana_registro, text="") .pack()
    etiqueta_nombre = Label(ventana_registro, text="Username")
    etiqueta_nombre.pack()
    entrada_nombre = Entry(ventana_registro, textvariable=nombre_usuario)
    entrada_nombre.pack()
    etiqueta_clave = Label(ventana_registro, text="Password")
    etiqueta_clave.pack()
    entrada_clave = Entry(ventana_registro, textvariable=contra, show='*')
    entrada_clave.pack()
    Label (ventana_registro, text="") .pack()
    Button (ventana_registro, text="Register", width=12, height=2, bg="#d90a10", command=registro_user).pack()

def login():
    global ventana_login
    ventana_login = Toplevel(ventana_prin)
    ventana_login.title ("Account Access")
    ventana_login.geometry ("300x250")
    Label (ventana_login, text="Join username and password", bg="#d90a10", width="300", height="2", font=("Futura", 13)).pack()
    Label(ventana_login, text="") .pack()
    global verifica_usuario
    global verifica_clave
    verifica_usuario = StringVar()
    verifica_clave = StringVar()
    global entrada_login_usuario
    global entrada_login_clave
    Label (ventana_login, text="Username").pack()
    entrada_login_usuario = Entry(ventana_login, textvariable=verifica_usuario)
    entrada_login_usuario.pack()

    Label (ventana_login, text="").pack()
    Label(ventana_login, text="Password").pack()
    entrada_login_clave = Entry(ventana_login, textvariable=verifica_clave, show= '*')
    entrada_login_clave.pack()
    Label (ventana_login, text="").pack()
    Button(ventana_login, text="Join", width=12, height=2, command=verifica_login, bg=pestañas_color) .pack()

def verifica_login():
    usuariol = verifica_usuario.get()
    clavel = verifica_clave.get()
    entrada_login_usuario.delete(0, END)
    entrada_login_clave.delete(0, END)

    lista_archivos = os.listdir()
    if usuariol in lista_archivos:
        archivol = open(usuariol, "r")
        verifica = archivol.read() .splitlines()
        if clavel in verifica:
            exito_login()
        else:
            no_clave()
    else:
        no_usuario()

def no_usuario():
    global ventana_no_usuario
    ventana_no_usuario = Toplevel(ventana_prin)
    ventana_no_usuario.title ("ERROR")
    ventana_no_usuario.geometry ("200x100")
    Label (ventana_no_usuario, text="User not found").pack()
    Label (ventana_no_usuario,text="").pack()
    Button(ventana_no_usuario, text="OK",width=12, height=2, command=borrar_no_usuario, bg=pestañas_color).pack()

def exito_login():
    global ventana_exito
    ventana_exito = Toplevel (ventana_prin)
    ventana_exito.title("Exito")
    ventana_exito.geometry ("300x300")
    Label (ventana_exito, text="Successful",bg="#d90a10", width="300", height="2", font=("Futura", 13)).pack()
    Label (ventana_exito,text="").pack()
    Button(ventana_exito, text="Continuar",width=12, height=2, command=ruta, bg=pestañas_color) .pack()
    Label (ventana_exito,text="").pack()
    Label (ventana_exito, text="Imprimir rutas",bg="#d90a10", width="300", height="1", font=("Futura", 13)).pack()
    Label (ventana_exito,text="").pack()
    Button(ventana_exito, text="D50",width=12, height=2, command=impriD50, bg=pestañas_color) .pack()
    Button(ventana_exito, text="D51",width=12, height=2, command=impriD51, bg=pestañas_color) .pack()

def no_clave():
    global ventana_no_clave
    ventana_no_clave = Toplevel(ventana_login)
    ventana_no_clave.title ("ERROR")
    ventana_no_clave.geometry ("200x100")
    Label (ventana_no_clave, text="Incorrent password",bg="#d90a10", width="300", height="1", font=("Futura", 10)).pack()
    Label (ventana_no_clave,text="").pack()
    Button (ventana_no_clave, text="OK", command=borrar_no_clave, bg=pestañas_color,width=12, height=2).pack()

def borrar_no_clave():
    ventana_no_clave.destroy()

def borrar_no_usuario():
    ventana_no_usuario.destroy()

def impriD50():
    global Ventana_ListaD50
    Ventana_ListaD50 = Toplevel(ventana_login)
    Ventana_ListaD50.title ("Lista D50")
    Ventana_ListaD50.geometry ("200x350")
    Label(Ventana_ListaD50,text="Paradas D50",bg="#d90a10", width="300", height="2", font=("Futura", 13)).pack()
    Label(Ventana_ListaD50,text="").pack()
    for i in listaTM1D50:
        Label(Ventana_ListaD50,text="{}".format(i)).pack()
    Label(Ventana_ListaD50,text="").pack()
    Button (Ventana_ListaD50, text="Cerrar", command=cerrarD50, bg=pestañas_color,width=12, height=2).pack()

def impriD51():
    global Ventana_ListaD51
    Ventana_ListaD51 = Toplevel(ventana_login)
    Ventana_ListaD51.title ("Lista D50")
    Ventana_ListaD51.geometry ("200x300")
    Label(Ventana_ListaD51,text="Paradas D51",bg="#d90a10", width="300", height="2", font=("Futura", 13)).pack()
    Label(Ventana_ListaD51,text="").pack()
    for i in listaTM2D51:
        Label(Ventana_ListaD51,text="{}".format(i)).pack()
    Label(Ventana_ListaD51,text="").pack()
    Button (Ventana_ListaD51, text="Cerrar", command=cerrarD51, bg=pestañas_color,width=12, height=2).pack()

def cerrarD50():
    Ventana_ListaD50.destroy()

def cerrarD51():
    Ventana_ListaD51.destroy()

def ruta():
    global ventana_ruta
    ventana_ruta= Toplevel(ventana_prin)
    ventana_ruta.title("Elegír Ruta")
    ventana_ruta.geometry("300x250")
    ventana_ruta.resizable(False,False)
    Label(ventana_ruta, text="Elige la Ruta",bg="#d90a10", width="300", height="2", font=("Futura", 13)).pack()
    Label (ventana_ruta,text="").pack()
    Button(ventana_ruta, text="D50",width=12, height=2, command=ruta_D50_iniciar, bg=pestañas_color).pack()
    Label (ventana_ruta,text="").pack()
    Button(ventana_ruta, text="D51", width=12, height=2,command=ruta_D51_iniciar, bg=pestañas_color).pack()

def ruta_D50_iniciar():
    global ventana_D50_Ini
    ventana_D50_Ini= Toplevel(ventana_prin)
    ventana_D50_Ini.title("Iniciar Ruta")
    ventana_D50_Ini.geometry("300x200")
    ventana_D50_Ini.resizable(False, False)
    Label(ventana_D50_Ini, text="Presione para iniciar",bg="#d90a10", width="300", height="2", font=("Futura", 13)).pack()
    Label(ventana_D50_Ini,text="").pack()
    Label(ventana_D50_Ini,text="").pack()
    Button(ventana_D50_Ini, text="Iniciar",width=12, height=2, command=ruta_D50, bg=pestañas_color).pack()


def ruta_D50():
    global ventana_D50
    ventana_D50= Toplevel(ventana_prin)
    ventana_D50.title("Ruta D50")
    ventana_D50.geometry("300x200")
    ventana_D50.resizable(False, False)
    Label(ventana_D50, text="Presione el botón cuando realice la parada",bg="#d90a10", width="300", height="2", font=("Futura", 11)).pack()
    Label(ventana_D50,text="").pack()
    Label(ventana_D50,text="").pack()
    Button(ventana_D50, text="Parada", command=voz_D50,width=12, height=2,bg="#e9df46").pack()

def voz_D50():
    texto = "Proximas paradas " + \
        str(listaTM1D50[0])+str(" y ")+str(listaTM1D50[1])
    engine = pyttsx3.init()
    engine.setProperty("rate", 135)
    engine.say(texto)
    engine.runAndWait()
    if len(listaTM1D50)==2:
        texto=("Destino, "+str(listaTM1D50[1]))
        engine = pyttsx3.init()
        engine.setProperty("rate", 135)
        engine.say(texto)
        engine.runAndWait()
        Label(ventana_D50,text="").pack()
        Button(ventana_D50, text="Cerrar", width=12, height=2,bg="#e9df46", command=terminar).pack()
    listaTM1D50.pop(0)

def ruta_D51_iniciar():
    global ventana_D51_Ini
    ventana_D51_Ini= Toplevel(ventana_prin)
    ventana_D51_Ini.title("Iniciar Ruta")
    ventana_D51_Ini.geometry("300x200")
    ventana_D51_Ini.resizable(False, False)
    Label(ventana_D51_Ini, text="Presione para iniciar",bg="#d90a10", width="300", height="2", font=("Futura", 13)).pack()
    Label(ventana_D51_Ini,text="").pack()
    Label(ventana_D51_Ini,text="").pack()
    Button(ventana_D51_Ini, text="Iniciar",width=12, height=2, command=ruta_D51, bg=pestañas_color).pack()

def ruta_D51():
    global ventana_D51
    ventana_D51= Toplevel(ventana_prin)
    ventana_D51.title("Ruta D51")
    ventana_D51.geometry("300x200")
    ventana_D51.resizable(False, False)
    Label(ventana_D51, text="Presione el botón cuando realice la parada",bg="#d90a10", width="300", height="2", font=("Cursive", 11)).pack()
    Label (ventana_D51,text="").pack()
    Label (ventana_D51,text="").pack()
    try:
        Button(ventana_D51, text="Parada", command=voz_D51,width=12, height=2,bg="#e9df46").pack()
    except IndexError:
        Label(ventana_D51, text="Ruta terminada.")


def voz_D51():
    texto = "Proximas paradas " + \
        str(listaTM2D51[0])+str(" y ")+str(listaTM2D51[1])
    engine = pyttsx3.init()
    engine.setProperty("rate", 135)
    engine.say(texto)
    engine.runAndWait()
    if len(listaTM2D51)==2:
        texto=("Destino, "+str(listaTM2D51[1]))
        engine = pyttsx3.init()
        engine.setProperty("rate", 135)
        engine.say(texto)
        engine.runAndWait()
        Label (ventana_D51,text="").pack()
        Button(ventana_D51, text="Cerrar", width=12, height=2,bg="#e9df46", command=terminar).pack()
    listaTM2D51.pop(0)

def terminar():
    ventana_prin.destroy()

ventana()
