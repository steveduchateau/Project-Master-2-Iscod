// Importation des modules nécessaires depuis Angular
import { Injectable } from '@angular/core'; // Importation du décorateur Injectable pour permettre l'injection de dépendances
import { HttpClient } from '@angular/common/http'; // Importation de HttpClient pour effectuer des requêtes HTTP
import { Observable } from 'rxjs'; // Importation de Observable pour gérer les flux de données asynchrones
import { environment } from '../environments/environment'; // Importation des variables d'environnement

// Déclaration de la classe ProjetsService en tant que fournisseur injectable dans toute l'application
@Injectable({
  providedIn: 'root' // Spécifie que le service sera disponible dans toute l'application
})
export class ProjetsService {
  // URL de l'API pour accéder aux projets, récupérée des variables d'environnement
  private apiUrl = environment.apiUrlProjets; // Utilise l'URL des projets depuis l'environnement

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
