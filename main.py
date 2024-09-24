# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
import pickle

# Cargar el tokenizer guardado
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

# Crear una instancia de la app FastAPI
app = FastAPI()

# 1. Cargar el modelo entrenado
model = load_model('lstm_sentiment_model.h5')

# 2. Definir el tamaño máximo de secuencia y vocabulario (debe ser consistente con el entrenamiento)
max_len = 200
vocab_size = 10000

# 3. Crear una clase Pydantic para el cuerpo de la solicitud
class ReviewInput(BaseModel):
    review: str

# 4. Dummy tokenizer (ejemplo). En producción, debes usar el mismo tokenizer con el que entrenaste tu modelo
# Aquí, reemplaza esto con tu tokenizer real
#tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=vocab_size)
# En producción, cargarías el tokenizer entrenado, por ejemplo:
# tokenizer = pickle.load(open('tokenizer.pickle', 'rb'))

# 5. Endpoint para verificar si el servidor está funcionando
@app.get("/")
def root():
    return {"message": "API Sentiment Analysis is running"}

# 6. Endpoint para predecir el sentimiento
@app.post("/predict/")
def predict_sentiment(review_input: ReviewInput):
    # 7. Preprocesar el texto de la entrada (tokenización y padding)
    text = [review_input.review]
    sequences = tokenizer.texts_to_sequences(text)
    padded_sequences = pad_sequences(sequences, maxlen=max_len, padding='post')
    
    # 8. Hacer la predicción
    prediction = model.predict(padded_sequences)
    
    # 9. Interpretar el resultado (0 = Negativo, 1 = Positivo)
    sentiment = "Positive" if prediction[0][0] > 0.5 else "Negative"
    
    # 10. Devolver el resultado como JSON
    return {"sentiment": sentiment, "confidence": float(prediction[0][0])}
