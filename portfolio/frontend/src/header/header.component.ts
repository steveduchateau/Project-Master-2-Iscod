import { Component, OnInit } from '@angular/core';
import { Router, NavigationEnd } from '@angular/router'; 
import { filter } from 'rxjs/operators'; 
import { CommonModule } from '@angular/common'; 
import { RouterModule } from '@angular/router'; 
import { ProjetsService } from './projets.service'; // Assurez-vous d'importer votre service de projets

@Component({
  selector: 'app-header', 
  standalone: true, 
  templateUrl: './header.component.html', 
  styleUrls: ['./header.component.scss'], 
  imports: [CommonModule, RouterModule] 
})
export class HeaderComponent implements OnInit {
  projects: any[] = []; // Liste des projets avec leurs noms et IDs
  currentRoute: string = '';

  constructor(private router: Router, private projetsService: ProjetsService) {}

  ngOnInit(): void {
    // Abonnez-vous aux événements de navigation
    this.router.events.pipe(
      filter(event => event instanceof NavigationEnd) 
    ).subscribe(() => {
      this.currentRoute = this.router.url; 
    });

    // Récupération des projets depuis l'API
    this.projetsService.getProjets().subscribe(data => {
      this.projects = data; // Assurez-vous que la réponse contient les noms des projets
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
