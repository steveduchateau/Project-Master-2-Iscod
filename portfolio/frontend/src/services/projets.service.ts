// Importation des modules nécessaires depuis Angular
import { Injectable } from '@angular/core'; // Importation du décorateur Injectable pour permettre l'injection de dépendances
import { HttpClient } from '@angular/common/http'; // Importation de HttpClient pour effectuer des requêtes HTTP
import { Observable } from 'rxjs'; // Importation de Observable pour la gestion des flux de données asynchrones

// Déclaration du service en tant que fournisseur injectable dans toute l'application
@Injectable({
  providedIn: 'root' // Spécifie que le service sera disponible dans toute l'application
})
// Définition de la classe du service
export class ProjetsService {
  // URL de l'API pour accéder aux projets
  private apiUrl = 'http://127.0.0.1:5001/api/projets'; // URL de l'API Flask pour la gestion des projets

  // Constructeur du service, injecte le client HTTP pour effectuer des requêtes
  constructor(private http: HttpClient) {}

  // Méthode pour obtenir la liste des projets
  getProjets(): Observable<any[]> {
    // Effectue une requête GET vers l'URL de l'API pour récupérer tous les projets
    return this.http.get<any[]>(this.apiUrl);
  }

  // Méthode pour obtenir les détails d'un projet par son ID
  getProjetById(id: string): Observable<any> {
    // Effectue une requête GET vers l'URL de l'API pour récupérer un projet spécifique en fonction de son ID
    return this.http.get<any>(`${this.apiUrl}/${id}`);
  }
}
