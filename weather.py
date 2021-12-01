import tkinter as tk
import requests
import time

def get_weather(ciudad1: str):
    try:
        #ciudad = textfield.get()
        ciudad = ciudad1
        api = "http://api.openweathermap.org/data/2.5/weather?q="+ciudad+"&appid=eaf6b3576ac41a0c689053e2ac87d22f"
        json_data = requests.get(api).json()
        condicion = json_data['weather'][0]['main']
        temp = int(json_data['main']['temp'] - 273.15)
        min_temp = int(json_data['main']['temp'] - 273.15)
        max_temp = int(json_data['main']['temp'] - 273.15)
        presion = json_data['main']['pressure']
        humedad = json_data['main']['humidity']
        viento = json_data['wind']['speed']
        sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 21600))
        sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] - 21600))
        
        info_final = condicion + "\n" + str(temp) + "°C"
        final = "\n" + "Max. Temp: " + str(max_temp) + "\nMin. Temp: " + str(min_temp) + "\nPresion: " + str(presion) + "\nHumedad: " + str(humedad) + "\nViento: " + str(viento) + "\nSalida del sol: " + sunrise + "\nPuesta de sol: " + sunset
        
        #print(info_final)
        #print(final)

        """label1.config(text=final_info)
        label2.config(text=final_data)"""

        resultado = 'Exito'
        return resultado
    except:
        resultado = "Error encontrando clima para la ciudad '" + ciudad1 + "'"
        print(resultado)
        return resultado


if __name__ == '__main__':
    #get_weather('saltillo')
    """canvas = tk.Tk()
    canvas.geometry("600x500")
    canvas.title("Weather App")

    f = ("poppins", 15, "bold")
    t = ("poppins", 35, "bold")

    textfield = tk.Entry(canvas, font = t)
    textfield.pack(pady = 20)
    textfield.focus()
    textfield.bind('<Return>', get_weather)

    label1 = tk.Label(canvas, font = t)
    label1.pack()
    label2 = tk.Label(canvas, font = f)
    label2.pack()

    canvas.mainloop()
"""