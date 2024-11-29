import { Component, OnInit } from '@angular/core';
import { Router, NavigationEnd } from '@angular/router'; 
import { filter } from 'rxjs/operators'; 
import { CommonModule } from '@angular/common'; 
import { RouterModule } from '@angular/router'; 
import { ProjetsService } from '../services/projets.service';

@Component({
  selector: 'app-header',
  standalone: true,
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss'],
  imports: [CommonModule, RouterModule]
})
export class HeaderComponent implements OnInit {
  projects: any[] = [];  // Liste des projets qui contiendra les noms et autres informations
  currentRoute: string = '';

  constructor(private router: Router, private projetsService: ProjetsService) {}

  ngOnInit(): void {
    // Récupérer les projets au moment de l'initialisation du composant
    this.projetsService.getProjets().subscribe((projets: any[]) => {
      this.projects = projets; // On assigne la réponse de l'API à la variable projects
    });

    // Gérer la navigation
    this.router.events.pipe(
      filter(event => event instanceof NavigationEnd)
    ).subscribe(() => {
      this.currentRoute = this.router.url;
    });
  }

  scrollToSection(sectionId: string) {
    if (this.currentRoute === '/accueil') {
      const element = document.getElementById(sectionId);
      if (element) {
        element.scrollIntoView({ behavior: 'smooth' });
      }
    }
  }
}
