# Análisis de Sentimiento con LSTM y FastAPI

Este proyecto consiste en un sistema de análisis de sentimientos utilizando un modelo de Deep Learning (LSTM) para clasificar opiniones de películas como positivas o negativas. El modelo está entrenado con el dataset **IMDb Movie Reviews** y está desplegado como una API REST utilizando **FastAPI**.

## Estructura del Proyecto

El proyecto se divide en tres componentes principales:

- **train_model.py**: Script para entrenar el modelo LSTM.
- **main.py**: Script para desplegar el modelo entrenado utilizando FastAPI.
- **model/**: Carpeta que contiene el modelo entrenado y el tokenizer.

## Configuración e Instalación

### Requisitos Previos

- Python 3.8 o superior
- Se recomienda usar un entorno virtual (opcional)

### Instalación de Dependencias

Primero, clona el repositorio y navega a la carpeta del proyecto:

```bash
git clone https://github.com/tu-usuario/sentiment-analysis-lstm.git
cd sentiment-analysis-lstm

Luego, instala las dependencias necesarias utilizando pip:
pip install -r requirements.txt

Entrenamiento del Modelo 
Si deseas entrenar el modelo desde cero, ejecuta el siguiente comando
python train_model.py

El modelo entrenado y el tokenizer se guardarán en la carpeta model/.

Ejecución del Servidor FastAPI
Una vez que el modelo esté entrenado, puedes desplegarlo como una API REST utilizando FastAPI. Para iniciar el servidor, ejecuta:
uvicorn main:app --reload

El servidor estará disponible en http://127.0.0.1:8000.

Ejemplo de Solicitud a la API
Puedes realizar una solicitud POST a la API con un review en formato JSON, como se muestra a continuación:

curl -X 'POST' \
  'http://127.0.0.1:8000/predict/' \
  -H 'Content-Type: application/json' \
  -d '{
  "review": "Esta película fue increíble. Las actuaciones y la trama fueron sobresalientes."
}'

Respuesta Esperada
La respuesta será en formato JSON, indicando el sentimiento (positivo o negativo) y la confianza del modelo:
{
  "sentiment": "Positive",
  "confidence": 0.85
}

Contenidos del Proyecto
train_model.py: Código para el entrenamiento del modelo LSTM.
main.py: Código para desplegar la API utilizando FastAPI.
model/: Carpeta que contiene el modelo entrenado (sentiment_lstm.h5) y el tokenizer (tokenizer.pickle).
README.md: Documentación del proyecto.
requirements.txt: Dependencias del proyecto.
test_reviews/: Carpeta con ejemplos de reseñas para probar la API (opcional).

Licencia
Este proyecto está bajo la licencia MIT.