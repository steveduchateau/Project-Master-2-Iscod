import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { CompetencesService } from '../services/competences.service';
import { Location } from '@angular/common';
import { CommonModule } from '@angular/common';
import { switchMap, catchError } from 'rxjs/operators';
import { throwError } from 'rxjs';

// Interfaces pour structurer les données des compétences et des anecdotes
export interface Anecdote {
  titre: string;
  description: string;
  resultat: string;
  lien_realisations: string;
}

export interface CompetenceData {
type: any;
  id: number;
  nom: string;
  description: string;
  contexte?: string;
  objectifs?: string;
  enjeux?: string;
  risques?: string;
  etapes?: string;
  competences?: string;
  regardCritique?: string;
  anecdotes?: Anecdote[];
  cas_utilisation?: string;
  conseils_experience?: string;
  formations_en_cours?: string;
  importance_profil?: string;
  marge_progression?: string;
  niveau?: string;
  niveau_maitrise?: string;
  objectif_moyen_terme?: string;
  utilisation?: string;
  vitesse_acquisition?: string;
}

@Component({
  selector: 'app-competence-details',
  standalone: true,
  templateUrl: './competence-details.component.html',
  styleUrls: ['./competence-details.component.scss'],
  imports: [CommonModule],
})
export class CompetenceDetailsComponent implements OnInit {
  competence: CompetenceData | null = null; // Stocke les détails de la compétence
  isLoading: boolean = true; // Indicateur de chargement
  errorMessage: string | null = null; // Message d'erreur

  constructor(
    private route: ActivatedRoute,
    private competencesService: CompetencesService,
    private location: Location
  ) {}

  ngOnInit(): void {
    this.isLoading = true; // Commence le chargement

    this.route.paramMap
      .pipe(
        switchMap((params) => {
          const id = params.get('id');
          const type = params.get('type') as 'techniques' | 'humaines';

          if (id && type) {
            return this.competencesService.getCompetenceById(type, +id); // Conversion de l'ID en nombre
          } else {
            return throwError(() => new Error('ID ou type de compétence manquant'));
          }
        }),
        catchError((err) => {
          console.error('Erreur lors de la récupération de la compétence:', err);
          this.errorMessage = 'Impossible de récupérer les détails de la compétence.';
          this.isLoading = false;
          return throwError(() => err);
        })
      )
      .subscribe({
        next: (data) => {
          // Assurez-vous que les données reçues sont bien de type CompetenceData
          if (data && 'id' in data) {
            this.competence = data as CompetenceData;
          } else {
            console.error('Données de compétence non valides, manque de l\'ID');
            this.errorMessage = 'Les détails de la compétence sont incomplets.';
            this.isLoading = false;
            return;
          }

          // Tentative de parsing des anecdotes si elles existent et si elles sont sous forme de chaîne
          if (this.competence?.anecdotes && typeof this.competence.anecdotes === 'string') {
            try {
              this.competence.anecdotes = JSON.parse(this.competence.anecdotes);
            } catch (error) {
              console.error('Erreur de parsing des anecdotes :', error);
            }
          }

          console.log('Compétence:', this.competence);
          this.isLoading = false;
        },
        error: (err) => {
          console.error('Erreur lors de la récupération des détails de la compétence:', err);
          this.errorMessage = 'Une erreur est survenue. Veuillez réessayer plus tard.';
          this.isLoading = false;
        },
      });
  }

  goBack(): void {
    this.location.back(); // Retour à la page précédente
  }
}
