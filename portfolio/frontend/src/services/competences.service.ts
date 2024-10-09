// Importation des modules nécessaires depuis Angular
import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { environment } from '../environments/environment'; // Assurez-vous que le chemin est correct

// Définition de l'interface pour le modèle de compétence
export interface Competence {
  nom: string;
  niveau: string;
  description: string;
}

// Déclaration du service en tant que fournisseur injectable dans toute l'application
@Injectable({
  providedIn: 'root'
})
// Définition de la classe du service
export class CompetencesService {
  // URL de l'API pour accéder aux données des compétences techniques et humaines
  private apiUrlTechniques = environment.apiUrlTechniques; // Utilisation de l'URL de production
  private apiUrlHumaines = environment.apiUrlHumaines; // Utilisation de l'URL de production

  // Constructeur du service, injecte le client HTTP pour effectuer des requêtes
  constructor(private http: HttpClient) {}

  // Méthode pour récupérer les compétences techniques depuis l'API
  getCompetencesTechniques(): Observable<Competence[]> {
    return this.http.get<Competence[]>(this.apiUrlTechniques).pipe(
      catchError(this.handleError)
    );
  }

  // Méthode pour récupérer les compétences humaines depuis l'API
  getCompetencesHumaines(): Observable<Competence[]> {
    return this.http.get<Competence[]>(this.apiUrlHumaines).pipe(
      catchError(this.handleError)
    );
  }

  // Méthode générique pour récupérer les compétences en fonction du type
  getCompetences(type: 'techniques' | 'humaines'): Observable<Competence[]> {
    const url = type === 'techniques' ? this.apiUrlTechniques : this.apiUrlHumaines;
    return this.http.get<Competence[]>(url).pipe(
      catchError(this.handleError)
    );
  }

  // Méthode pour gérer les erreurs
  private handleError(error: HttpErrorResponse) {
    console.error('Une erreur est survenue:', error.message);
    return throwError(() => new Error('Erreur lors de la récupération des données.'));
  }
}
