# Portfolio

Bienvenue sur mon portfolio ! Ce projet est conçu pour présenter mes compétences, projets, et expériences professionnelles. Il utilise une architecture web moderne avec Docker pour déployer une application Angular pour le frontend, Python Flask pour le backend, et une base de données MySQL.

## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre machine :

- **Docker** : [Installation Docker](https://docs.docker.com/get-docker/)
- **Docker Compose** : [Installation Docker Compose](https://docs.docker.com/compose/install/)

## Installation

Suivez ces étapes pour installer et configurer le projet :

1. **Clonez le dépôt du projet** :

    ```bash
    git clone https://github.com/steveduchateau/Project-Master-2-Iscod.git
    ```

2. **Accédez au répertoire du projet** :

    ```bash
    cd portfolio
    ```

3. **Construisez les images Docker pour le frontend, le backend, et la base de données** :

    ```bash
    docker-compose build
    ```

## Lancement du Projet

Pour démarrer tous les conteneurs, utilisez la commande suivante :

```bash
docker-compose up


(Tous les services (frontend, backend, et base de données) seront lancés simultanément.)

## Configuration

Frontend : L'application Angular est servie via Nginx sur le port 80.
Backend : L'API Python Flask tourne sur le port 5001.
Base de données : MySQL est accessible sur le port 3306.
Pour modifier les configurations par défaut, éditez le fichier docker-compose.yml.

## Utilisation

Accédez au frontend de l'application en ouvrant votre navigateur à l'adresse :http://localhost:8080.
L'API backend est disponible sur http://localhost:5001.

##Technologies Utilisées

Frontend : Angular, Nginx
Backend : Python, Flask
Base de données : MySQL
Conteneurisation : Docker, Docker Compose

## Auteurs

Steve Duchateau - Développeur principal - https://github.com/steveduchateau



