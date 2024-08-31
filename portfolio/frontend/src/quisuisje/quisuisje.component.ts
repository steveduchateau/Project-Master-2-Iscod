// Importation des modules nécessaires depuis Angular
import { Component, AfterViewInit } from '@angular/core'; // Importation de 'Component' pour définir un composant Angular et 'AfterViewInit' pour exécuter du code après l'initialisation de la vue

// Déclaration du composant Angular
@Component({
  // Sélecteur du composant qui sera utilisé dans les templates HTML pour insérer ce composant
  selector: 'app-quisuisje',
  // Déclaration que ce composant est autonome (standalone), ce qui signifie qu'il peut être utilisé sans module Angular traditionnel
  standalone: true,
  // Chemin vers le fichier HTML du template du composant
  templateUrl: './quisuisje.component.html',
  // Chemin vers le fichier SCSS du style du composant
  styleUrls: ['./quisuisje.component.scss']
})
// Définition de la classe du composant
export class QuisuisjeComponent implements AfterViewInit {
  // Propriété pour suivre l'indice de la page actuelle, initialisée à 0 (première page)
  currentPage = 0;
  // Propriété pour suivre le nombre total de pages, initialisée à 0
  totalPages: number = 0;

  // Méthode du cycle de vie Angular appelée après l'initialisation de la vue du composant
  ngAfterViewInit() {
    // Sélectionne toutes les éléments de page en utilisant le sélecteur CSS '.page'
    const pages = document.querySelectorAll('.page');
    // Définit le nombre total de pages en fonction du nombre d'éléments '.page'
    this.totalPages = pages.length;

    // Fonction pour mettre à jour l'affichage et l'orientation des pages
    const updatePages = () => {
      // Parcourt chaque élément de page
      pages.forEach((page, index) => {
        // Si l'indice de la page est inférieur à la page actuelle, elle est tournée vers l'arrière
        if (index < this.currentPage) {
          page.setAttribute('style', 'transform: rotateY(-180deg);');
        } 
        // Si l'indice de la page est égal à la page actuelle, elle est visible normalement
        else if (index === this.currentPage) {
          page.setAttribute('style', 'transform: rotateY(0deg);');
        } 
        // Si l'indice de la page est supérieur à la page actuelle, elle est tournée vers l'avant
        else {
          page.setAttribute('style', 'transform: rotateY(180deg);');
        }
      });

      // Sélectionne l'élément affichant le numéro de la page actuelle
      const currentPageElement = document.querySelector('.current-page');
      // Met à jour le texte de l'élément pour afficher le numéro de la page actuelle
      if (currentPageElement) {
        currentPageElement.textContent = `Page ${this.currentPage + 1}`;
      }
    };

    // Sélectionne le bouton "Suivant" en utilisant le sélecteur CSS '.next'
    const nextButton = document.querySelector('.next');
    // Sélectionne le bouton "Précédent" en utilisant le sélecteur CSS '.prev'
    const prevButton = document.querySelector('.prev');

    // Ajoute un gestionnaire d'événement pour le bouton "Suivant"
    if (nextButton) {
      nextButton.addEventListener('click', () => {
        // Vérifie si la page actuelle est inférieure au nombre total de pages moins un
        if (this.currentPage < this.totalPages - 1) {
          // Incrémente le numéro de la page actuelle
          this.currentPage++;
          // Met à jour l'affichage des pages après le changement de page
          updatePages();
        }
      });
    }

    // Ajoute un gestionnaire d'événement pour le bouton "Précédent"
    if (prevButton) {
      prevButton.addEventListener('click', () => {
        // Vérifie si la page actuelle est supérieure à 0
        if (this.currentPage > 0) {
          // Décrémente le numéro de la page actuelle
          this.currentPage--;
          // Met à jour l'affichage des pages après le changement de page
          updatePages();
        }
      });
    }

    // Mise à jour initiale des pages lors du chargement du composant
    updatePages();
  }
}
