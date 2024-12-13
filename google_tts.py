"""
Este módulo se encarga de la conversión de texto a voz utilizando el servicio Google Cloud Text-to-Speech. A través de este servicio, 
se toma un texto como entrada y se genera un archivo de audio en formato MP3 con la voz configurada, listo para ser reproducido. 
Este proceso es útil en aplicaciones donde se desea una respuesta en formato de audio para mejorar la interacción con los usuarios.

"""

# Importar las bibliotecas
import os
from google.cloud import texttospeech
import logging

# Configurar las credenciales de Google Cloud para poder usar la API de Text-to-Speech.
# La clave de API se carga desde un archivo JSON, cuya ruta se obtiene de una variable de entorno o un valor por defecto.
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "E:/PROYECTO/CHAT - GCP/credencial/CREDENCIAL.JSON")

# Crear un cliente para acceder al servicio de Google Cloud Text-to-Speech
client = texttospeech.TextToSpeechClient()

# Configuración de la voz: 
# 1. El idioma es español (España) "es-ES".
# 2. Se selecciona una voz neural específica.
# 3. La velocidad de habla y el tono de la voz son configurables.
nombre_voz = "es-ES-Neural2-H"
speaking_rate = 0.89  # Velocidad de habla (1.0 es la velocidad normal)
pitch = 2.90  # Tono de la voz (0.0 es el tono base)

# Función principal para convertir el texto proporcionado en voz.
def speak_text(text):
    try:
        # Si no se proporciona texto, devolver None (sin procesar).
        if not text:
            return None
        
        # Crear un objeto que contiene el texto a sintetizar
        synthesis_input = texttospeech.SynthesisInput(text=text)
        
        # Configurar la voz a utilizar: idioma y nombre de la voz seleccionada.
        voice = texttospeech.VoiceSelectionParams(
            language_code='es-ES',  # Idioma español (España)
            name=nombre_voz        # Voz seleccionada previamente
        )
        
        # Configurar la codificación del audio, la velocidad de habla y el tono.
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3,  # Formato de salida (MP3)
            speaking_rate=speaking_rate,  # Velocidad de la voz
            pitch=pitch                   # Tono de la voz
        )

        # Llamar a la API de Google para generar el audio a partir del texto.
        response = client.synthesize_speech(
            input=synthesis_input,
            voice=voice,
            audio_config=audio_config
        )

        # Retornar el contenido binario del audio generado (el archivo de audio en MP3)
        return response.audio_content

    # En caso de un error, se registra el error y se retorna None.
    except Exception as e:
        logging.error(f"Error al convertir el texto a voz: {e}")
        return None

