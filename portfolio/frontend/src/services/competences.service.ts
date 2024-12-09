import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';

// Définition de l'interface pour le modèle de compétence
export interface Competence {
  nom: string;
  niveau: string;
  description: string;
  lien_Git_Hub?: string; // Propriété optionnelle pour le lien GitHub
  type: 'techniques' | 'humaines'; // Correspondance exacte avec l'API backend
}

@Injectable({
  providedIn: 'root', // Spécifie que le service est injectable dans toute l'application
})
export class CompetencesService {
  private baseUrl = 'https://project-master-2-iscod.onrender.com/api/competences';

  constructor(private http: HttpClient) {}

  /**
   * Récupère une compétence par ID et type.
   * @param type Le type de compétence (techniques ou humaines).
   * @param id L'identifiant de la compétence.
   */
  getCompetenceById(type: 'techniques' | 'humaines', id: number): Observable<Competence | null> {
    const url = `${this.baseUrl}/${type}/${id}`; // URL dynamique avec type et ID
    return this.http.get<Competence>(url).pipe(
      catchError(this.handleError) // Gestion des erreurs
    );
  }

  /**
   * Récupère toutes les compétences d'un type donné.
   * @param type Le type de compétence (techniques ou humaines).
   */
  getCompetences(type: 'techniques' | 'humaines'): Observable<Competence[]> {
    const url = `${this.baseUrl}/${type}`; // URL dynamique avec type
    return this.http.get<Competence[]>(url).pipe(
      catchError(this.handleError) // Gestion des erreurs
    );
  }

  /**
   * Gestionnaire d'erreurs pour les requêtes HTTP.
   * @param error L'erreur HTTP reçue.
   */
  private handleError(error: HttpErrorResponse) {
    console.error('Une erreur est survenue:', error.message); // Log de l'erreur dans la console
    return throwError(() => new Error('Erreur lors de la récupération des données.')); // Retourne une erreur observable
  }
}
