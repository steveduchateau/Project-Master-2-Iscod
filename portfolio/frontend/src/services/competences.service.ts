import { Injectable } from '@angular/core'; // Définir un service injectable
import { HttpClient, HttpErrorResponse } from '@angular/common/http'; // Gérer les requêtes HTTP et les erreurs
import { Observable, throwError } from 'rxjs'; // Gérer les flux de données et les erreurs
import { catchError } from 'rxjs/operators'; // Gérer les erreurs dans les flux

// Interface pour définir le modèle de compétence
export interface Competence {
  id?: number; // Ajout de l'ID (optionnel)
  nom: string;
  niveau: string;
  description: string;
  lien_Git_Hub?: string; // Champ optionnel pour les liens GitHub
}

// Service injectable
@Injectable({
  providedIn: 'root',
})
export class CompetencesService {
  // URLs des API
  private apiUrlTechniques = 'https://project-master-2-iscod.onrender.com/api/competences/techniques';
  private apiUrlHumaines = 'https://project-master-2-iscod.onrender.com/api/competences/humaines';
  private apiUrlCompetenceById = 'https://project-master-2-iscod.onrender.com/api/competences'; // Base pour récupérer par ID

  constructor(private http: HttpClient) {}

  // Récupérer les compétences techniques
  getCompetencesTechniques(): Observable<Competence[]> {
    return this.http.get<Competence[]>(this.apiUrlTechniques).pipe(
      catchError(this.handleError)
    );
  }

  // Récupérer les compétences humaines
  getCompetencesHumaines(): Observable<Competence[]> {
    return this.http.get<Competence[]>(this.apiUrlHumaines).pipe(
      catchError(this.handleError)
    );
  }

  // Récupérer les compétences en fonction du type (techniques ou humaines)
  getCompetences(type: 'techniques' | 'humaines'): Observable<Competence[]> {
    const url = type === 'techniques' ? this.apiUrlTechniques : this.apiUrlHumaines;
    return this.http.get<Competence[]>(url).pipe(
      catchError(this.handleError)
    );
  }

  // **Nouvelle méthode** : Récupérer une compétence par ID
  getCompetenceById(id: number): Observable<Competence> {
    const url = `${this.apiUrlCompetenceById}/${id}`; // Construire l'URL avec l'ID
    return this.http.get<Competence>(url).pipe(
      catchError(this.handleError)
    );
  }

  // Gestion des erreurs
  private handleError(error: HttpErrorResponse) {
    console.error('Une erreur est survenue:', error.message);
    return throwError(() => new Error('Erreur lors de la récupération des données.'));
  }
}
