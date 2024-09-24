# Usa una imagen base de Python
FROM python:3.8-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY . /app

# Instala las dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto en el que correrá FastAPI
EXPOSE 8000

# Comando para ejecutar la aplicación al iniciar el contenedor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
