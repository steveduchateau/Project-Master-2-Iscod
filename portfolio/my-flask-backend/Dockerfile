# Utiliser l'image officielle de Python
FROM python:3.9

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier requirements.txt dans le conteneur
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code de l'application dans le conteneur
COPY . .

# Exposer le port sur lequel l'application Flask écoute
EXPOSE 5001

# Commande pour lancer l'application avec Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5001", "app:app"]
