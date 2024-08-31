import unittest
from flask import Flask, jsonify, request
from flask_testing import TestCase

# Exemple de configuration de l'application Flask pour les tests
app = Flask(__name__)

# Configuration des routes de l'application pour les tests
@app.route('/api/competences', methods=['GET'])
def get_competences():
    return jsonify(["Développement web", "Gestion de base de données", "Python", "Automatisation"])

@app.route('/api/projets', methods=['GET'])
def get_projets():
    return jsonify([{"id": "1", "nom": "Gestionnaire de contact"}])

@app.route('/api/projets/<id>', methods=['GET'])
def get_projet(id):
    if id == "1":
        return jsonify({"id": "1", "nom": "Gestionnaire de contact"})
    else:
        return jsonify({"message": "Projet non trouvé"}), 404

class TestApp(TestCase):
    def create_app(self):
        # Configure l'application pour les tests
        app.config['TESTING'] = True
        return app

    def test_get_competences(self):
        response = self.client.get('/api/competences')
        self.assert200(response)  # Vérifie que la réponse a le statut 200
        self.assertEqual(response.json, ["Développement web", "Gestion de base de données", "Python", "Automatisation"])

    def test_get_projets(self):
        response = self.client.get('/api/projets')
        self.assert200(response)  # Vérifie que la réponse a le statut 200
        self.assertTrue(len(response.json) > 0)  # Vérifie qu'il y a des projets dans la réponse

    def test_get_projet(self):
        response = self.client.get('/api/projets/1')
        self.assert200(response)  # Vérifie que la réponse a le statut 200
        self.assertEqual(response.json['id'], '1')
        self.assertEqual(response.json['nom'], 'Gestionnaire de contact')

    def test_get_projet_not_found(self):
        response = self.client.get('/api/projets/999')
        self.assert404(response)  # Vérifie que la réponse a le statut 404
        self.assertEqual(response.json, {'message': 'Projet non trouvé'})

if __name__ == '__main__':
    unittest.main()
