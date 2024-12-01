import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { CompetencesService } from '../services/competences.service';  // Service pour récupérer les compétences
import { Location } from '@angular/common';  // Service pour manipuler l'historique de navigation
import { CommonModule } from '@angular/common';  // Module nécessaire pour directives Angular de base
import { switchMap, catchError } from 'rxjs/operators';  // Opérateurs RxJS pour la gestion des flux de données et des erreurs
import { throwError } from 'rxjs';  // Permet de générer des erreurs dans les observables

@Component({
  selector: 'app-competence-details-dialog',  // Sélecteur pour le composant
  standalone: true,  // Composant autonome
  templateUrl: './competence-details-dialog.component.html',  // Chemin vers le fichier HTML
  styleUrls: ['./competence-details-dialog.component.scss'],  // Chemin vers le fichier SCSS
  imports: [CommonModule],  // Importation des modules nécessaires
})
export class CompetenceDetailsComponent implements OnInit {
  competence: any;  // Variable pour stocker les données de la compétence récupérées

  constructor(
    private route: ActivatedRoute,  // Pour récupérer les paramètres de la route (ID de la compétence)
    private competencesService: CompetencesService,  // Service pour obtenir les compétences
    private location: Location  // Pour gérer la navigation vers la page précédente
  ) {}

  ngOnInit(): void {
    // Méthode appelée lors de l'initialisation du composant
    this.route.paramMap.pipe(
      switchMap(params => {
        const id = params.get('id');  // Récupération de l'ID de la compétence dans les paramètres de la route
        if (id) {
          // Si l'ID est présent, on récupère les détails de la compétence via le service
          return this.competencesService.getCompetenceById(id);
        } else {
          // Si l'ID est manquant, on lance une erreur
          return throwError(() => new Error('ID de compétence manquant'));
        }
      }),
      catchError(err => {
        console.error('Erreur lors de la récupération de la compétence:', err);
        return throwError(() => err);
      })
    ).subscribe({
      next: (data) => {
        this.competence = data;  // Stockage des données dans la variable competence
        console.log('Compétence:', this.competence);
        
        // Assurez-vous que le lien GitHub est bien défini (si nécessaire)
        if (this.competence && this.competence.lien_Git_Hub) {
          this.competence.lien_Git_Hub = this.competence.lien_Git_Hub.trim();
        }
      },
      error: (err) => {
        console.error('Erreur lors de la récupération de la compétence:', err);
      }
    });
  }

  goBack(): void {
    this.location.back();  // Revenir à la page précédente
  }
}
