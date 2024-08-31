import { Component } from '@angular/core';

/**
 * Déclaration du composant Angular.
 * Le composant est utilisé pour la page d'accueil.
 */
@Component({
  // Sélecteur du composant, utilisé pour l'inclure dans les templates HTML
  selector: 'app-accueil',

  // Indique que ce composant est autonome, c'est-à-dire qu'il peut fonctionner indépendamment
  standalone: true,

  // Liste des autres composants ou modules importés dans ce composant (ici, aucun import)
  imports: [],

  // Chemin vers le fichier de template HTML du composant
  templateUrl: './accueil.component.html',

  // Chemin vers le fichier de style SCSS du composant
  styleUrls: ['./accueil.component.scss']
})
export class AccueilComponent {
  // Ce composant n'a pas de logique propre pour l'instant
}
