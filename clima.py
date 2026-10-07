import tkinter as tk
import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
import json
from datetime import datetime



vent = tk.Tk()
vent.geometry("500x500")
vent.title("Reconocimiento de voz")


text_to_speech = pyttsx3.init()


def speak(audio):
    text_to_speech.say(audio)
    text_to_speech.runAndWait()

def r_audio():

    speak("como puedo ayudarte?")

    reconocimiento = sr.Recognizer()

    try:
        with sr.Microphone(device_index=15) as source:

            print("Escuchando...")
            reconocimiento.adjust_for_ambient_noise(
                source,
                duration=1
            )

            audio = reconocimiento.listen(source)

        resultado.config(
            text="Procesando.."
        )

        vent.update

        voice_data = reconocimiento.recognize_google(
            audio,
            language="es-MX"
        )

        print("Tu dijiste:", voice_data)

        resultado.config(
            text="Tu dijiste: \n\n" + voice_data
        )

        respond(voice_data.lower())

    except sr.UnknownValueError:

        print("No entendí la solicitud.")

        resultado.config(
            text="no entendi tu solicitud.\n\n"
                "intenta nuevamente"
        )

    except sr.RequestError as error:
        print("Problema con el servicio:", error)

        resultado.config(
            text="Problema con el servicio de reconocimiento.\n\n"
        )

    except Exception as error:
        print("Problema con el micrófono:", error)

        resultado.config(
            text="Problema con el micrófono.\n\n"
                + str(error)
        )

def respond(voice_data):

    print("Soliciud",voice_data)


    if "nombre" in voice_data:

        respuesta = "Mi nombre es Jarvis"

        speak(respuesta)

        speak(respuesta)

        resultado.config(
            text="jarvis:\n\n" + respuesta
        )

    elif "hora" in voice_data:

        now = datetime.now()

        current_time = now.strftime("%H: %M: %S")

        respuesta = "La hora actual es" + current_time

        speak(respuesta)

        speak(respuesta)

        resultado.config(
            text="jarvis:\n\n" + respuesta
        )


    elif "google" in voice_data:


        respuesta = "Abriendo Google" 

        speak(respuesta)

        speak(respuesta)

        webbrowser.open(
            "https://www.google.com"
        )


    elif "youtube" in voice_data:


        respuesta = "Abriendo Youtube" 

        speak(respuesta)

        speak(respuesta)

        webbrowser.open(
            "https://www.youtube.com"
        )

    elif "clima" in voice_data:

        respuesta = "Buscando el clima"
        speak(respuesta)

        try:
            api_request = requests.get(
                "https://api.openweathermap.org/data/2.5/weather?q=" + "Ciudad de Mexico" +"&appid=" + "21cab08deb7b27f4c2b55f3e2df28ea4"
            )

            api_output_json = api_request.json()

            weather_info = api_output_json["weather"][0]["description"]
            humidity = api_output_json["main"]["humidity"]
            temperature = api_output_json["main"]["temp"]

            respuesta = (
                "El clima en Ciudad de México es "
                + weather_info
                + ". La temperatura es de "
                + str(round(temperature))
                + " grados. "
                + "La humedad es del "
                + str(humidity)
                + " por ciento."
            )

            speak(respuesta)

            resultado.config(
                text="jarvis:\n\n" + respuesta
            )

        except Exception as error:

            print("Error:", error)

            respuesta = "No pude obtener el clima."

            speak(respuesta)

            resultado.config(
                text="jarvis:\n\n" + respuesta
            )




    else:

        respuesta = "No conozco esa solicitud" 


        speak(respuesta)

        speak(respuesta)

        resultado.config(
            text="jarvis:\n\n" + respuesta
        )


boton = tk.Button(
    vent,
    text="HABLAR",
    command=r_audio
)

boton.pack(pady=100)


resultado = tk.Label(
    vent,
    text="Presiona HABLAR \n\n"
        "Puedes decir:\n"
        "Cual es tu nombre?:\n"
        "que hora es?:\n"
        "Abre google:\n"
        "Abre Youtube:\n"
        "clima:\n",
    font=("Arial", 12),
    wraplength=400

)

resultado.pack(pady=20)


vent.mainloop()