import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_mysqldb import MySQL

app = Flask(__name__)
CORS(app)

# Configuration MySQL
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST', 'db')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER', 'root')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD', 'steve')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB', 'Portfolio')

mysql = MySQL(app)

@app.route('/test-db', methods=['GET'])
def test_db():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT 1')  # Simple requête pour tester la connexion
        cursor.close()
        return "Connexion à la base de données MySQL réussie !", 200
    except Exception as e:
        return f"Erreur de connexion à la base de données MySQL : {str(e)}", 500

@app.route('/', methods=['GET'])
def home():
    return "Bienvenue sur mon backend Flask !", 200

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

if __name__ == "__main__":
    app.run(debug=False)


competences = [
    # Compétences techniques
    {
        "nom": "Python",
        "type": "technique",
        "niveau": "Junior",
        "description": "Python est un langage de programmation extrêmement puissant et polyvalent. Je l'utilise principalement pour développer des outils d'automatisation de tâches et pour l'analyse de données. Sa syntaxe claire et sa vaste bibliothèque standard en font un choix idéal pour de nombreux types de projets, qu'il s'agisse de développement web, d'analyse scientifique, ou encore de prototypage d'applications.",
        "utilisation": "Dans mon travail, Python me permet de créer des scripts efficaces qui automatisent des tâches répétitives et complexes, améliorant ainsi l'efficacité et la précision des processus. Je l'utilise également pour manipuler, analyser et visualiser des données, ce qui est essentiel pour extraire des insights significatifs et orienter les décisions stratégiques de l'entreprise.",
        "cas_utilisation": [
            "Analyse de données",
            "Création de scripts d'automatisation"
        ],
        "contexte_professionnel": "J'ai développé ma compétence en Python en l'intégrant directement dans mon travail quotidien, principalement pour le développement d'outils d'automatisation et d'analyse de données. Dans mon rôle actuel, cette compétence est cruciale car elle me permet de répondre aux besoins croissants de l'entreprise en matière d'efficacité opérationnelle et de précision dans les analyses. Avec l'émergence de la science des données comme une discipline clé dans de nombreuses industries, j'ai compris l'importance d'affiner et d'élargir mes connaissances en Python pour rester pertinent et apporter une réelle valeur ajoutée à mon entreprise.",
        "anecdotes": [
            {
                "titre": "Gestionnaire de nouveaux candidats",
                "description": "J'ai développé un outil multifonctionnel capable de gérer plusieurs étapes du traitement des candidatures : téléchargement et comparaison de fichiers, scraping d'informations à partir d'un site web, intégration des données dans un tableau Excel, et mise en forme du fichier final. Cet outil vise à automatiser et optimiser la gestion des nouveaux candidats pour le reporting annuel du consultant, simplifiant ainsi un processus autrefois manuel et chronophage.",
                "resultat": "L'outil a permis une réduction du temps de traitement des candidatures de 80%, ce qui a entraîné une amélioration notable de la satisfaction du consultant, une diminution des erreurs. Et La productivité globale a également été augmentée grâce à l'automatisation du processus.",
                "lien_realisations": "http://localhost:4200/projets/5",
                "lien_Git_Hub:":"https://github.com/steveduchateau?tab=repositories",
            },
            {
                "titre": "Outil de Scraping pour le Reporting",
                "description": " J'ai développé un outil de scraping qui extrait automatiquement des données spécifiques depuis un site web pour le reporting de la Business Unit.",
                "resultat": "Ce projet a réduit le temps de collecte des données d'une semaine à 5 heures, avec une précision accrue.",
                "lien_realisations": "http://localhost:4200/projets/3",
                "lien_Git_Hub:":"https://github.com/steveduchateau?tab=repositories",
            }
        ],
        "niveau_maitrise": "Je me situe à un niveau dit junior en Python. Je suis à l'aise avec les concepts de base, comme la manipulation de données, le développement de scripts d'automatisation, et la création de prototypes. Cependant, je reconnais qu'il reste des domaines dans lesquels je peux encore progresser, notamment en ce qui concerne l'utilisation de bibliothèques plus spécialisées et les meilleures pratiques pour la gestion de projets plus complexes.",
        "marge_progression": "Bien que j'ai acquis des bases sur Python, je suis conscient qu'il y a toujours une marge de progression. J'ai l'intention de continuer à me perfectionner, notamment en explorant des technologies avancées comme TensorFlow pour l'apprentissage automatique. Je souhaite également approfondir mes connaissances sur les frameworks Python pour le développement d'applications robustes et scalables. Cela me permettra de participer à des projets encore plus ambitieux et de contribuer davantage aux objectifs stratégiques de mon entreprise.",
        "importance_profil": "Python est une compétence centrale dans mon profil professionnel. Elle est directement liée à mes responsabilités actuelles, en particulier dans le développement et l'optimisation des processus d'analyse de données et d'automatisation. Cette compétence est non seulement essentielle pour mon rôle actuel, mais elle est également cruciale pour mon développement professionnel futur. Elle me permet de rester à la pointe des évolutions technologiques dans mon domaine et de continuer à apporter une valeur ajoutée significative à l'entreprise.",
        "vitesse_acquisition": "J'ai acquis cette compétence rapidement grâce à une approche axée sur l'apprentissage par la pratique. J'ai commencé par des projets concrets, qui m'ont permis de consolider mes connaissances théoriques en les appliquant à des problèmes réels. L'accessibilité de Python et la richesse des ressources disponibles en ligne ont grandement facilité cet apprentissage. En peu de temps, j'ai pu maîtriser les concepts essentiels et les appliquer avec succès dans divers projets professionnels.",
        "conseils_experience": "Avec le recul, je conseille à quiconque souhaite maîtriser Python de ne jamais se limiter aux concepts de base. Il est important d'explorer constamment de nouvelles bibliothèques et outils, car le langage évolue rapidement et de nouvelles solutions émergent régulièrement. Travailler sur des projets concrets est également essentiel pour développer une compréhension approfondie de Python. De plus, rester informé des tendances actuelles et des meilleures pratiques dans le domaine est crucial pour maintenir un niveau de compétence élevé et pertinent.",
        "objectif_moyen_terme": "À moyen terme, mon objectif est de maîtriser des technologies avancées telles que TensorFlow, qui me permettront de me spécialiser dans l'apprentissage automatique. Je souhaite également approfondir mes compétences en développement d'applications Python complexes et robustes, afin de participer à des projets de plus grande envergure, notamment dans le domaine de l'intelligence artificielle et de la science des données.",
        "formations_en_cours": "À ce jour, je n'ai pas de formation spécifique en cours sur Python, mais je prévois de suivre des cours spécialisés sur TensorFlow et d'autres technologies émergentes dans un avenir proche. Je suis également en auto-formation continue, en m'informant régulièrement sur les nouvelles bibliothèques et en testant de nouvelles approches dans mes projets actuels."
    },
    {
        "nom": "Power BI",
        "type": "technique",
         "niveau": "Intermédiaire",
        "description": "Power BI est un outil d'analyse et de visualisation de données permettant de créer des rapports interactifs et des tableaux de bord dynamiques. Il offre une interface intuitive pour transformer des données brutes en insights exploitables, facilitant ainsi la prise de décision informée.",
        "utilisation": "Dans mon travail, j'utilise Power BI pour analyser des données provenant de multiples sources, créer des rapports interactifs, et partager ces visualisations avec les parties prenantes. Cet outil est essentiel pour suivre les performances de la Business Unit (BU), consolider des données disparates, et fournir une vue d'ensemble unifiée des indicateurs clés de performance (KPI).",
        "cas_utilisation": [
        "Création de tableaux de bord pour le suivi des performances",
        "Consolidation des données de différents systèmes pour une vue unifiée"
    ],
    "contexte_professionnel": "Power BI est un outil central dans mon rôle actuel. Je l'utilise principalement pour la visualisation des données et l'analyse des performances. Il me permet de fournir des insights clairs et pertinents qui aident à orienter les décisions stratégiques au sein de la BU. En consolidant des données provenant de divers systèmes, je peux offrir une perspective unifiée et améliorer la compréhension des performances globales de l'entreprise.",
    "anecdotes": [
        {
            "titre": "Création d'un tableau de bord de performance",
            "description": "J'ai développé un tableau de bord Power BI pour fournir une vision globale de la performance de la BU. Ce tableau de bord inclut des indicateurs comme la gestion des entrées, le suivi des erreurs, et d'autres KPI essentiels. Grâce à cette visualisation, les décideurs ont pu accéder rapidement et facilement aux informations critiques, améliorant ainsi la réactivité et la précision des décisions.",
            "resultat": "Amélioration de la prise de décision grâce à une vue claire des indicateurs clés de performance.",
        },
    ],
    "niveau_maitrise": "Intermédiaire",
    "marge_progression": "Je me situe à un niveau intermédiaire en Power BI. Je suis à l'aise avec les fonctionnalités de base et avancées, telles que la création de tableaux de bord, la modélisation de données, et l'intégration avec d'autres outils de Business Intelligence. Toutefois, je reconnais qu'il y a encore des domaines, comme l'utilisation avancée de DAX (Data Analysis Expressions), où je peux progresser.",
    "importance_profil": "Bien que je maîtrise bien Power BI, je vois encore des opportunités pour approfondir mes connaissances, notamment dans l'utilisation de fonctionnalités avancées, comme les expressions DAX et l'intégration avec d'autres outils de BI. Mon objectif est d'utiliser ces compétences pour créer des analyses encore plus sophistiquées et maximiser l'efficacité des processus décisionnels.",
    "vitesse_acquisition": "J'ai acquis cette compétence rapidement grâce à une approche pratique, en travaillant sur des projets concrets de visualisation et en suivant des formations en ligne. L'accessibilité de Power BI et la richesse des ressources disponibles m'ont permis de maîtriser rapidement les concepts clés et de les appliquer efficacement dans mon travail.",
    "conseils_experience": "Je conseille à quiconque souhaite maîtriser Power BI d'explorer continuellement ses fonctionnalités avancées, comme DAX, et de rester informé des meilleures pratiques de visualisation des données. Travailler sur des projets réels et rester à jour avec les nouvelles fonctionnalités est crucial pour tirer le meilleur parti de cet outil.",
    "objectif_moyen_terme": "À moyen terme, je vise à devenir un expert en Power BI, capable de créer des rapports et des tableaux de bord sophistiqués. Je souhaite également approfondir mes compétences en DAX et explorer les possibilités d'intégration avec d'autres outils de BI pour maximiser l'efficacité des analyses de données.",
    "formations_en_cours": "À ce jour, je n'ai pas de formation spécifique en cours sur Power BI, mais je prévois de suivre des cours spécialisés sur DAX et les fonctionnalités avancées de Power BI. Je m'engage également dans une auto-formation continue en explorant de nouvelles fonctionnalités et en mettant en pratique les meilleures approches dans mes projets actuels"
}
,
    {
      "nom": "SQL",
     "type": "technique",
        "niveau": "Junior",
        "description": "SQL (Structured Query Language) est un langage de requête essentiel pour la gestion, la manipulation, et l'interrogation des bases de données relationnelles. Il me permet de créer et de gérer des bases de données, ainsi que d'extraire des données pour les analyser et générer des rapports pertinents.",
        "utilisation": "Dans mon travail, SQL est utilisé pour créer et gérer des bases de données relationnelles, optimiser les requêtes pour améliorer les performances, et gérer les données nécessaires à l'analyse et à la prise de décision. Cet outil est essentiel pour structurer les informations de manière efficace et pour fournir des insights critiques via des rapports détaillés.",
        "cas_utilisation": [
        "Gestion de bases de données relationnelles",
        "Extraction et analyse des données pour des rapports et des décisions business"
    ],
    "contexte_professionnel": "SQL est principalement utilisé dans la gestion des bases de données pour l'analyse des données et la génération de rapports. Dans mon rôle, il me permet de structurer et d'extraire des informations de manière efficace, facilitant ainsi la prise de décisions basées sur des données précises et actualisées.",
    "anecdotes": [

        {
            "titre": "Création de systèmes de reportings",
            "description": "J'ai conçu des systèmes de reporting en SQL pour extraire et analyser des données critiques. Ces systèmes ont permis de générer des rapports détaillés qui ont facilité une prise de décision plus éclairée pour l'équipe de direction.",
            "resultat": "Production de rapports précis qui ont amélioré la capacité de l'équipe de direction à prendre des décisions basées sur des données fiables.",
        }
    ],
    "niveau_maitrise": "Je me situe à un niveau junior en SQL. Je suis à l'aise avec les requêtes de base, la gestion des données, et la création de rapports simples. Cependant, il me reste à approfondir mes compétences dans l'optimisation avancée des requêtes et la gestion de grandes bases de données pour maximiser l'efficacité des opérations.",
    "marge_progression": "Bien que je maîtrise les aspects fondamentaux de SQL, je souhaite affiner mes compétences, notamment en optimisation avancée et en gestion de grandes bases de données. Mon objectif est de développer une expertise plus approfondie dans l'analyse des performances des bases de données et la gestion efficace des données complexes.",
    "importance_profil": "SQL est crucial pour la gestion efficace des données et la création de solutions d'analyse robustes. Cette compétence est essentielle dans mon rôle pour structurer, interroger, et analyser les données nécessaires à la prise de décisions stratégiques.",
    "vitesse_acquisition": "J'ai acquis cette compétence principalement à travers des projets concrets et des besoins professionnels spécifiques. Travailler directement avec des bases de données et résoudre des problèmes réels a été fondamental pour maîtriser les concepts de SQL.",
    "conseils_experience": "Pour maîtriser SQL, il est important de se concentrer non seulement sur les requêtes de base mais aussi sur les techniques d'optimisation avancées et la gestion de bases de données complexes. Travailler sur des projets réels et comprendre les meilleures pratiques pour structurer et interroger les données est crucial pour progresser dans ce domaine.",
    "objectif_moyen_terme": "À moyen terme, mon objectif est de devenir un expert en gestion de bases de données, avec des compétences avancées en optimisation des requêtes et en analyse de grandes bases de données. Je souhaite également approfondir mes connaissances pour créer des solutions d'analyse plus sophistiquées et efficaces.",
    "formations_en_cours": "À ce jour, je n'ai pas de formation spécifique en cours sur SQL, mais je prévois de suivre des formations et des cours spécialisés pour améliorer mes compétences en optimisation avancée et en gestion des bases de données."  
    },
  {
    "nom": "Office 365",
    "type": "technique",
    "niveau": "Intermédiaire",
    "description": "Office 365 est une suite bureautique intégrée qui offre une gamme d'outils pour la gestion des données, la création de documents, et la collaboration en temps réel. Elle comprend des applications telles que Word, Excel, PowerPoint, Outlook, et OneDrive, permettant une gestion efficace des tâches quotidiennes et la communication au sein de l'entreprise.",
    "utilisation": "Dans mon travail, Office 365 est utilisé pour créer des documents professionnels, gérer des données complexes, automatiser des tâches récurrentes, et collaborer en temps réel avec mes collègues. Cela inclut la création de rapports détaillés, l'automatisation des processus via Excel et Outlook, et la gestion des communications et des documents partagés.",
    "cas_utilisation": [
        "Création de tableaux de reporting avec Excel",
        "Automatisation de l'envoi de mails avec Outlook",
    ],
    "contexte_professionnel": "Dans mon rôle actuel, Office 365 est essentiel pour optimiser la gestion des données et la création de rapports. J'utilise Excel pour concevoir des tableaux de reporting et des tableaux de bord qui facilitent la visualisation des performances et des indicateurs clés. Outlook est utilisé pour automatiser l'envoi de communications régulières, ce qui permet de gagner du temps et d'améliorer l'efficacité de la gestion des courriels. L'intégration de ces outils contribue à une meilleure organisation des informations, à la réduction des tâches manuelles et à une collaboration plus fluide au sein de l'équipe.",
    "anecdotes": [
        {
            "titre": "Création d'un tableau de reporting avec Excel",
            "description": "J'ai conçu des tableaux de reporting avancés avec Excel pour suivre les performances de l'entreprise. Ces tableaux ont permis une analyse plus approfondie et ont réduit le temps de préparation des rapports.",
            "resultat": "Les rapports sont plus précis et offrent des insights plus détaillés, ce qui a significativement diminué le temps nécessaire pour leur préparation.",
            
        },
        {
            "titre": "Automatisation de l'envoi de mails",
            "description": "J'ai mis en place une automatisation pour l'envoi de mails réguliers via Outlook, en utilisant des macros.",
            "resultat": " Cela a réduit le temps consacré aux communications répétitives et a amélioré l'efficacité de la gestion des courriels.",
         
        },

    ],
    "niveau_maitrise": "Je possède un niveau intermédiaire en Office 365. Je suis compétent dans l'utilisation de ses principales fonctionnalités pour la création de documents, la gestion des données, et l'automatisation des tâches. Toutefois, je cherche à approfondir mes compétences, notamment en automatisation avancée et en intégration avec d'autres outils Microsoft 365.",
    "marge_progression": "Je souhaite approfondir mes compétences en automatisation avancée et explorer l'intégration d'Office 365 avec d'autres outils Microsoft pour optimiser les processus de gestion des données et améliorer l'efficacité des workflows.",
    "importance_profil": "Office 365 est crucial pour mon efficacité professionnelle, car il soutient la gestion des données, la création de rapports, et la communication. Cette compétence me permet d'améliorer la productivité et de collaborer efficacement au sein de mon équipe.",
    "vitesse_acquisition": "J'ai acquis cette compétence progressivement grâce à des projets pratiques et des formations en ligne. L'utilisation régulière des outils et l'expérimentation avec des fonctionnalités avancées ont été clés pour maîtriser Office 365.",
    "conseils_experience": "Pour maximiser l'efficacité avec Office 365, je recommande d'expérimenter avec les fonctionnalités avancées d'Excel et d'explorer les outils d'automatisation disponibles. Se tenir informé des nouvelles fonctionnalités et pratiques d'Office 365 peut également améliorer significativement les processus de gestion des données.",
    "objectif_moyen_terme": "Mon objectif est de devenir expert dans l'utilisation avancée des outils de Microsoft 365. Je souhaite optimiser les processus de gestion des données et automatiser davantage les tâches pour accroître l'efficacité de mon travail et de mon équipe.",
    "formations_en_cours": "À ce jour, je n'ai pas de formation spécifique en cours sur Office 365, mais je prévois de suivre des formations spécialisées pour approfondir mes compétences en automatisation avancée et en utilisation des outils Microsoft 365."
},

    # Compétences humaines
    {
        "nom": "Communication",
        "type": "humaine",
        "niveau": "intermédiaire",
        "description": "La communication est la capacité à transmettre des informations de manière claire et efficace, tant à l'oral qu'à l'écrit. Elle inclut la capacité à présenter des idées, rédiger des documents, et interagir de manière constructive avec les autres.",
        "utilisation": "Dans mon travail, la communication est essentielle pour mener à bien des présentations, organiser des réunions d'équipe, rédiger des rapports détaillés, et assurer une communication interpersonnelle fluide avec les membres de l'équipe et les parties prenantes.",
        "cas_utilisation": [
            "Présentations de projets aux parties prenantes",
            "Rédaction de documentation technique",
            "Communication efficace avec les membres de l'équipe"
        ],
        "contexte_professionnel": "Dans mon rôle actuel, la communication est cruciale pour la gestion de projets et les interactions quotidiennes au sein de l'équipe. Elle permet de coordonner les efforts, de clarifier les objectifs, et de garantir que toutes les parties prenantes sont informées et engagées. Une communication efficace contribue à la bonne marche des projets et à la résolution rapide des problèmes.",
        "anecdotes": [
            {
                "titre": "Présentation de mes rapports aux équipes",
                "description": "J'ai présenté mes rapports à différents acteurs de mon entreprise (directeur de projets, responsables; consultants, assitants).",
                "resultat": "Adoption des rapports par la direction, ce qui a facilité la prise de décision et amélioré la transparence des résultats.",
            },
            {
                "titre": "Rédaction d'un manuel utilisateur",
                "description": "J'ai rédigé un manuel utilisateur détaillé pour l'utilisation de mes dahsboards en interne.",
                "resultat": "Amélioration de l'adoption de l'application et réduction des demandes de support technique, ce qui a optimisé l'efficacité des utilisateurs.",
            }
        ],
        "niveau_maitrise": "Je possède un niveau intermédiaire en communication. Je suis compétent dans la présentation d'informations, la rédaction de documents professionnels, et la communication avec les membres de l'équipe. Cependant, je souhaite continuer à perfectionner mes techniques de présentation et de rédaction pour atteindre un niveau supérieur.",
        "marge_progression": "Je souhaite perfectionner les techniques de présentation, améliorer la rédaction professionnelle, et développer des compétences en communication interculturelle pour mieux interagir avec des équipes et parties prenantes diversifiées.",
        "importance_profil": "La communication est indispensable pour la gestion efficace des projets et la coordination avec les parties prenantes. Une bonne communication garantit que les objectifs sont clairs, que les informations sont partagées efficacement, et que les équipes travaillent ensemble de manière harmonieuse.",
        "vitesse_acquisition": "J'ai acquis cette compétence rapidement grâce à diverses expériences professionnelles et à des formations en communication. L'application pratique et les interactions régulières avec différents interlocuteurs ont facilité ce développement.",
        "conseils_experience": "Pour améliorer les interactions professionnelles, je recommande de se concentrer sur l'écoute active et la clarté de l'expression. Cela aide à comprendre les besoins des autres et à communiquer les idées de manière plus efficace.",
        "objectif_moyen_terme": "Mon objectif est de maîtriser les techniques avancées de présentation et de communication interculturelle pour mieux gérer des projets internationaux et coordonner des équipes diversifiées.",
        "formations_en_cours": "À ce jour, je n'ai pas de formation spécifique en cours sur la communication, mais je serai interessé par une formation en techniques de présentation avancées e. Cette formation visera à approfondir mes compétences en communication et à améliorer encore mon efficacité dans la présentation d'informations complexes."
    },
    {
    "nom": "Interprétation des résultats",
    "type": "humaine",
    "niveau": "Intermédiaire",
    "description": "La compétence d'interprétation des résultats implique la capacité à analyser les données, à identifier des tendances pertinentes, et à tirer des conclusions significatives qui aident à orienter la prise de décision. Elle est essentielle pour convertir des données brutes en informations exploitables et pour fournir des recommandations éclairées.",
    "utilisation": "Dans mon travail, l'interprétation des résultats est cruciale pour analyser les données, identifier des tendances dans des ensembles de données volumineux, et présenter les conclusions aux parties prenantes. Cette compétence permet de transformer les analyses en actions concrètes et de soutenir les décisions stratégiques.",
    "cas_utilisation": [
        "Analyse des résultats",
        "Présentation des conclusions d'analyse à l'équipe pour influencer la direction sur les décisions"
    ],
    "contexte_professionnel": "Dans mon rôle actuel, l'interprétation des résultats est essentielle pour transformer les données brutes en informations exploitables. Cela soutient les décisions business et stratégiques en fournissant des insights qui aident à orienter les actions et les stratégies de l'entreprise. Une bonne interprétation permet de prendre des décisions plus informées et de mettre en place des actions adaptées aux réalités du marché et aux performances observées.",
    "anecdotes": [
        {
            "titre": "Présentation des conclusions d'analyse à l'équipe",
            "description": "J'ai analysé les données relatives aux livrables, en mettant en évidence les tendances, les opportunités et les erreurs. J'ai présenté ces conclusions à l'équipe pour fournir des insights exploitables.",
            "resultat": "Les insights obtenus ont permis à la directrice de projets de mettre en place des stratégies ciblées pour améliorer les livrables. Cette présentation a facilité une compréhension claire des problèmes et a guidé la mise en œuvre de solutions adaptées.",
        },
        {
            "titre": "Évaluation des performances des équipes",
            "description": "J'ai interprété les données de performance des équipes pour évaluer leur efficacité et leurs résultats.",
            "resultat": "Les conclusions ont permis d'ajuster le fonctionnement et de planifier des initiatives futures basées sur les performances observées.",
        }
    ],
    "niveau_maitrise": "Je possède un niveau intermédiaire en interprétation des résultats. Je suis capable d'analyser les données, de détecter des tendances, et de formuler des conclusions pertinentes. Cependant, je souhaite approfondir mes compétences en interprétation de données complexes et en formulation de recommandations stratégiques.",
    "marge_progression": "Je souhaite approfondir mes compétences en interprétation de données complexes, améliorer ma capacité à extraire des insights détaillés, et affiner ma formulation de recommandations stratégiques pour mieux soutenir la prise de décision.",
    "importance_profil": "L'interprétation des résultats est cruciale pour transformer les analyses en actions concrètes. Elle permet de prendre des décisions importantes basées sur des données fiables et de guider les stratégies de l'entreprise.",
    "vitesse_acquisition": "J'ai acquis cette compétence progressivement à travers des projets d'analyse de données et des discussions avec les parties prenantes. L'expérience pratique et les retours des parties prenantes ont été essentiels pour développer cette compétence.",
    "conseils_experience": "Pour améliorer l'interprétation des résultats, je recommande de se concentrer sur l'amélioration des compétences en storytelling avec les données et en analyse approfondie. Présenter les données de manière claire et contextuelle aide à mieux communiquer les insights.",
    "objectif_moyen_terme": "Mon objectif est de devenir expert en interprétation des résultats d'analyse, avec la capacité de fournir des recommandations stratégiques précises et adaptées aux besoins de l'entreprise.",
    "formations_en_cours": "À ce jour, je n'ai pas de formation spécifique en cours sur l'interprétation des résultats."
},

    {
        "nom": "Gestion du temps",
        "type": "humaine",
        "niveau":"intermédiaire",
        "description": "La gestion du temps implique la capacité à planifier, organiser et gérer efficacement son propre temps ainsi que celui de l'équipe pour atteindre les objectifs fixés. Cela inclut la priorisation des tâches, la gestion des délais et la planification de projets.",
        "utilisation": "Dans mon travail, la gestion du temps est essentielle pour la planification des projets, la gestion des tâches concurrentes, et l'optimisation des processus de travail. Cela permet de garantir que les projets sont livrés dans les délais impartis et que les ressources sont utilisées de manière efficace.",
        "cas_utilisation": [
            "Planification de projets complexes",
            "Gestion de multiples tâches concurrentes",
            "Optimisation des processus de travail"
        ],
        "contexte_professionnel": "Dans mon rôle actuel, la gestion du temps est cruciale pour la réussite des projets et pour assurer l'efficacité individuelle et collective. Une bonne gestion du temps permet de respecter les délais des projets, d'optimiser les processus de travail, et de maximiser la productivité de l'équipe. Elle est essentielle pour atteindre les objectifs de l'entreprise et garantir la satisfaction des clients et des parties prenantes.",
        "anecdotes": [
            {
                "titre": "Planification des outils",
                "description": "J'ai planifié et géré la création d'outils avec des délais serrés, en priorisant les tâches critiques pour respecter les échéances.",
                "resultat": " Livraison des projets dans les délais impartis.",
            },
            {
                "titre": "Optimisation des processus de travail",
                "description": "J'ai optimisé les processus de travail en identifiant les goulets d'étranglement et en améliorant l'efficacité opérationnelle.",
                "resultat": "Augmentation de la productivité de l'équipe et réduction significative des délais de livraison, contribuant à une meilleure performance globale de l'équipe.",
            }
        ],
        "niveau_maitrise": "Je possède un niveau intermédiaire en gestion du temps. Je suis capable de planifier efficacement des projets, de gérer plusieurs tâches concurrentes, et d'optimiser les processus de travail pour améliorer la productivité et respecter les délais.",
        "marge_progression": "Je souhaite perfectionner les techniques de gestion du temps et d'optimisation des processus pour continuer à améliorer l'efficacité et la performance dans mon rôle. Cela inclut l'exploration d'outils avancés et de méthodologies pour une gestion encore plus fine du temps et des ressources.",
        "importance_profil": "La gestion du temps est indispensable pour la réussite des projets et pour la gestion efficace des ressources. Elle joue un rôle clé dans la planification, la coordination des tâches et l'atteinte des objectifs, et est cruciale pour la performance et la satisfaction des clients.",
        "vitesse_acquisition": "Cette compétence a été acquise rapidement grâce à des expériences de gestion de projets et des formations spécifiques en gestion du temps. Les défis rencontrés dans différents projets ont contribué à améliorer mes compétences en gestion du temps.",
        "conseils_experience": "Pour optimiser la gestion du temps, il est important de se concentrer sur la planification proactive et l'optimisation continue des processus de travail. Utiliser des outils de gestion du temps et des méthodologies éprouvées peut aider à améliorer l'efficacité et à atteindre les objectifs plus rapidement.",
        "objectif_moyen_terme": "Mon objectif est de maîtriser les outils avancés de gestion du temps et de planification de projets, afin de continuer à améliorer la gestion des projets complexes et l'efficacité des processus.",
        "formations_en_cours": "À ce jour, je n'ai pas de formation spécifique en cours sur la gestion du temps. Cependant, je m'auto-forme régulièrement en consultant des ressources en ligne et en expérimentant différentes techniques de gestion du temps. Je suis également intéressé par des formations spécialisées pour approfondir mes compétences en gestion du temps et optimiser les processus."
    },
    {
        "nom": "Esprit d\'équipe",
        "type": "humaine",
        "niveau": "Intermédiaire",
        "description": "L'esprit d'équipe implique la capacité à travailler efficacement au sein d'une équipe, en favorisant la collaboration, l'entraide et la communication ouverte. Cela englobe la coopération harmonieuse et la participation active aux projets collectifs.",
        "utilisation": "Dans mon contexte professionnel, l'esprit d'équipe est essentiel pour la collaboration sur des projets transversaux, le soutien aux membres de l'équipe, et la participation active aux réunions et ateliers. Une bonne dynamique d'équipe améliore la cohésion et facilite l'atteinte des objectifs communs.",
        "cas_utilisation": [
            "Collaboration sur des projets transversaux",
            "Soutien aux membres de l'équipe",
            "Participation active aux réunions et aux ateliers"
        ],
        "contexte_professionnel": "L'esprit d'équipe est crucial pour la réussite collective et la cohésion de l'équipe. Il joue un rôle central dans l'efficacité des projets et la création d'un environnement de travail collaboratif et harmonieux.",
        "anecdotes": [
            {
                "titre": "Collaboration sur un projet transversal",
                "description": "J'ai collaboré avec différentes équipes pour mener à bien un projet transversal .",
                "resultat": "Réussite du projet grâce à une collaboration efficace et à une communication ouverte.",
             
            },
            {
              "titre": "Formation d'un collègue sur les outils d'analyse",
            "description": "J'ai formé un collègue sur l'utilisation des outils d'analyse de données et des techniques de visualisation.",
            "resultat": "Le collègue a rapidement acquis les compétences nécessaires pour gérer ses propres projets d'analyse, améliorant ainsi l'efficacité globale de l'équipe.", 
            }
        ],
        "niveau_maitrise": "Je possède un niveau intermédiaire en esprit d'équipe, avec une bonne capacité à collaborer et à soutenir les membres de l'équipe.",
        "marge_progression": "Je souhaite encourager davantage la collaboration et l'entraide au sein de l'équipe pour améliorer la cohésion et optimiser les performances collectives.",
        "importance_profil": "L'esprit d'équipe est indispensable pour assurer la cohésion et la performance de l'équipe. Il est crucial pour la réussite des projets collectifs et pour la création d'un environnement de travail positif.",
        "vitesse_acquisition": "Cette compétence a été acquise progressivement grâce à des expériences variées de travail en équipe.",
        "conseils_experience": "Pour renforcer l'esprit d'équipe, il est important de favoriser un environnement de travail collaboratif et ouvert. Encourager la communication, offrir du soutien aux collègues et participer activement aux projets collectifs sont essentiels pour développer une forte cohésion d'équipe.",
        "objectif_moyen_terme": "Mon objectif est de devenir un modèle de collaboration et de soutien au sein de l'équipe. Je souhaite continuer à promouvoir un environnement de travail collaboratif et aider mes collègues à atteindre leurs objectifs.",
        "formations_en_cours": "Je n'ai pas de formation spécifique en cours sur l'esprit d'équipe, mais je m'auto-forme en consultant des ressources sur la dynamique de groupe et la collaboration. Je suis également intéressé par des formations spécialisées pour approfondir mes compétences en dynamique d'équipe et en collaboration, prévues pour le semestre prochain."
    }
]

projets = [
    {
        "id": "1",
        "nom": "Gestionnaire de contact",
        "contexte": "Une personne détenant une marque de vêtements m'a demandé de lui développer un script qui lui permettrait de recevoir un fichier avec les informations de personnes qui souhaiteraient travailler avec elle, de ce fait, elle ne serait plus obligée d'aller rechercher dans ses anciennes discussions les informations nécessaires. La nécessité était de centraliser les informations de contact pour une gestion plus efficace dans un environnement professionnel en croissance.",
        "description": "Pour répondre à ce besoin, j'ai développé un script personnalisé qui permet de gérer efficacement les contacts professionnels. Ce script est capable de stocker, organiser et rechercher des informations de contact de manière intuitive et efficace. Il s'appuie sur un Google Form conçu spécifiquement pour collecter les informations de contact, qui sont ensuite traitées et centralisées dans une base de données. Chaque semaine, le script génère automatiquement un fichier contenant les nouveaux contacts collectés et l'envoie par mail au client.",
        "objectifs": "L'objectif principal était de faciliter la recherche des contacts tout en assurant l'automatisation de l'envoi d'un rapport récurrent chaque semaine, comprenant les nouveaux contacts. Ce rapport devait être directement envoyé par mail, permettant ainsi au client de gagner du temps et de se concentrer sur d'autres aspects de son activité.",
        "enjeux": "L'enjeu principal du projet était de créer une solution opérationnelle et facile à utiliser, capable de gérer un volume important de données sans compromettre la qualité du service. Il était crucial de s'assurer que le script soit non seulement fonctionnel, mais aussi assez intuitif pour que le client puisse l'adopter facilement dans son workflow quotidien.",
        "risques": "Les principaux risques identifiés étaient liés à la sécurité des données, puisque les informations de contact sont sensibles et doivent être protégées contre les accès non autorisés. Un autre risque potentiel concernait la difficulté d'adoption du script par l'utilisateur final, en raison de la complexité technique ou d'une interface utilisateur peu conviviale.",
        "etapes": "Analyse des besoins : Compréhension approfondie des attentes du client et des spécificités de ses processus de travail. Conception du Google Form : Création d'un formulaire en ligne permettant de recueillir les informations de contact de manière structurée. Développement du script : Écriture du code pour automatiser la collecte, le stockage, et l'organisation des données, ainsi que la génération et l'envoi hebdomadaire des rapports. Tests : Phase de test rigoureuse pour s'assurer que le script fonctionne correctement et répond aux besoins du client. Déploiement : Mise en service du script et formation du client pour une prise en main rapide et efficace.",
        "acteurs": "Moi qui suis développeur et concepteur du script, et l'utilisateur final qui est le client qui utilise le script pour gérer les contacts.",
        "resultats": "Le script a été déployé avec succès, validé et adopté par le client. Grâce à cette solution, le client a pu réduire le temps nécessaire de 50% pour rechercher des contacts, ce qui représente un gain de productivité significatif.",
        "lendemains": "À l'avenir, il sera nécessaire d'assurer une maintenance continue du script, notamment pour ajouter de nouvelles fonctionnalités et améliorer l'expérience utilisateur. Par ailleurs, une attention particulière devra être portée à la sécurité des données, surtout en ce qui concerne l'envoi des fichiers par mail.",
        "regardCritique": "Bien que le projet ait atteint ses objectifs initiaux, il est clair que le script pourrait être encore amélioré. L'ajout de nouvelles fonctionnalités, comme l'intégration avec des réseaux sociaux ou des CRM, pourrait rendre l'outil encore plus puissant et utile pour le client. En outre, une amélioration de la sécurité des données est impérative pour garantir la confidentialité des informations collectées.",
        "competences": ["Gestion de base de données", "Java","Automatisation"],
    },
    {
        "id": "2",
        "nom": "Automatisation de PowerPoint",
        "contexte": "Dans le cadre des activités de la Business Unit (BU) Service Public à l'Emploi, les responsables doivent régulièrement préparer des présentations PowerPoint pour les clients. Ces présentations nécessitent souvent l'intégration de données et la création de graphiques, des tâches qui peuvent prendre jusqu'à trois heures pour certaines personnes. La nécessité d'une solution pour réduire ce temps de préparation tout en maintenant la cohérence des présentations est devenue évidente, d'où la création de cet outil d'automatisation.",
        "description": "J'ai développé un outil capable de générer automatiquement des présentations PowerPoint à partir de données structurées. Cet outil prend en entrée des informations formatées, les analyse et produit des diapositives avec des graphiques et du texte explicatif, tout en respectant les normes de présentation de l'entreprise. Le script utilise des bibliothèques Python pour interagir avec PowerPoint, ce qui permet d'automatiser la création de slides et d'assurer une cohérence visuelle et stylistique entre les différentes présentations.",
        "objectifs": "L'objectif principal était de réduire le temps de préparation des présentations PowerPoint en automatisant la génération des diapositives. Cette automatisation devait permettre aux responsables de créer des présentations cohérentes et professionnelles en quelques minutes, libérant ainsi du temps pour d'autres tâches à plus forte valeur ajoutée.",
        "enjeux": "Le principal enjeu était de s'assurer que l'automatisation fonctionne sans accroc, en particulier en ce qui concerne l'intégration avec PowerPoint. Les erreurs de formatage, la cohérence des graphiques et la capacité de l'outil à gérer des données variées étaient des défis importants à surmonter.",
        "risques": "Les risques étaient principalement liés à l'intégration technique avec PowerPoint, notamment des problèmes potentiels de formatage et de mise en page des diapositives. Il était également crucial de garantir la cohérence des présentations générées, tant au niveau du contenu que du style.",
        "etapes": "Collecte des besoins : Discussions avec les utilisateurs finaux pour comprendre leurs attentes et les types de données à intégrer dans les présentations. Développement du script d'automatisation : Écriture du code pour automatiser la génération des diapositives PowerPoint, y compris l'intégration des graphiques et du texte. Tests : Validation du fonctionnement de l'outil avec différents ensembles de données pour s'assurer qu'il génère des présentations cohérentes et sans erreurs.",
        "acteurs": "Moi qui suis le développeur de l'outil d'automatisation et les utilisateurs finaux qui sont les responsables de la BU.",
        "resultats": "L'outil a permis une réduction du temps de préparation des présentations PowerPoint de 70%. Les responsables ont pu générer des slides cohérents et professionnels en quelques minutes, libérant ainsi du temps pour se concentrer sur d'autres tâches à plus forte valeur ajoutée.",
        "lendemains": "À l'avenir, il est prévu d'améliorer l'outil pour qu'il puisse gérer des formats de données plus complexes et permettre l'utilisation de modèles personnalisés. Une autre perspective d'évolution est l'intégration avec une intelligence artificielle pour pousser l'analyse des données et générer des présentations encore plus pertinentes.",
        "regardCritique": "Bien que l'outil ait grandement facilité la tâche des utilisateurs, il reste perfectible. L'automatisation pourrait être étendue à d'autres types de documents, et il serait également bénéfique de développer une interface utilisateur pour le rendre plus accessible. De plus, l'outil est actuellement dépendant de ma personne pour son lancement, car il est difficile de déployer même des projets mineurs au sein de la BU dans une grande entreprise. Cela est principalement dû aux règles strictes mises en place dans l'entreprise, qui compliquent le déploiement de nouvelles solutions informatiques. Pour l'instant, je lance l'outil depuis mon ordinateur en local, ce qui limite son accessibilité.",
        "competences": ["Python", "Automatisation", "Microsoft Office"],
    },
    {
        "id": "3",
        "nom": "Outil de scraping",
        "contexte": "Dans le cadre des opérations de reporting de la Business Unit, ma supérieure hiérarchique (N+1) devait rassembler manuellement des informations concernant les événements pour chaque candidat. Pour une moyenne de 1 000 candidats, cette tâche prenait environ une semaine. Constatant l'inefficacité de ce processus manuel, j'ai décidé de développer un outil capable d'extraire automatiquement ces données depuis un site web, réduisant ainsi considérablement le temps nécessaire au recensement des informations.",
        "description": "J'ai développé un outil de scraping utilisant Python pour extraire automatiquement des données spécifiques depuis un site web. Cet outil collecte les informations nécessaires, les organise, puis les présente sous un format exploitable pour le reporting. L'automatisation du scraping permet de traiter un grand nombre de candidats en quelques heures, là où le processus manuel prenait plusieurs jours.",
        "objectifs": "L'objectif principal était d'automatiser la collecte de données depuis un site web et d'organiser ces informations pour une analyse ultérieure. L'automatisation visait à non seulement accélérer le processus de collecte, mais aussi à assurer l'exactitude et la fiabilité des données extraites, afin de faciliter le travail de reporting.",
        "enjeux": "L'enjeu principal était de s'assurer que l'outil de scraping respecte les politiques d'utilisation des sites web pour éviter tout risque de blocage ou de bannissement. De plus, il était essentiel de garantir la qualité des données collectées, en s'assurant qu'elles soient complètes et exactes.",
        "risques": "Les risques incluent la possibilité que le site web cible modifie sa structure, ce qui pourrait entraîner des erreurs dans le scraping des données. Il y avait également un risque de non-conformité avec les politiques de scraping du site web, ce qui pourrait entraîner des complications juridiques ou techniques.",
        "etapes": "Analyse des besoins : Identification des données à extraire et compréhension de la structure du site web cible. Développement de l'outil de scraping : Écriture du code pour extraire et organiser les données. Tests : Validation du processus de scraping avec différents ensembles de données pour vérifier l'exactitude et la fiabilité des informations collectées. Déploiement : Mise en place de l'outil et formation des utilisateurs finaux pour une utilisation efficace.",
        "acteurs": "Moi en tant que développeur de l'outil et ma supérieure hiérarchique, qui est l'utilisateur final et bénéficiaire de l'automatisation.",
        "resultats": "L'outil de scraping a réduit le temps nécessaire pour collecter les informations des candidats de 70%. Ce gain de temps a permis à la Business Unit de préparer les reportings beaucoup plus rapidement et avec une meilleure précision.",
        "lendemains": "Il est prévu d'améliorer l'outil pour qu'il puisse extraire des informations depuis plusieurs sites web ou sources de données et gérer les éventuels changements de structure des sites. Une future amélioration pourrait également inclure des fonctionnalités d'analyse des données extraites pour offrir des insights plus approfondis.",
        "regardCritique": "L'outil a significativement amélioré l'efficacité du processus de collecte de données, mais il est nécessaire d'envisager des améliorations pour gérer les évolutions potentielles des sites web cibles. De plus, le respect des politiques de scraping et la gestion des éventuels blocages doivent être soigneusement surveillés pour éviter des interruptions dans le processus.",
        "competences": ["Scraping", "Python", "Analyse de données"],
    },
    {
        "id": "4",
        "nom": "Outil de gestion des événements",
        "contexte": "Dans le cadre du suivi de l'accompagnement des candidats sur le site web de Pôle emploi, une section dédiée permet aux utilisateurs de vérifier où en est le processus d'accompagnement. Toutefois, la tâche de télécharger manuellement chaque fichier CSV, de les rassembler et d'en extraire les informations pertinentes est très chronophage pour les assistants de projets. Cette activité, bien qu'essentielle, devenait de plus en plus difficile à gérer efficacement en raison de la multiplicité des fichiers et des informations à traiter. Pour résoudre ce problème, j'ai entrepris de développer un outil capable d'automatiser ces tâches.",
        "description": "J'ai développé un outil destiné à extraire automatiquement les événements à partir d'un site web, à fusionner les fichiers CSV récupérés, puis à mettre en forme ces données pour qu'elles soient facilement utilisables dans le cadre de rapports et de suivis. L'outil simplifie considérablement le processus de gestion des événements, permettant ainsi aux assistants de projets de se concentrer sur des tâches à plus forte valeur ajoutée.",
        "objectifs": "L'objectif principal du projet était de faciliter le reporting lié aux événements en centralisant toutes les informations nécessaires et en automatisant les tâches répétitives, telles que l'extraction des événements à partir du site web, la fusion des fichiers CSV, et la mise en forme des données pour une analyse efficace.",
        "enjeux": "Le principal enjeu était de garantir que l'outil synchronise correctement les informations provenant des différents fichiers CSV et qu'il fonctionne de manière fluide lors de l'exécution de tâches complexes, comme la fusion de données et leur mise en forme. Une mauvaise synchronisation ou des bugs pourraient entraîner des erreurs dans les rapports, ce qui affecterait la prise de décision.",
        "risques": "Les risques identifiés incluaient des problèmes de synchronisation des informations, des bugs potentiels lors de l'utilisation de l'outil pendant les événements, ainsi que le risque de rendre l'outil obsolète en cas de modifications importantes sur le site source.",
        "etapes": "Analyse des besoins : Identification des exigences spécifiques des utilisateurs finaux, notamment les types de données à extraire et les formats de sortie nécessaires. Conception de l'outil : Élaboration de l'architecture de l'outil, incluant les fonctionnalités d'extraction, de fusion et de mise en forme des données. Développement : Programmation de l'outil en utilisant des technologies adaptées pour assurer sa robustesse et son efficacité. Tests : Validation des performances de l'outil à travers différents scénarios d'utilisation pour garantir la fiabilité des résultats.",
        "acteurs": "Moi qui suis développeur de l'outil d'automatisation et les utilisateurs finaux, qui sont les assistants de projets.",
        "resultats": "L'outil a permis d'améliorer l'efficacité de la gestion des événements de 60%, ce qui a considérablement réduit le temps consacré au reporting et a augmenté la satisfaction des utilisateurs finaux. Les tâches qui prenaient auparavant plusieurs heures sont désormais réalisées en quelques minutes, libérant ainsi du temps pour d'autres activités.",
        "lendemains": "À l'avenir, il serait pertinent d'intégrer un frontend à l'outil pour en faciliter l'utilisation et le rendre accessible à un plus grand nombre d'utilisateurs sans nécessiter une intervention technique directe. Cela permettrait également d'ajouter des fonctionnalités supplémentaires pour approfondir l'analyse des données extraites, offrant ainsi une vue encore plus détaillée des événements gérés.",
        "regardCritique": "Le projet a été un succès en termes d'amélioration de l'efficacité des processus de gestion des événements. Toutefois, l'outil nécessite un développement ultérieur pour inclure un frontend afin de le rendre plus accessible et utilisable par tous. Le déploiement à l'échelle de l'entreprise reste un défi en raison des politiques internes strictes qui compliquent l'intégration et le déploiement de nouvelles solutions informatiques.",
        "competences": ["Scrapping", "Python", "Gestion des données"],
    },
    {
        "id": "5",
        "nom": "Outil d'intégration et suivi de nouveaux candidats",
        "contexte": "Pour le compte du Conseil Départemental du Val-d’Oise, un consultant doit réaliser chaque année un reporting complet de tous les candidats reçus. Ce reporting est maintenu dans un fichier Excel, mais le volume élevé de candidatures rend cette tâche extrêmement longue et laborieuse. Le consultant a exprimé le besoin d'un outil capable d'automatiser ce processus pour réduire le temps et l'énergie consacrés à la gestion des données des candidats.",
        "description": "J'ai développé un outil multifonctionnel capable de gérer plusieurs étapes du traitement des candidatures : téléchargement et comparaison de fichiers, scraping d'informations à partir d'un site web, intégration des données dans un tableau Excel, et mise en forme du fichier final. Cet outil vise à automatiser et optimiser la gestion des nouveaux candidats pour le reporting annuel du consultant, simplifiant ainsi un processus autrefois manuel et chronophage.",
        "objectifs": "L'objectif principal était d'automatiser le processus d'ajout de nouveaux candidats dans un fichier Excel. Cela comprend le téléchargement de fichiers, la comparaison entre différents fichiers, le scraping d'informations depuis un site web, l'intégration de ces informations dans un tableau Excel, et le traitement final du fichier pour ajouter de nouvelles données et le mettre en forme. Ce processus vise à améliorer l'efficacité, la traçabilité et à réduire considérablement le temps consacré à la gestion des candidatures.",
        "enjeux": "Les enjeux principaux étaient de garantir une gestion efficace des candidatures, avec un gain de temps significatif et une augmentation de la productivité. L'outil devait aussi assurer une traçabilité améliorée des données et réduire les erreurs humaines associées à la gestion manuelle des informations.",
        "risques": "Les risques potentiels comprenaient des erreurs dans l'extraction des données, des problèmes liés à la mise à jour des structures du site web, et des difficultés liées à la gestion du fichier Excel lorsqu'il serait volumineux ou complexe.",
        "etapes": "Identification des besoins : Compréhension des exigences du consultant et définition des spécifications pour l'outil. Développement de l'outil : Création de l'outil pour automatiser le téléchargement, la comparaison, le scraping, et le traitement des fichiers. Phase pilote : Test de l'outil avec un échantillon de données pour valider son fonctionnement et ses performances.",
        "acteurs": "Moi qui suis développeur principal responsable de la création et de la mise en œuvre de l'outil, et le consultant qui est l'utilisateur final de l'outil, chargé du reporting et de la gestion des candidatures.",
        "resultats": "L'outil a permis une réduction du temps de traitement des candidatures de 80%, ce qui a entraîné une amélioration notable de la satisfaction du consultant, une diminution des erreurs. La productivité globale a également été augmentée grâce à l'automatisation du processus.",
        "lendemains": "À l'avenir, il sera nécessaire de maintenir l'outil à jour pour s'adapter aux éventuels changements sur le site web d'où proviennent les données. Cela garantira que l'outil reste fonctionnel et efficace à long terme.",
        "regardCritique": "Bien que l'outil ait considérablement optimisé le processus de gestion des candidatures, il reste dépendant de mon ordinateur pour son exécution, ce qui le rend inutilisable en mon absence. Ce problème est en partie dû aux politiques strictes de l'entreprise qui compliquent le déploiement d'applications automatisées. Ces règlements rendent difficile l'intégration et l'accès à l'outil pour d'autres utilisateurs, limitant ainsi son efficacité lorsque je ne suis pas présent.",
        "competences": ["Scrapping", "Python", "Gestion des données","365 office"],
    },
]





@app.route('/api/competences', methods=['GET'])
def get_competences():
    return jsonify(competences)

@app.route('/api/projets', methods=['GET'])
def get_projets():
    return jsonify(projets)

@app.route('/api/projets/<int:id>', methods=['GET'])
def get_projet(id):
    projet = next((p for p in projets if p['id'] == str(id)), None)
    
    if projet:
        return jsonify(projet)
    else:
        return jsonify({'message': 'Projet non trouvé'}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
