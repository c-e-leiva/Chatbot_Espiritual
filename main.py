"""
Este archivo es el punto de entrada de la aplicación web basada en Flask. Su objetivo principal es gestionar las solicitudes HTTP entrantes,
manejar la lógica para responder preguntas y generar audios en formato MP3 a partir de texto. Utiliza el servicio de generación de texto a voz
de Google Cloud, y la lógica está separada en otro módulo (logic.py). Además, maneja los errores y proporciona respuestas claras al cliente.
"""

# Importar las bibliotecas necesarias
from flask import Flask, render_template, request, jsonify, Response
from google_tts import speak_text  # Importar la función que convierte texto a voz
from logic import find_best_quote  # Importar la función que maneja la lógica para obtener la mejor cita
import logging

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Configurar el logger para registrar eventos e información sobre el funcionamiento del servidor
logging.basicConfig(level=logging.INFO)

# Ruta principal ('/') que maneja las solicitudes GET y POST
@app.route('/', methods=['GET', 'POST'])
def home():
    try:
        # Si la solicitud es POST y contiene una pregunta, procesar la pregunta
        if request.method == 'POST' and 'question' in request.form:
            question = request.form['question']
            # Obtener la mejor cita en base a la pregunta realizada
            response = find_best_quote(question)  # Llamar a la función que responde la pregunta
            return jsonify({'response': response})  # Devolver la respuesta como JSON
        
        # Si la solicitud es GET, renderizar el formulario en el HTML
        return render_template('index.html')
    
    # Manejo de errores: si algo sale mal al procesar la solicitud, se registra el error y se devuelve una respuesta de error
    except Exception as e:
        logging.error(f"Error al procesar la solicitud: {e}")
        return jsonify({'error': 'Ocurrió un error procesando la solicitud.'}), 500

# Ruta '/get_audio' que maneja la conversión de texto a voz
@app.route('/get_audio', methods=['POST'])
def get_audio():
    try:
        # Obtener el texto enviado en la solicitud JSON
        text = request.json.get('text')
        
        # Si no se proporciona texto, devolver un error 400 (Bad Request)
        if not text:
            return jsonify({"error": "Texto no proporcionado."}), 400
        
        # Convertir el texto a audio usando la función de texto a voz
        audio_content = speak_text(text)
        
        # Si se genera el audio correctamente, devolverlo como respuesta binaria en formato MP3
        if audio_content:
            return Response(audio_content, mimetype="audio/mpeg")
        else:
            # Si no se pudo generar el audio, devolver un error 500 (Internal Server Error)
            return jsonify({"error": "No se pudo generar el audio."}), 500
    
    # Manejo de errores: si ocurre un problema en la conversión de texto a voz, se registra el error
    except Exception as e:
        logging.error(f"Error al procesar el audio: {e}")
        return jsonify({"error": "Ocurrió un error al generar el audio."}), 500

# Ejecutar la aplicación Flask si el archivo se ejecuta directamente
if __name__ == '__main__':
    # Ejecutar la aplicación en modo debug en el puerto 8000
    app.run(debug=True, port=8000)
