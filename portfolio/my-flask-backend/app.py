import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_mysqldb import MySQL

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Configuration CORS pour autoriser toutes les origines

# Configuration de la base de données MySQL
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST', 'localhost')  # Hôte de la base de données, avec valeur par défaut 'localhost'
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER', 'root')  # Utilisateur de la base de données, avec valeur par défaut 'root'
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD', 'steve')  # Mot de passe de la base de données, avec valeur par défaut 'steve'
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB', 'Portfolio')  # Nom de la base de données, avec valeur par défaut 'Portfolio'

mysql = MySQL(app)  # Création de l'objet MySQL pour interagir avec la base de données

@app.route('/', methods=['GET'])
def home():
    return "Bienvenue sur mon backend Flask !", 200
    # Route principale, renvoie un message de bienvenue avec le code HTTP 200 (OK)

@app.route('/test-db', methods=['GET'])
def test_db():
    try:
        cursor = mysql.connection.cursor()  # Création d'un curseur pour exécuter des requêtes SQL
        cursor.execute('SELECT 1')  # Exécution d'une requête simple pour tester la connexion à la base de données
        cursor.close()  # Fermeture du curseur
        return "Connexion à la base de données MySQL réussie !", 200  # Réponse indiquant que la connexion est réussie
    except Exception as e:
        return f"Erreur de connexion à la base de données MySQL : {str(e)}", 500
        # Gestion des erreurs en cas d'échec de la connexion, avec le code HTTP 500 (Erreur interne du serveur)

@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.json  # Récupération des données JSON envoyées dans la requête POST
    first_name = data.get('firstName')  # Extraction du prénom
    last_name = data.get('lastName')  # Extraction du nom
    email = data.get('email')  # Extraction de l'adresse email
    message = data.get('message')  # Extraction du message

    try:
        cursor = mysql.connection.cursor()  # Création d'un curseur pour exécuter des requêtes SQL
        cursor.execute('INSERT INTO contact_messages (first_name, last_name, email, message) VALUES (%s, %s, %s, %s)',
                       (first_name, last_name, email, message))  # Insertion des données dans la table 'contact_messages'
        mysql.connection.commit()  # Validation des modifications dans la base de données
        cursor.close()  # Fermeture du curseur
        return jsonify({'message': 'Message enregistré avec succès'}), 200  # Réponse de succès avec le code HTTP 200 (OK)
    except Exception as e:
        return jsonify({'message': f'Erreur lors de l\'enregistrement du message : {str(e)}'}), 500
        # Gestion des erreurs en cas d'échec de l'enregistrement, avec le code HTTP 500 (Erreur interne du serveur)

@app.route('/api/competences/techniques', methods=['GET'])
def get_competences_techniques():
    try:
        cursor = mysql.connection.cursor()  # Création d'un curseur pour exécuter des requêtes SQL
        cursor.execute('SELECT * FROM competences_techniques')  # Exécution de la requête pour obtenir toutes les compétences techniques
        rows = cursor.fetchall()  # Récupération de tous les résultats
        cursor.close()  # Fermeture du curseur
        
        competences = [
            {
                'id': row[0],
                'nom': row[1],
                'type': row[2],
                'niveau': row[3],
                'description': row[4],
                'utilisation': row[5],
                'niveau_maitrise': row[6],
                'marge_progression': row[7],
                'importance_profil': row[8],
                'vitesse_acquisition': row[9],
                'conseils_experience': row[10],
                'objectif_moyen_terme': row[11],
                'formations_en_cours': row[12],
                'anecdotes': row[13],
                'cas_utilisation': row[14]
            } for row in rows
        ]
        
        return jsonify(competences), 200  # Réponse contenant la liste des compétences techniques avec le code HTTP 200 (OK)
    except Exception as e:
        return jsonify({'message': f'Erreur lors de la récupération des compétences techniques : {str(e)}'}), 500
        # Gestion des erreurs en cas d'échec de la récupération, avec le code HTTP 500 (Erreur interne du serveur)

@app.route('/api/competences/humaines', methods=['GET'])
def get_competences_humaines():
    try:
        cursor = mysql.connection.cursor()  # Création d'un curseur pour exécuter des requêtes SQL
        cursor.execute('SELECT * FROM competences_humaines')  # Exécution de la requête pour obtenir toutes les compétences humaines
        rows = cursor.fetchall()  # Récupération de tous les résultats
        cursor.close()  # Fermeture du curseur
        
        competences = [
            {
                'id': row[0],
                'nom': row[1],
                'type': row[2],
                'niveau': row[3],
                'description': row[4],
                'utilisation': row[5],
                'niveau_maitrise': row[6],
                'marge_progression': row[7],
                'importance_profil': row[8],
                'vitesse_acquisition': row[9],
                'conseils_experience': row[10],
                'objectif_moyen_terme': row[11],
                'formations_en_cours': row[12],
                'anecdotes': row[13],
                'cas_utilisation': row[14],
                'contexte_professionnel': row[15]
            } for row in rows
        ]
        
        return jsonify(competences), 200  # Réponse contenant la liste des compétences humaines avec le code HTTP 200 (OK)
    except Exception as e:
        return jsonify({'message': f'Erreur lors de la récupération des compétences humaines : {str(e)}'}), 500
        # Gestion des erreurs en cas d'échec de la récupération, avec le code HTTP 500 (Erreur interne du serveur)

@app.route('/api/projets', methods=['GET'])
def get_projets():
    try:
        cursor = mysql.connection.cursor()  # Création d'un curseur pour exécuter des requêtes SQL
        cursor.execute('SELECT * FROM projets')  # Exécution de la requête pour obtenir tous les projets
        rows = cursor.fetchall()  # Récupération de tous les résultats
        cursor.close()  # Fermeture du curseur
        
        projets = [
            {
                'id': row[0],
                'nom': row[1],
                'contexte': row[2],
                'description': row[3],
                'objectifs': row[4],
                'enjeux': row[5],
                'risques': row[6],
                'etapes': row[7],
                'acteurs': row[8],
                'resultats': row[9],
                'lendemains': row[10],
                'regardCritique': row[11],
                'competences': row[12]
            } for row in rows
        ]
        
        return jsonify(projets), 200  # Réponse contenant la liste des projets avec le code HTTP 200 (OK)
    except Exception as e:
        return jsonify({'message': f'Erreur lors de la récupération des projets : {str(e)}'}), 500
        # Gestion des erreurs en cas d'échec de la récupération, avec le code HTTP 500 (Erreur interne du serveur)

@app.route('/api/projets/<int:id>', methods=['GET'])
def get_projet_by_id(id):
    try:
        cursor = mysql.connection.cursor()  # Création d'un curseur pour exécuter des requêtes SQL
        cursor.execute('SELECT * FROM projets WHERE id = %s', (id,))  # Exécution de la requête pour obtenir un projet par son ID
        row = cursor.fetchone()  # Récupération du résultat (une seule ligne)
        cursor.close()  # Fermeture du curseur
        
        if row:
            projet = {
                'id': row[0],
                'nom': row[1],
                'contexte': row[2],
                'description': row[3],
                'objectifs': row[4],
                'enjeux': row[5],
                'risques': row[6],
                'etapes': row[7],
                'acteurs': row[8],
                'resultats': row[9],
                'lendemains': row[10],
                'regardCritique': row[11],
                'competences': row[12]
            }
            return jsonify(projet), 200  # Réponse contenant les détails du projet avec le code HTTP 200 (OK)
        else:
            return jsonify({'message': 'Projet non trouvé'}), 404
            # Réponse indiquant que le projet n'a pas été trouvé, avec le code HTTP 404 (Non trouvé)
    except Exception as e:
        return jsonify({'message': f'Erreur lors de la récupération du projet : {str(e)}'}), 500
        # Gestion des erreurs en cas d'échec de la récupération, avec le code HTTP 500 (Erreur interne du serveur)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
    # Lancement de l'application Flask en mode debug, écoutant sur toutes les interfaces réseau à port 5001
