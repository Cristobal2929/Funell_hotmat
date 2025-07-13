# Dockerfile para Flask en Fly.io

FROM python:3.11-slim

# Directorio de trabajo
WORKDIR /app

# Copia todo el proyecto
COPY . .

# Actualiza pip e instala dependencias
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expone el puerto que usará Flask (usamos 8080 para Fly.io)
EXPOSE 8080

# Comando para arrancar la app
CMD ["python", "app.py"]
