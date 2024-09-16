# Fonctionnement du Frontend

Le frontend de l'application est conçu de manière modulaire, avec des composants spécialisés pour chaque fonctionnalité, permettant une organisation claire et maintenable du code. Voici un aperçu de la structure et du fonctionnement du frontend :

## Structure Modulaire des Composants

Chaque fonctionnalité de l'application est encapsulée dans des composants distincts. Cela facilite la réutilisation du code et améliore la lisibilité. Les composants sont utilisés pour créer des sections spécifiques de l'interface utilisateur ce qui offrent une expérience utilisateur cohérente et optimisée.

## Gestion des Pages Statiques

Les pages statiques, telles que la page d'accueil et les pages de présentation, contiennent des informations intégrées directement dans le code. Ces données sont considérées comme constantes, car elles ne nécessitent pas de mises à jour fréquentes. Cela permet une performance optimale en évitant des appels inutiles au backend pour des informations rarement modifiées.

## Composant de Services pour les Sections Dynamiques

Pour les sections dynamiques, comme celles dédiées aux projets et aux compétences, un composant dédié nommé `services` est utilisé. Ce composant joue un rôle essentiel dans la communication entre le frontend et le backend :

- **Appels API** : Le composant `services` gère les appels API nécessaires pour interagir avec le serveur. Il permet de récupérer en temps réel les données dynamiques requises par l'application.
- **Intégration des Données** : Les données récupérées via les API sont intégrées directement dans les composants appropriés. Cela garantit que les contenus affichés à l'utilisateur sont toujours à jour et reflètent les informations les plus récentes.
- **Mise à jour Dynamique** : Grâce au composant `services`, les sections dynamiques sont mises à jour automatiquement sans nécessiter de rechargement de la page, assurant une expérience utilisateur fluide et interactive.
