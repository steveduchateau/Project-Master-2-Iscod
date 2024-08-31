Portfolio

Ce projet est un portfolio personnel conçu pour présenter mes compétences, projets, et expériences professionnelles. Il utilise une architecture web basée sur Docker pour déployer une application Angular pour mon frontend ,Python Flask pour mon backend et une base de données MySQL.

Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre machine :

Docker
Docker Compose

Installation

Clonez le dépôt du projet : git clone https://github.com/steveduchateau/Project-Master-2-Iscod.git
cd portfolio

Construisez les images Docker pour le frontend, le backend, et la base de données :

docker-compose build

Lancement du Projet

Pour démarrer tous les conteneurs, utilisez la commande suivante :

docker-compose up

(Tous les services (frontend, backend, et base de données) seront lancés simultanément.)

Configuration

Frontend : L'application Angular est servie via Nginx sur le port 80.
Backend : L'API Python Flask tourne sur le port 5001.
Base de données : MySQL est accessible sur le port 3306.
Pour modifier les configurations par défaut, éditez le fichier docker-compose.yml.

Utilisation

Accédez au frontend de l'application en ouvrant votre navigateur à l'adresse :http://localhost:8080.
L'API backend est disponible sur http://localhost:5001.

Technologies Utilisées

Frontend : Angular, Nginx
Backend : Python, Flask
Base de données : MySQL
Conteneurisation : Docker, Docker Compose

Auteurs

Steve Duchateau - Développeur principal - https://github.com/steveduchateau



