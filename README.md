# 🤖 **Chatbot Espiritual** 🧘‍♂️

## Índice

1. [Descripción del Proyecto](#descripción-del-proyecto)
2. [Objetivo](#objetivo)
3. [Proceso de Desarrollo](#proceso-de-desarrollo)
   - [Recolección y Preparación de Datos](#recolección-y-preparación-de-datos)
   - [Traducción y Mejora de Citas](#traducción-y-mejora-de-citas)
   - [Clasificación de Citas](#clasificación-de-citas)
   - [Almacenamiento en Estructura JSON](#almacenamiento-en-estructura-json)
   - [Funcionalidad del Chatbot](#funcionalidad-del-chatbot)
4. [Tecnologías y Herramientas Utilizadas](#tecnologías-y-herramientas-utilizadas)
5. [Estructura del Proyecto](#estructura-del-proyecto)
   - [main.py](#mainpy)
   - [google_tts.py](#google_ttspy)
   - [logic.py](#logicpy)
   - [data.json](#datajson)
6. [Ejecución](#ejecución)
7. [Licencia](#licencia)

## Descripción del Proyecto

El proyecto "Chatbot Espiritual" tiene como objetivo proporcionar una experiencia introspectiva y filosófica a los usuarios a través de citas de Buda, basadas en el dataset "Buddha Quotes with Sentiments". Este dataset incluye más de 100 citas de Buda junto con una clasificación de sentimientos asociados, lo que permite al chatbot ofrecer respuestas profundas y resonantes en relación a temas de vida, felicidad, sufrimiento y otros aspectos espirituales y reflexivos. 

El chatbot está diseñado para fomentar una desconexión de la tecnología centrada en la lógica y el análisis, ofreciendo en su lugar una perspectiva filosófica y espiritual. El proyecto se utiliza como un recurso inspirador y orientador para quienes buscan un momento de paz y sabiduría. No tiene la intención de modificar ni ofender las enseñanzas budistas, sino de servir como una herramienta de reflexión.

## Objetivo🎯

El propósito de este chatbot es ofrecer respuestas basadas en citas de Buda que se alineen con preguntas sobre temas de vida, felicidad, sufrimiento, y otros aspectos espirituales y reflexivos. Al responder a las consultas, el chatbot utiliza citas de Buda clasificadas por categorías temáticas, garantizando que las respuestas sean tanto relevantes como profundas.

Este proyecto proporciona una pausa espiritual y filosófica, permitiendo a los usuarios reflexionar sobre las enseñanzas de Buda de manera accesible y respetuosa.

## Proceso de Desarrollo🔧

### Recolección y Preparación de Datos 📊
- Se recopiló el dataset "Buddha Quotes with Sentiments", que incluye citas en inglés junto con sus sentimientos correspondientes.
- Posteriormente, se realizó una visualización de los datos para comprender su estructura y la distribución por sentimiento.
- El proceso de limpieza de datos eliminó columnas innecesarias y caracteres irrelevantes para el uso de las citas.

### Traducción y Mejora de Citas 🌐
- Para que las citas fueran accesibles al público hispanohablante, se utilizó la biblioteca `googletrans` para traducir las citas del inglés al español.
- Las traducciones iniciales fueron procesadas con un modelo de OpenAI GPT para ajustar la traducción y garantizar que la esencia de las enseñanzas budistas se mantuviera fiel al texto original.

### Clasificación de Citas 📚
- Las citas fueron organizadas en diferentes categorías temáticas para facilitar respuestas relevantes según la consulta del usuario. Las categorías definidas fueron:
  - Sabiduría
  - Reflexión
  - Compasión
  - Felicidad
  - Mente
  - Sufrimiento
  - Negatividad (Maldad y Sin categoría)
  - Tranquilidad (Desapego y Paz)
  - Práctica (Meditación y Enseñanzas)

### Almacenamiento en Estructura JSON 💾
- Las citas clasificadas se almacenaron en un archivo JSON, estructurado en formato de diccionario. Cada entrada contiene la cita, su categoría y una lista de preguntas relevantes asociadas a la categoría.

### Funcionalidad del Chatbot 💬
- El chatbot busca la categoría adecuada en el archivo JSON y selecciona la cita que mejor responde a la consulta del usuario.
- Se implementaron mensajes de bienvenida y despedida, proporcionando una experiencia amigable y acogedora.

## Tecnologías y Herramientas Utilizadas 🛠️

- **Flask**: Framework web utilizado para gestionar las peticiones y respuestas del chatbot en un servidor local.
- **BERT**: Utilizado para mejorar la comprensión contextual de las citas y las preguntas.
- **PyTorch**: Usado para el modelo de comprensión de lenguaje y clasificación.
- **Googletrans**: Para la traducción automática de citas del inglés al español.
- **OpenAI GPT**: Para mejorar la calidad y fidelidad de las traducciones.
- **Google Text-to-Speech (TTS)**: Para convertir las respuestas del chatbot en voz, ofreciendo una experiencia interactiva.
- **Google Speech-to-Text (STT)**: Para permitir al chatbot reconocer comandos de voz.
- **JSON**: Para almacenar las citas y organizar las respuestas según las categorías definidas.

## Estructura del Proyecto 📁

El proyecto está organizado en varios módulos, cada uno con una función específica para gestionar las interacciones y respuestas del chatbot. A continuación, se describe cada uno:

### `main.py` 📝
El módulo principal del chatbot que gestiona la ejecución del servidor Flask, maneja las peticiones HTTP y coordina la interacción con el usuario. Aquí se inicializa la funcionalidad básica del chatbot, incluyendo el procesamiento de entradas y la entrega de respuestas en formato de texto o voz.

### `google_tts.py` 🎙️
Este módulo se encarga de integrar la API de Google Text-to-Speech (TTS), convirtiendo las respuestas textuales en voz. Aquí se configura el tono, la velocidad y el volumen de la voz para una experiencia más personalizada.

### `logic.py` 🤖
Este módulo contiene la lógica del chatbot, gestionando la búsqueda y selección de las citas relevantes según la consulta del usuario. Organiza las citas por categorías temáticas y utiliza modelos como BERT y PyTorch para comprender el contexto de las preguntas del usuario.

### `data.json` 📚
Archivo que contiene las citas de Buda organizadas por categorías. Este archivo es esencial para el funcionamiento del chatbot, ya que le permite buscar citas relacionadas con temas específicos solicitados por el usuario.

## Ejecución 🚀

Para ejecutar el chatbot, simplemente inicia el archivo principal del proyecto (main.py). Una vez que el servidor esté en funcionamiento, abre tu navegador web y accede a la dirección local http://localhost:8000.
Desde allí podrás interactuar con el chatbot, hacer preguntas sobre temas espirituales y recibir respuestas en forma de citas de Buda.

## Licencia 📝
Este proyecto está bajo la Licencia MIT. Puedes usar, modificar y distribuir este código de acuerdo con los términos de la licencia.
