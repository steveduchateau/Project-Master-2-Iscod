import { Component, AfterViewInit } from '@angular/core';

@Component({
  selector: 'app-experience',
  standalone: true,
  templateUrl: './experience.component.html',
  styleUrls: ['./experience.component.scss']
})
export class ExperienceComponent implements AfterViewInit {

  ngAfterViewInit() {
    // Convertir NodeList en tableau pour manipulation plus facile
    const buttons = Array.from(document.querySelectorAll('.nav-btn')) as HTMLElement[];
    const timelines = Array.from(document.querySelectorAll('.timeline')) as HTMLElement[];
    const detailButtons = Array.from(document.querySelectorAll('.toggle-details')) as HTMLElement[];

    // Ajouter les gestionnaires d'événements aux boutons de navigation
    buttons.forEach(button => {
      button.addEventListener('click', () => {
        const target = button.getAttribute('data-target') || '';
        console.log(`Button clicked, target: ${target}`);

        // Mettre à jour les classes d'activation des boutons
        buttons.forEach(btn => btn.classList.remove('active'));
        button.classList.add('active');

        // Afficher ou masquer les timelines en fonction du bouton sélectionné
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

    // Afficher la première section par défaut
    buttons[0]?.click(); // Afficher la première section au chargement
  }
}
