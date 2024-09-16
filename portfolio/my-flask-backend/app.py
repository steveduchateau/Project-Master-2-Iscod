import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_mysqldb import MySQL

app = Flask(__name__)
CORS(app)

# Configuration de la base de données MySQL
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST', 'localhost')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER', 'root')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD', 'steve')  
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB', 'Portfolio')

mysql = MySQL(app)

@app.route('/', methods=['GET'])
def home():
    return "Bienvenue sur mon backend Flask !", 200

@app.route('/test-db', methods=['GET'])
def test_db():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT 1')  # Simple requête pour tester la connexion
        cursor.close()
        return "Connexion à la base de données MySQL réussie !", 200
    except Exception as e:
        return f"Erreur de connexion à la base de données MySQL : {str(e)}", 500

@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.json
    first_name = data.get('firstName')
    last_name = data.get('lastName')
    email = data.get('email')
    message = data.get('message')

    try:
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO contact_messages (first_name, last_name, email, message) VALUES (%s, %s, %s, %s)',
                       (first_name, last_name, email, message))
        mysql.connection.commit()
        cursor.close()
        return jsonify({'message': 'Message enregistré avec succès'}), 200
    except Exception as e:
        return jsonify({'message': f'Erreur lors de l\'enregistrement du message : {str(e)}'}), 500

@app.route('/api/competences/techniques', methods=['GET'])
def get_competences_techniques():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM competences_techniques')
        rows = cursor.fetchall()
        cursor.close()
        
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
        
        response = jsonify(competences)
        response.headers.add('Content-Type', 'application/json; charset=utf-8')
        return response
    except Exception as e:
        return jsonify({'message': f'Erreur lors de la récupération des compétences techniques : {str(e)}'}), 500

@app.route('/api/competences/humaines', methods=['GET'])
def get_competences_humaines():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM competences_humaines')
        rows = cursor.fetchall()
        cursor.close()
        
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
        
        response = jsonify(competences)
        response.headers.add('Content-Type', 'application/json; charset=utf-8')
        return response
    except Exception as e:
        return jsonify({'message': f'Erreur lors de la récupération des compétences humaines : {str(e)}'}), 500

@app.route('/api/projets', methods=['GET'])
def get_projets():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM projets')
        rows = cursor.fetchall()
        cursor.close()
        
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
        
        response = jsonify(projets)
        response.headers.add('Content-Type', 'application/json; charset=utf-8')
        return response
    except Exception as e:
        return jsonify({'message': f'Erreur lors de la récupération des projets : {str(e)}'}), 500

@app.route('/api/projets/<int:id>', methods=['GET'])
def get_projet_by_id(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM projets WHERE id = %s', (id,))
        row = cursor.fetchone()
        cursor.close()
        
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
            response = jsonify(projet)
            response.headers.add('Content-Type', 'application/json; charset=utf-8')
            return response
        else:
            return jsonify({'message': 'Projet non trouvé'}), 404
    except Exception as e:
        return jsonify({'message': f'Erreur lors de la récupération du projet : {str(e)}'}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
