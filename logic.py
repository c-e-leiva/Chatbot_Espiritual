"""
Este archivo tiene como función gestionar las respuestas del chatbot. Cuando el usuario hace una pregunta, el sistema busca la cita más 
relevante usando un modelo de lenguaje preentrenado (DistilBERT) para procesar las preguntas y compararlas con las preguntas almacenadas 
en un archivo JSON. También maneja saludos y despedidas, y puede devolver consejos aleatorios basados en frases específicas.
"""

# Importar las bibliotecas necesarias
import random
import json
from transformers import DistilBertTokenizer, DistilBertModel
import torch

# Ruta del archivo JSON que contiene citas y preguntas
json_file_path = r"E:\proyecto\chatbot\citas_preguntas_buda\data.JSON"

# Cargar datos desde el archivo JSON
with open(json_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)  # Cargar las citas y preguntas del archivo JSON

# Lista de frases aleatorias para responder con citas de Buda
random_messages = [
    "Esta cita de Buda puede ofrecerte una reflexión sobre tu inquietud:",
    "Aquí tienes una enseñanza de Buda que puede iluminar tu situación:",
    "Considera esta cita de Buda como una posible guía para tu consulta:",
    "Buda ofrece esta sabiduría que podría ser útil para tu reflexión:",
    "En respuesta a tu inquietud, esta cita de Buda puede ayudarte:",
    "Esta cita de Buda podría ser relevante para tu solicitud:"
]

# Cargar el modelo de DistilBERT y su tokenizador
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
model = DistilBertModel.from_pretrained('distilbert-base-uncased')

# Precomputar los embeddings de las preguntas y citas para comparación rápida
precomputed_embeddings = []
for cita in data:
    for pregunta in cita['preguntas']:
        inputs = tokenizer(pregunta, return_tensors='pt', padding=True, truncation=True)  # Tokenización de la pregunta
        with torch.no_grad():
            outputs = model(**inputs)  # Obtener las salidas del modelo (embeddings)
        embedding = outputs.last_hidden_state.mean(dim=1)  # Calcular el embedding medio
        precomputed_embeddings.append((cita['cita'], pregunta, embedding))  # Guardar la cita, pregunta y su embedding

# Función para obtener el embedding de una entrada de texto (usada para comparar con las preguntas)
def get_embedding(text):
    inputs = tokenizer(text, return_tensors='pt', padding=True, truncation=True)  # Tokenización del texto
    with torch.no_grad():
        outputs = model(**inputs)  # Obtener la salida del modelo
    return outputs.last_hidden_state.mean(dim=1)  # Devolver el embedding medio

# Función principal para encontrar la mejor cita para una entrada del usuario
def find_best_quote(user_input):
    # Listas de saludos y despedidas para respuestas rápidas
    greetings = ["hola", "hello", "buenos días", "buenas tardes", "buenas noches", "saludos", "buenas", "holis", "holu", "hi"]
    farewells = ["hasta luego", "chau", "adiós", "nos vemos", "hasta pronto", "bye", "gracias", "adios", "nv", "EXIT"]

    # Lista de frases que indican que el usuario quiere un consejo o cita
    advice_phrases = [
        "dame un consejo", "brindame un consejo", "quiero un consejo", "aconsejame", "dame una cita",
        "dame una opinion", "que piensas", "que piensas al respecto", "cual es tu opinion", "puedes darme un consejo",
        "que opinas", "podrias aconsejarme", "me das un consejo", "necesito un consejo", "tienes algun consejo", "consejo"
    ]

    # Convertir la entrada del usuario a minúsculas para comparaciones insensibles a mayúsculas
    user_input_lower = user_input.strip().lower()

    # Responder si la entrada es un saludo
    if any(greet in user_input_lower for greet in greetings):
        return "Hola, ¡qué alegría saludarte! ¿Qué enseñanza o reflexión te gustaría explorar ahora?"

    # Responder si la entrada es una despedida
    if any(farewell in user_input_lower for farewell in farewells):
        return "Gracias por tu tiempo. Que la paz y la sabiduría te guíen. Espero que pronto podamos seguir reflexionando juntos. Hasta pronto."
    
    # Responder si la entrada es una solicitud de consejo
    for phrase in advice_phrases:
        if phrase in user_input_lower:
            random_quote = random.choice(data)  # Seleccionar una cita aleatoria
            random_message = random.choice(random_messages)  # Seleccionar un mensaje aleatorio
            return f"{random_message} {random_quote['cita']}"  # Devolver la cita con el mensaje aleatorio

    # Si no es una solicitud de consejo, buscar la cita más relevante usando embeddings
    user_embedding = get_embedding(user_input)  # Obtener el embedding de la entrada del usuario
    
    best_match = None  # Inicializar la mejor coincidencia
    best_similarity = -1  # Inicializar la mejor similitud

    # Comparar el embedding del usuario con las preguntas precomputadas
    for cita, pregunta, pregunta_embedding in precomputed_embeddings:
        similarity = torch.cosine_similarity(user_embedding, pregunta_embedding).item()  # Calcular la similitud
        if similarity > best_similarity:  # Si la similitud es mejor que la actual, actualizar
            best_similarity = similarity
            best_match = cita

    # Devolver la mejor cita encontrada o pedir al usuario que reformule la pregunta
    if best_match:
        random_message = random.choice(random_messages)  # Seleccionar un mensaje aleatorio
        return f"{random_message}\n\n{best_match}"  # Devolver la cita más relevante
    else:
        return "¿Podrías reformular tu pregunta para ayudarme a ofrecerte una cita más iluminadora?"
