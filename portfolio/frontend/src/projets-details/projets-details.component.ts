import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { ProjetsService } from '../services/projets.service';
import { Location } from '@angular/common';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { switchMap, catchError } from 'rxjs/operators';
import { throwError } from 'rxjs';

@Component({
  selector: 'app-projets-details',
  standalone: true,
  templateUrl: './projets-details.component.html',
  styleUrls: ['./projets-details.component.scss'],
  imports: [CommonModule, RouterModule],
})
export class ProjetsDetailsComponent implements OnInit {
  projet: any;
  isCompetencesArray: boolean = false;
  isCompetencesString: boolean = false;

  // Mapping des compétences avec leurs URLs fixes
  competenceUrls: { [key: string]: string } = {
    // Compétences techniques
    Python: '/competences/techniques/1',
    'Power BI': '/competences/techniques/2',
    SQL: '/competences/techniques/3',
    'Office 365': '/competences/techniques/4',

    // Compétences humaines
    Communication: '/competences/humaines/101',
    'Interprétation des résultats': '/competences/humaines/102',
    'Gestion du temps': '/competences/humaines/103',
    "Esprit d'équipe": '/competences/humaines/104',
  };

  constructor(
    private route: ActivatedRoute,
    private projetsService: ProjetsService,
    private location: Location,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.route.paramMap
      .pipe(
        switchMap((params) => {
          const id = params.get('id');
          if (id) {
            return this.projetsService.getProjetById(id);
          } else {
            return throwError(() => new Error('ID de projet manquant'));
          }
        }),
        catchError((err) => {
          console.error('Erreur lors de la récupération du projet:', err);
          return throwError(() => err);
        })
      )
      .subscribe({
        next: (data) => {
          this.projet = data;
          console.log('Projet:', this.projet);

          // Déterminer si les compétences sont une chaîne ou un tableau
          if (this.projet && this.projet.competences) {
            this.isCompetencesArray = Array.isArray(this.projet.competences);
            this.isCompetencesString = typeof this.projet.competences === 'string';
          }

          // Nettoyage du lien GitHub si défini
          if (this.projet && this.projet.lien_Git_Hub) {
            this.projet.lien_Git_Hub = this.projet.lien_Git_Hub.trim();
          }
        },
        error: (err) => {
          console.error('Erreur lors de la récupération du projet:', err);
        },
      });
  }

  // Fonction pour obtenir l'URL d'une compétence avec une redirection fixe
  getCompetenceLink(competence: string): string {
    // Retourner l'URL fixe pour la compétence
    return this.competenceUrls[competence] || '#'; // URL par défaut si la compétence n'est pas définie
  }

  // Méthode pour séparer les compétences si elles sont dans une chaîne
  splitCompetences(competences: string): string[] {
    return competences.split(',').map((comp) => comp.trim());
  }

  // Méthode pour revenir à la page précédente
  goBack(): void {
    this.location.back();
  }
}
