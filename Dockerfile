# Usa imagen oficial de Python slim para mantenerlo ligero
FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia solo requirements para aprovechar cache de Docker al instalar dependencias
COPY requirements.txt .

# Actualiza pip e instala las dependencias
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copia todo el código al contenedor
COPY . .

# Expone el puerto en el que Flask escuchará
EXPOSE 5000

# Variable de entorno para que Flask sepa dónde está la app
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Comando para lanzar la aplicación con Gunicorn (más robusto para producción)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
