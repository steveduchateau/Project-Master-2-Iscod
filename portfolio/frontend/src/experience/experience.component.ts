import { Component, AfterViewInit } from '@angular/core';

/**
 * Composant Angular pour la section "Expérience".
 * Ce composant est chargé d'afficher et de gérer les sections d'expérience avec des détails interactifs.
 */
@Component({
  // Sélecteur du composant utilisé pour insérer ce composant dans le template HTML
  selector: 'app-experience',

  // Indique que ce composant est autonome, donc indépendant et ne nécessite pas d'autres modules
  standalone: true,

  // Chemin vers le fichier de template HTML du composant
  templateUrl: './experience.component.html',

  // Chemin vers le fichier de style SCSS du composant
  styleUrls: ['./experience.component.scss']
})
export class ExperienceComponent implements AfterViewInit {

  /**
   * Méthode appelée après l'initialisation de la vue du composant.
   * Utilisée ici pour ajouter des gestionnaires d'événements aux éléments du DOM.
   */
  ngAfterViewInit() {
    // Convertir NodeList en tableau pour une manipulation plus facile
    const buttons = Array.from(document.querySelectorAll('.nav-btn')) as HTMLElement[];
    const timelines = Array.from(document.querySelectorAll('.timeline')) as HTMLElement[];
    const detailButtons = Array.from(document.querySelectorAll('.toggle-details')) as HTMLElement[];

    // Ajouter les gestionnaires d'événements aux boutons de navigation
    buttons.forEach(button => {
      button.addEventListener('click', () => {
        // Récupérer la cible associée au bouton cliqué
        const target = button.getAttribute('data-target') || '';
        console.log(`Button clicked, target: ${target}`);

        // Mettre à jour les classes d'activation des boutons
        buttons.forEach(btn => btn.classList.remove('active'));
        button.classList.add('active');

        // Afficher ou masquer les sections de timeline en fonction du bouton sélectionné
        timelines.forEach(timeline => {
          if ((timeline as HTMLElement).id === target) {
            (timeline as HTMLElement).style.display = 'flex';
          } else {
            (timeline as HTMLElement).style.display = 'none';
          }
        });
      });
    });

    // Ajouter les gestionnaires d'événements aux boutons de détails
    detailButtons.forEach(button => {
      button.addEventListener('click', () => {
        const details = button.nextElementSibling as HTMLElement;
        if (details) {
          // Afficher ou masquer les détails en fonction de leur état actuel
          if (details.style.display === 'none' || details.style.display === '') {
            details.style.display = 'block';
            button.textContent = '- Moins de détails';
          } else {
            details.style.display = 'none';
            button.textContent = '+ Plus de détails';
          }
        }
      });
    });

    // Afficher la première section par défaut au chargement
    buttons[0]?.click(); // Simule un clic sur le premier bouton pour afficher la première section
  }
}
