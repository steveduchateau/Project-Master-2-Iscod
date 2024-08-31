// Importation des modules nécessaires depuis Angular
import { Injectable } from '@angular/core'; // Importation de 'Injectable' pour définir un service injectable
import { HttpClient } from '@angular/common/http'; // Importation de 'HttpClient' pour effectuer des requêtes HTTP
import { Observable } from 'rxjs'; // Importation de 'Observable' pour gérer les flux de données asynchrones

// Déclaration du service en tant que fournisseur injectable dans toute l'application
@Injectable({
  providedIn: 'root' // Spécifie que le service sera disponible dans toute l'application
})
// Définition de la classe du service
export class CompetencesService {
  // URL de l'API pour accéder aux données des compétences
  private apiUrl = 'http://127.0.0.1:5001/api/competences';

  // Constructeur du service, injecte le client HTTP pour effectuer des requêtes
  constructor(private http: HttpClient) {}

  // Méthode pour récupérer les compétences depuis l'API
  getCompetences(): Observable<any[]> {
    // Effectue une requête GET vers l'URL de l'API et retourne un Observable de tableau d'objets
    return this.http.get<any[]>(this.apiUrl);
  }
}
