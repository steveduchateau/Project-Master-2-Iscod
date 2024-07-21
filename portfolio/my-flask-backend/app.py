# app.py
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_mysqldb import MySQL

app = Flask(__name__)
CORS(app)

# Configuration MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Asmara95370!'
app.config['MYSQL_DB'] = 'portfolio'

mysql = MySQL(app)

@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.json
    first_name = data.get('firstName')
    last_name = data.get('lastName')
    email = data.get('email')
    message = data.get('message')

    cursor = mysql.connection.cursor()
    cursor.execute('INSERT INTO contacts (first_name, last_name, email, message) VALUES (%s, %s, %s, %s)',
                   (first_name, last_name, email, message))
    mysql.connection.commit()
    cursor.close()

    return jsonify({'message': 'Message enregistré avec succès'}), 200


competences = [
    # Compétences techniques
    {
        "nom": "Python",
        "type": "technique",
        "niveau": "Intermédiaire",
        "description": "Langage de programmation puissant utilisé pour le développement web, scientifique,analyse de données etc.",
        "utilisation": "Développement d'outils d'automatisation de tâches et analyse de données",
        "cas_utilisation": [
            "Analyse de données",
            "Création de scripts d'automatisation"
        ],
        "contexte_professionnel": "Utilisé principalement dans le développement d'outils d'automatisations et de d'analyse de données.",
        "anecdotes": [
            {
                "titre": "Développement d'un outil d'analyse de données",
                "description": "J'ai développé un outil d'analyse de données avec Python pour automatiser les rapports des bénéficiaires que nous suivons.",
                "resultat": "Réduction du temps de génération des rapports de 50% et amélioration de la précision des données.",
                "lien_realisations": "http://example.com/realisations/outil-analyse"
            },
            {
                "titre": "Création d'outils automatiser",
                "description": "J'ai créé des outils pour automatiser des processus chronophages et lourds pour degager du temps aux salariés de ma BU.",
                "resultat": "Les outils ont permis  une  des erreurs et on soulager les salariés dans leurs tâches.",
                "lien_realisations": "http://example.com/realisations/api-client"
            }
        ],
        "niveau_maitrise": "Intermédiaire",
        "marge_progression": "Continue à se perfectionner dans les bibliothèques avancées et les meilleures pratiques.",
        "importance_profil": "Essentielle pour le développement et l'analyse de données.",
        "vitesse_acquisition": "Acquise rapidement grâce à des projets pratiques et des lectures ainsi que des vidéos",
        "conseils_experience": "Continuer à explorer les nouvelles bibliothèques et outils pour rester à jour avec les tendances actuelles.",
        "objectif_moyen_terme": "Maîtriser les technologies avancées telles que TensorFlow pour l'apprentissage automatique.",
        "formations_en_cours": "Aucune à ce jour"
    },
    {
        "nom": "Power BI",
        "type": "outil",
         "niveau": "Intermédiaire",
        "description": "Outil d'analyse et de visualisation de données permettant de créer des rapports interactifs et des tableaux de bord dynamiques.",
        "utilisation": "Analyse de données, création de rapports interactifs, visualisation et partage de données.",
        "cas_utilisation": [
        "Création de tableaux de bord pour le suivi des performances",
        "Analyse des tendances et des KPI à partir de sources multiples",
        "Consolidation des données de différents systèmes pour une vue unifiée"
    ],
    "contexte_professionnel": "Principalement utilisé pour la visualisation de données et l'analyse des performances de la BU.",
    "anecdotes": [
        {
            "titre": "Création d'un tableau de bord de performance",
            "description": "J'ai conçu un tableau de bord Power BI pour avoir une vision global sur la BU (performance,gestionn des entrées, nombre d'erreurs ect).",
            "resultat": "Amélioration de la prise de décision grâce à une vue claire des indicateurs clés de performance.",
            "lien_realisations": "http://example.com/realisations/tableau-de-bord-performance"
        },
    ],
    "niveau_maitrise": "Intermédiaire",
    "marge_progression": "Approfondir les compétences dans les fonctionnalités avancées de Power BI et l'intégration avec d'autres outils de BI.",
    "importance_profil": "Essentiel pour la création de rapports dynamiques et la prise de décisions basée sur les données.",
    "vitesse_acquisition": "Apprise assez rapidement notamenment à travers des projets de visualisation et des formations en ligne.",
    "conseils_experience": "Explorer les fonctionnalités avancées de Power BI et intégrer les meilleures pratiques de visualisation des données.",
    "objectif_moyen_terme": "Devenir expert en Power BI avec la capacité de créer des rapports et des tableaux de bord sophistiqués.",
    "formations_en_cours": "Aucune à ce jour"
}
,
    {
      "nom": "SQL",
     "type": "technique",
        "niveau": "Avancé",
        "description": "Langage de requête utilisé pour gérer, manipuler et interroger des bases de données relationnelles.",
        "utilisation": "Création, gestion et interrogation de bases de données, optimisation des requêtes et gestion des performances.",
        "cas_utilisation": [
        "Gestion de bases de données relationnelles",
        "Extraction et analyse des données pour des rapports et des décisions business"
    ],
    "contexte_professionnel": "Principalement utilisé dans la gestion des bases de données pour l'analyse de données et la génération de rapports.",
    "anecdotes": [

        {
            "titre": "Création de systèmes de reportings",
            "description": "J'ai conçu des systèmes de reporting avec SQL pour extraire et analyser des données .",
            "resultat": "Production de rapports détaillés permettant une prise de décision plus éclairée pour l'équipe de direction.",
            "lien_realisations": "http://example.com/realisations/reporting"
        }
    ],
    "niveau_maitrise": "Débutant",
    "marge_progression": "Affiner les compétences en optimisation avancée et en gestion de grandes bases de données.",
    "importance_profil": "Cruciale pour la gestion efficace des données et la création de solutions d'analyse robustes.",
    "vitesse_acquisition": "Apprise principalement à travers des projets concrets et des besoins professionnels spécifiques.",
    "conseils_experience": "Se concentrer sur les techniques d'optimisation avancées et la gestion de bases de données complexes.",
    "objectif_moyen_terme": "Devenir un expert en gestion de bases de données avec des compétences avancées en optimisation et en analyse.",
    "formations_en_cours": "Aucune à ce jour"  
    },
  {
    "nom": "Microsoft 365 Office",
    "type": "outil",
    "niveau": "Intermédiaire",
    "description": "Suite bureautique intégrée offrant des outils pour la gestion des données, la création de documents, et la collaboration.",
    "utilisation": "Création de documents, gestion des données, automatisation des tâches, collaboration en temps réel.",
    "cas_utilisation": [
        "Création de tableaux de reporting avec Excel",
        "Automatisation de l'envoi de mails avec Outlook",
        "Automatisation de tableaux de bord sur Excel"
    ],
    "contexte_professionnel": "Utilisé pour la gestion des données, la communication et la création de rapports dans divers environnements professionnels.",
    "anecdotes": [
        {
            "titre": "Création d'un tableau de reporting avec Excel",
            "description": "Je créé des tableaux de reporting avec Excel ",
            "resultat": "Les rapports sont précis et pemerttent d'aller plus loins dans l'analyse, ce qui a réduit le temps de préparation des rapports.",
            "lien_realisations": "http://example.com/realisations/reporting-excel"
        },
        {
            "titre": "Automatisation de l'envoi de mails",
            "description": "J'ai mis en place une automatisation pour l'envoi de mails réguliers avec Outlook à l'aide de macros.",
            "resultat": "Réduction du temps consacré à l'envoi de communications répétitives et amélioration de l'efficacité.",
            "lien_realisations": "http://example.com/realisations/automatisation-mails"
        },
        {
            "titre": "Automatisation d'un tableau de bord sur Excel",
            "description": "J'ai développé un tableau de bord interactif sur Excel avec des macros pour l'analyse des données.",
            "resultat": "Le tableau de bord se met à jour automatiquement, facilitant l'analyse des données en temps réel.",
            "lien_realisations": "http://example.com/realisations/dashboard-excel"
        }
    ],
    "niveau_maitrise": "Intermédiaire",
    "marge_progression": "Approfondir les compétences dans l'automatisation avancée et l'intégration avec d'autres outils Microsoft 365.",
    "importance_profil": "Essentiel pour l'efficacité dans la gestion des données, la création de rapports et la communication.",
    "vitesse_acquisition": "Apprise progressivement à travers des projets pratiques et des formations en ligne.",
    "conseils_experience": "Expérimenter avec des fonctionnalités avancées d'Excel et des outils d'automatisation pour maximiser l'efficacité.",
    "objectif_moyen_terme": "Devenir expert dans l'utilisation avancée des outils de Microsoft 365 et optimiser les processus de gestion des données.",
    "formations_en_cours": "Formation avancée en automatisation avec Excel prévue pour le mois prochain."
},

    # Compétences humaines
    {
        "nom": "Communication",
        "type": "humaine",
        "niveau": "intermédiaire",
        "description": "Capacité à transmettre des informations de manière claire et efficace, tant à l'oral qu'à l'écrit.",
        "utilisation": "Présentations, réunions d'équipe, rédaction de rapports, communication interpersonnelle.",
        "cas_utilisation": [
            "Présentations de projets aux parties prenantes",
            "Rédaction de documentation technique",
            "Communication efficace avec les membres de l'équipe"
        ],
        "contexte_professionnel": "Essentielle dans la gestion de projets et les interactions quotidiennes au sein de l'équipe.",
        "anecdotes": [
            {
                "titre": "Présentation de mes rapports aux équipes",
                "description": "J'ai présenté mes rapports à différents acteurs de mon entreprise (directeur de projets, responsables; consultants, assitants).",
                "resultat": "Adoption des rapports par la direction.",
                "lien_realisations": "http://example.com/realisations/presentation-strategique"
            },
            {
                "titre": "Rédaction d'un manuel utilisateur",
                "description": "J'ai rédigé un manuel utilisateur détaillé pour l'utilisation de mes dahsboards en interne.",
                "resultat": "Amélioration de l'adoption de l'application et réduction des demandes de support technique.",
                "lien_realisations": "http://example.com/realisations/manuel-utilisateur"
            }
        ],
        "niveau_maitrise": "Avancé",
        "marge_progression": "Perfectionner les techniques de présentation et de rédaction professionnelle.",
        "importance_profil": "Indispensable pour la gestion des projets et la coordination avec les parties prenantes.",
        "vitesse_acquisition": "Acquise rapidement grâce à des expériences variées et des formations en communication.",
        "conseils_experience": "Se concentrer sur l'écoute active et la clarté de l'expression pour améliorer les interactions professionnelles.",
        "objectif_moyen_terme": "Maîtriser les techniques avancées de présentation et de communication interculturelle.",
        "formations_en_cours": "Formation en techniques de présentation avancées prévue pour le semestre prochain."
    },
    {
    "nom": "Interprétation des Résultats",
    "type": "humaine",
    "niveau": "Intermédiaire",
    "description": "Capacité à interpréter les résultats d'analyse de données et à tirer des conclusions pertinentes pour orienter la prise de décision.",
    "utilisation": "Analyse des résultats, identification des tendances, présentation des conclusions aux parties prenantes.",
    "cas_utilisation": [
        "Analyse des résultats",
        "Identification des tendances dans des ensembles de données volumineux pour orienter les décisions stratégiques",
        "Présentation des conclusions d'analyse à l'équipe pour influencer la direction sur les décisions"
    ],
    "contexte_professionnel": "Essentiel pour transformer les données brutes en informations exploitables qui soutiennent les décisions business et stratégiques.",
    "anecdotes": [
        {
            "titre": "Interprétation des tendances sur les livrables",
            "description": "J'ai analysé les données sur les livrables  les tendances et des opportunités ainsi que les erreurs sur les livrables.",
            "resultat": "Les insights obtenus ont permis à la directrice de projets de mettres en place des stratégies ciblées pour améliorer les livrables.",
            "lien_realisations": "http://example.com/realisations/tendances-vente"
        },
        {
            "titre": "Évaluation des performances des équipes",
            "description": "J'ai interprété les données de performance des équipes ",
            "resultat": "Les conclusions ont permis d'ajuster le fonctionnement et de planifier des initiatives futures basées sur les performances observées.",
            "lien_realisations": "http://example.com/realisations/evaluation-campagne"
        }
    ],
    "niveau_maitrise": "Intermédiaire",
    "marge_progression": "Approfondir les compétences en interprétation de données complexes et en formulation de recommandations stratégiques.",
    "importance_profil": "Cruciale pour transformer les analyses en actions concrètes et éclairer les décisions importantes.",
    "vitesse_acquisition": "Apprise progressivement à travers des projets d'analyse de données et des discussions avec les parties prenantes.",
    "conseils_experience": "Se concentrer sur l'amélioration des compétences en storytelling avec les données et en analyse approfondie.",
    "objectif_moyen_terme": "Devenir expert en interprétation des résultats d'analyse avec une capacité à fournir des recommandations stratégiques précises.",
    "formations_en_cours": "Formation en interprétation avancée des données et en prise de décision basée sur les données prévue pour le mois prochain."
},

    {
        "nom": "Gestion du temps",
        "type": "humaine",
        "niveau": "Avancé",
        "description": "Capacité à planifier et à gérer efficacement son temps et celui de l'équipe pour atteindre les objectifs.",
        "utilisation": "Priorisation des tâches, gestion des délais, planification de projets.",
        "cas_utilisation": [
            "Planification de projets complexes",
            "Gestion de multiples tâches concurrentes",
            "Optimisation des processus de travail"
        ],
        "contexte_professionnel": "Essentielle pour la réussite des projets et l'efficacité individuelle et collective.",
        "anecdotes": [
            {
                "titre": "Planification des outils",
                "description": "Je  planifie et gére la créations de mes outils avec pour objectifs délais serrés et en priorisant les tâches critiques.",
                "resultat": "Livraison des projets dans les délais",
                "lien_realisations": "http://example.com/realisations/planification-projet"
            },
            {
                "titre": "Optimisation des processus de travail",
                "description": "J'ai optimisé les processus de travail pour réduire les délais et améliorer l'efficacité.",
                "resultat": "Augmentation de la productivité de l'équipe de 30% et réduction des délais de livraison.",
                "lien_realisations": "http://example.com/realisations/optimisation-processus"
            }
        ],
        "niveau_maitrise": "Avancé",
        "marge_progression": "Perfectionner les techniques de gestion du temps et d'optimisation des processus.",
        "importance_profil": "Indispensable pour la réussite des projets et la gestion efficace des ressources.",
        "vitesse_acquisition": "Acquise rapidement grâce à des expériences de gestion de projets et des formations spécifiques.",
        "conseils_experience": "Se concentrer sur la planification proactive et l'optimisation continue des processus de travail.",
        "objectif_moyen_terme": "Maîtriser les outils avancés de gestion du temps et de planification de projets.",
        "formations_en_cours": "Formation en gestion du temps et productivité personnelle prévue pour le mois prochain."
    },
    {
        "nom": "Esprit d\'équipe",
        "type": "humaine",
        "niveau": "Avancé",
        "description": "Capacité à travailler efficacement au sein d'une équipe, en favorisant la collaboration et l'entraide.",
        "utilisation": "Travail en équipe, collaboration interdisciplinaire, soutien mutuel.",
        "cas_utilisation": [
            "Collaboration sur des projets transversaux",
            "Soutien aux membres de l'équipe",
            "Participation active aux réunions et aux ateliers"
        ],
        "contexte_professionnel": "Crucial pour la réussite collective et la cohésion de l'équipe.",
        "anecdotes": [
            {
                "titre": "Collaboration sur un projet transversal",
                "description": "J'ai collaboré avec différentes équipes pour mener à bien un projet transversal .",
                "resultat": "Réussite du projet grâce à une collaboration efficace et à une communication ouverte.",
                "lien_realisations": "http://example.com/realisations/projet-transversal"
            },
            {
              "titre": "Formation d'un collègue sur les outils d'analyse",
            "description": "J'ai formé un collègue sur l'utilisation des outils d'analyse de données et des techniques de visualisation.",
            "resultat": "Le collègue a rapidement acquis les compétences nécessaires pour gérer ses propres projets d'analyse, améliorant ainsi l'efficacité globale de l'équipe.",
            "lien_realisations": "http://example.com/realisations/formation-outils-analyse" 
            }
        ],
        "niveau_maitrise": "Avancé",
        "marge_progression": "Encourager davantage la collaboration et l'entraide au sein de l'équipe.",
        "importance_profil": "Indispensable pour la cohésion et la performance de l'équipe.",
        "vitesse_acquisition": "Acquise rapidement grâce à des expériences de travail en équipe variées et des formations en leadership.",
        "conseils_experience": "Favoriser un environnement de travail collaboratif et ouvert pour renforcer l'esprit d'équipe.",
        "objectif_moyen_terme": "Devenir un modèle de collaboration et de soutien au sein de l'équipe.",
        "formations_en_cours": "Formation en dynamique d'équipe et collaboration prévue pour le semestre prochain."
    }
]


projets = [
    {
        "nom": "Gestionnaire de contatct",
        "description": "",
        "objectifs": "",
        "contexte": "",
        "enjeux": "",
        "risques": "",
        "etapes": "",
        "acteurs": "",
        "resultats": "",
        "lendemains": "",
        "regardCritique": "",
        "competences": [""]
    },
    {
        "nom": "Automatisation de power point",
        "description": "",
        "objectifs": "",
        "contexte": "",
        "enjeux": "",
        "risques": "",
        "etapes": "",
        "acteurs": "",
        "resultats": "",
        "lendemains": "",
        "regardCritique": "",
        "competences": [""]
    },
    {
        "nom": "outil de scrapping",
        "description": "",
        "objectifs": "",
        "contexte": "",
        "enjeux": "",
        "risques": "",
        "etapes": "",
        "acteurs": "",
        "resultats": "",
        "lendemains": "",
        "regardCritique": "",
        "competences": [""]
    },
    {
        "nom": "Gestionnaire d'evenements ",
        "description": "",
        "objectifs": "",
        "contexte": "",
        "enjeux": "",
        "risques": "",
        "etapes": "",
        "acteurs": "",
        "resultats": "",
        "lendemains": "",
        "regardCritique": "",
        "competences": [""]
    },
    {
        "nom": "Gestionnaire de nouveaux candidat",
        "description": "",
        "objectifs": "",
        "contexte": "",
        "enjeux": "",
        "risques": "",
        "etapes": "",
        "acteurs": "",
        "resultats": "",
        "lendemains": "",
        "regardCritique": "",
        "competences": [""]
    }
]


@app.route('/api/competences', methods=['GET'])
def get_competences():
    return jsonify(competences)

@app.route('/api/projets', methods=['GET'])
def get_projets():
    return jsonify(projets)


if __name__ == '__main__':
    app.run(debug=True)