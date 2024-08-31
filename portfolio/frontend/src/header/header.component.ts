import { Component, OnInit } from '@angular/core';
import { Router, NavigationEnd } from '@angular/router'; // Importations pour la gestion de la navigation
import { filter } from 'rxjs/operators'; // Importation de l'opérateur filter pour RxJS
import { CommonModule } from '@angular/common'; // Module commun pour les directives Angular de base
import { RouterModule } from '@angular/router'; // Module pour les fonctionnalités de routage

@Component({
  selector: 'app-header', // Sélecteur pour utiliser ce composant dans les templates
  standalone: true, // Composant autonome, ne dépend pas d'un module NgModule
  templateUrl: './header.component.html', // Template HTML associé à ce composant
  styleUrls: ['./header.component.scss'], // Styles SCSS associés à ce composant
  imports: [CommonModule, RouterModule] // Modules nécessaires pour le composant
})
export class HeaderComponent implements OnInit {
  // Liste des IDs des projets, utilisée pour les menus déroulants ou autres fonctionnalités
  projects: number[] = [1, 2, 3, 4, 5];

  // Variable pour stocker la route actuelle
  currentRoute: string = '';

  constructor(private router: Router) {}

  ngOnInit(): void {
    // Abonnez-vous aux événements de navigation pour mettre à jour la route actuelle
    this.router.events.pipe(
      filter(event => event instanceof NavigationEnd) // Filtre pour ne traiter que les événements de fin de navigation
    ).subscribe(() => {
      this.currentRoute = this.router.url; // Met à jour la route actuelle
    });
  }

  scrollToSection(sectionId: string) {
    // Méthode pour faire défiler la page jusqu'à une section spécifique
    // Assure que le défilement ne se fait que si vous êtes sur la page d'accueil
    if (this.currentRoute === '/accueil') {
      const element = document.getElementById(sectionId); // Récupère l'élément avec l'ID spécifié
      if (element) {
        // Fait défiler l'élément en douceur dans la vue
        element.scrollIntoView({ behavior: 'smooth' });
      }
    }
  }
}
