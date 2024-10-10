import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_mysqldb import MySQL

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["https://portfolio-steve-duchateau.onrender.com", "http://localhost:8080"]}})  # Configuration CORS

# Configuration de la base de données MySQL
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST', 'junction.proxy.rlwy.net')  # hôte de la base de données
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER', 'root')  # utilisateur de la base de données
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD', 'sJZJplXzZTroxulYDRHPaaMhGDsSOKtu')  # mot de passe de la base de données
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB', 'railway')  # nom de la base de données
app.config['MYSQL_PORT'] = int(os.getenv('MYSQL_PORT', 43700))  # port de la base de données

mysql = MySQL(app)  # Création de l'objet MySQL pour interagir avec la base de données

@app.route('/', methods=['GET'])
def home():
    return "Bienvenue sur mon backend Flask !", 200

@app.route('/test-db', methods=['GET'])
def test_db():
    try:
        cursor = mysql.connection.cursor()  # Création d'un curseur pour exécuter des requêtes SQL
        cursor.execute('SELECT 1')  # Exécution d'une requête simple pour tester la connexion à la base de données
        cursor.close()  # Fermeture du curseur
        return "Connexion à la base de données MySQL réussie !", 200  # Réponse indiquant que la connexion est réussie
    except Exception as e:
        return jsonify({'error': f"Erreur de connexion à la base de données MySQL : {str(e)}"}), 500

@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.json  # Récupération des données JSON envoyées dans la requête POST
    first_name = data.get('first_Name')  # Vérifiez que les clés correspondent aux données envoyées
    last_name = data.get('last_Name')
    email = data.get('email')
    message = data.get('message')

    if not all([first_name, last_name, email, message]):
        return jsonify({'error': 'Tous les champs doivent être remplis.'}), 400

    try:
        cursor = mysql.connection.cursor()  # Création d'un curseur pour exécuter des requêtes SQL
        cursor.execute('INSERT INTO contact_messages (first_name, last_name, email, message) VALUES (%s, %s, %s, %s)',
                       (first_name, last_name, email, message))  # Insertion des données dans la table 'contact_messages'
        mysql.connection.commit()  # Validation des modifications dans la base de données
        cursor.close()  # Fermeture du curseur
        return jsonify({'message': 'Message enregistré avec succès'}), 200  # Réponse de succès
    except Exception as e:
        return jsonify({'error': f'Erreur lors de l\'enregistrement du message : {str(e)}'}), 500

@app.route('/api/competences/techniques', methods=['GET'])
def get_competences_techniques():
    try:
        cursor = mysql.connection.cursor()  # Création d'un curseur pour exécuter des requêtes SQL
        cursor.execute('SELECT * FROM competences_techniques')  # Exécution de la requête
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
        
        return jsonify(competences), 200  # Réponse contenant la liste des compétences techniques
    except Exception as e:
        return jsonify({'error': f'Erreur lors de la récupération des compétences techniques : {str(e)}'}), 500

@app.route('/api/competences/humaines', methods=['GET'])
def get_competences_humaines():
    try:
        cursor = mysql.connection.cursor()  # Création d'un curseur pour exécuter des requêtes SQL
        cursor.execute('SELECT * FROM competences_humaines')  # Exécution de la requête
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
        
        return jsonify(competences), 200  # Réponse contenant la liste des compétences humaines
    except Exception as e:
        return jsonify({'error': f'Erreur lors de la récupération des compétences humaines : {str(e)}'}), 500

@app.route('/api/projets', methods=['GET'])
def get_projets():
    try:
        cursor = mysql.connection.cursor()  # Création d'un curseur pour exécuter des requêtes SQL
        cursor.execute('SELECT * FROM projets')  # Exécution de la requête
        rows = cursor.fetchall()  # Récupération de tous les résultats
        cursor.close()  # Fermeture du curseur
        
        projets = []
        for row in rows:
            projet = {
                'id': int(row[0]) if isinstance(row[0], int) else 0,  # Validation que 'id' est un entier
                'nom': row[1] if row[1] is not None else '',  # Si la valeur est None, on retourne une chaîne vide
                'contexte': row[2] if row[2] is not None else '',
                'description': row[3] if row[3] is not None else '',
                'objectifs': row[4] if row[4] is not None else '',
                'enjeux': row[5] if row[5] is not None else '',
                'risques': row[6] if row[6] is not None else '',
                'etapes': row[7] if row[7] is not None else '',
                'acteurs': row[8] if row[8] is not None else '',
                'resultats': row[9] if row[9] is not None else '',
                'lendemains': row[10] if row[10] is not None else '',
                'regardCritique': row[11] if row[11] is not None else '',
                'competences': row[12] if row[12] is not None else ''
            }
            projets.append(projet)

        return jsonify(projets), 200  # Réponse contenant la liste des projets
    except Exception as e:
        return jsonify({'error': f'Erreur lors de la récupération des projets : {str(e)}'}), 500

@app.route('/api/projets/<int:id>', methods=['GET'])
def get_projet_by_id(id):
    try:
        cursor = mysql.connection.cursor()  # Création d'un curseur pour exécuter des requêtes SQL
        cursor.execute('SELECT * FROM projets WHERE id = %s', (id,))  # Exécution de la requête avec un paramètre
        row = cursor.fetchone()  # Récupération du résultat
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
            return jsonify(projet), 200  # Réponse contenant le projet recherché
        else:
            return jsonify({'error': 'Projet non trouvé.'}), 404  # Projet non trouvé
    except Exception as e:
        return jsonify({'error': f'Erreur lors de la récupération du projet : {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)  # Exécution de l'application Flask
