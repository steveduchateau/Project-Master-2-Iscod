// Importation des modules nécessaires depuis Angular
import { Injectable } from '@angular/core'; // Importation du décorateur Injectable pour permettre l'injection de dépendances
import { HttpClient } from '@angular/common/http'; // Importation de HttpClient pour effectuer des requêtes HTTP
import { Observable } from 'rxjs'; // Importation de Observable pour la gestion des flux de données asynchrones

// Déclaration du service en tant que fournisseur injectable dans toute l'application
@Injectable({
  providedIn: 'root' // Spécifie que le service sera disponible dans toute l'application
})
// Définition de la classe du service
export class ContactService {
  // URL de l'API pour accéder aux messages de contact
  private apiUrl = 'https://portfolio-backend.onrender.com/api/contact'; // Nouvelle URL de l'API Flask pour la gestion des messages de contact

  // Constructeur du service, injecte le client HTTP pour effectuer des requêtes
  constructor(private http: HttpClient) {}

  // Méthode pour envoyer un message de contact
  sendMessage(contactData: any): Observable<any> {
    // Effectue une requête POST vers l'URL de l'API pour envoyer un message de contact
    return this.http.post<any>(this.apiUrl, contactData);
  }
}
