# Utiliser une image Python officielle
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt requirements.txt
COPY app.py app.py

# Installer les dépendances
RUN pip install -r requirements.txt

# Exposer le port 5000 pour Flask
EXPOSE 5000

# Démarrer l'application
CMD ["python", "app.py"]
