import tkinter as tk
import requests 

class pokemon:                                                              

    def _init_ (self, nombre, tipo, habilidades, estadisticas):             
        self.nombre = nombre
        self.tipo = tipo
        self.habilidades = habilidades
        self.estadisticas = estadisticas



def obtener_datos_poke():
    pokeid = barra_de_texto.get()                           #es para tener el id de la api
    url = f"https://pokeapi.com/api/v2/pokemon/{pokeid}"
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        data = respuesta.json()

        nombre = data['name']
        tipo = data['types'][0]['type']['name']
        habilidades = [habilidad ['abilities']['name'] for habilidad in data ['abilities']]
        estadisticas = {stat['stat']['name']: stat['base_stat'] for stat in data ['stats']}

        etiqueta_nombre.config(text = f"nombre : {nombre}")   
        etiqueta_tipo.config(text = f"tipo : {tipo}")
        etiqueta_habilidades.config(text = f"habilidades : {', ' .join(habilidades)}")
        etiqueta_estadisticas.config(text = f"estadisticas : {estadisticas}")
    else:
        etiqueta_nombre.config(text="error")


ventana = tk.Tk()
ventana.title("poki")
ventana.geometry("400x400")

barra_de_texto = tk.Entry(ventana,bg="grey")
barra_de_texto.pack()

infoboton = tk.Button (ventana,text="Obtener Datos", command=obtener_datos_poke, bg= "red")
infoboton.pack()

etiqueta_tipo = tk.Label(ventana,text="")
etiqueta_tipo.pack()

etiqueta_nombre = tk.Label(ventana,text="")
etiqueta_nombre.pack()

etiqueta_habilidades = tk.Label(ventana,text="")
etiqueta_habilidades.pack()

etiqueta_estadisticas = tk.Label(ventana,text="")
etiqueta_estadisticas.pack()


ventana.mainloop()
