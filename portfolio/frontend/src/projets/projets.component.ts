// Importation des modules nécessaires depuis Angular
import { Component, OnInit } from '@angular/core'; // Importation des décorateurs et interfaces d'Angular
import { Router } from '@angular/router'; // Importation du service de routage pour la navigation
import { ProjetsService } from '../services/projets.service'; // Importation du service qui fournit les données des projets
import { CommonModule } from '@angular/common'; // Importation du module commun d'Angular (inclut des fonctionnalités de base)
import { RouterLink } from '@angular/router'; // Importation de la directive RouterLink pour la navigation dans les templates

// Déclaration du composant Angular
@Component({
  selector: 'app-projets', // Sélecteur SCSS pour utiliser ce composant dans le template HTML
  standalone: true, // Indique que ce composant est autonome et peut être utilisé indépendamment
  templateUrl: './projets.component.html', // Chemin vers le fichier template HTML associé
  styleUrls: ['./projets.component.scss'], // Chemin vers le fichier de styles SCSS associé
  imports: [CommonModule, RouterLink] // Importation des modules nécessaires pour le composant
})
export class ProjetsComponent implements OnInit {
  projets: any[] = []; // Liste des projets qui sera affichée dans le template

  // Injection des services nécessaires via le constructeur
  constructor(private projetsService: ProjetsService, private router: Router) { }

  // Méthode du cycle de vie Angular appelée après l'initialisation du composant
  ngOnInit(): void {
    this.loadProjets(); // Chargement des projets dès que le composant est initialisé
  }

  // Méthode pour charger les projets depuis le service
  loadProjets(): void {
    this.projetsService.getProjets().subscribe(data => {
      this.projets = data; // Attribution des données récupérées à la liste des projets
    });
  }

  // Méthode pour naviguer vers les détails d'un projet spécifique
  voirDetails(projetId: number): void {
    this.router.navigate(['/projets', projetId]); // Redirection vers la page de détails du projet
  }
}
