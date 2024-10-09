// Importation des modules nécessaires depuis Angular
import { Injectable } from '@angular/core'; // Importation de 'Injectable' pour définir un service injectable
import { HttpClient, HttpErrorResponse } from '@angular/common/http'; // Importation de 'HttpClient' et 'HttpErrorResponse' pour gérer les requêtes HTTP et les erreurs
import { Observable, throwError } from 'rxjs'; // Importation de 'Observable' et 'throwError' pour gérer les flux de données asynchrones et les erreurs
import { catchError } from 'rxjs/operators'; // Importation de 'catchError' pour gérer les erreurs dans les flux de données

// Définition de l'interface pour le modèle de compétence
export interface Competence {
  nom: string;
  niveau: string;
  description: string;
}

// Déclaration du service en tant que fournisseur injectable dans toute l'application
@Injectable({
  providedIn: 'root' // Spécifie que le service sera disponible dans toute l'application
})
// Définition de la classe du service
export class CompetencesService {
  // URL de l'API pour accéder aux données des compétences techniques et humaines
  private apiUrlTechniques = 'https://project-master-2-iscod.onrender.com/api/competences/techniques';
  private apiUrlHumaines = 'https://project-master-2-iscod.onrender.com/api/competences/humaines';

  // Constructeur du service, injecte le client HTTP pour effectuer des requêtes
  constructor(private http: HttpClient) {}

  // Méthode pour récupérer les compétences techniques depuis l'API
  getCompetencesTechniques(): Observable<Competence[]> {
    return this.http.get<Competence[]>(this.apiUrlTechniques).pipe(
      catchError(this.handleError) // Gestion des erreurs
    );
  }

  // Méthode pour récupérer les compétences humaines depuis l'API
  getCompetencesHumaines(): Observable<Competence[]> {
    return this.http.get<Competence[]>(this.apiUrlHumaines).pipe(
      catchError(this.handleError) // Gestion des erreurs
    );
  }

  // Méthode générique pour récupérer les compétences en fonction du type
  getCompetences(type: 'techniques' | 'humaines'): Observable<Competence[]> {
    const url = type === 'techniques' ? this.apiUrlTechniques : this.apiUrlHumaines;
    return this.http.get<Competence[]>(url).pipe(
      catchError(this.handleError) // Gestion des erreurs
    );
  }

  // Méthode pour gérer les erreurs
  private handleError(error: HttpErrorResponse) {
    console.error('Une erreur est survenue:', error.message); // Affichage de l'erreur dans la console
    return throwError(() => new Error('Erreur lors de la récupération des données.'));
  }
}