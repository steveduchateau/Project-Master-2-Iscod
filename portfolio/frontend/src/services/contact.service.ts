// Importation des modules nécessaires depuis Angular
import { Injectable } from '@angular/core'; // Importation du décorateur Injectable pour permettre l'injection de dépendances
import { HttpClient } from '@angular/common/http'; // Importation de HttpClient pour effectuer des requêtes HTTP
import { Observable } from 'rxjs'; // Importation de Observable pour gérer les flux de données asynchrones
import { environment } from '../environments/environment'; // Importation des variables d'environnement

// Déclaration de la classe ContactService en tant que fournisseur injectable dans toute l'application
@Injectable({
  providedIn: 'root' // Spécifie que le service sera disponible dans toute l'application
})
export class ContactService {
  // URL de l'API pour envoyer les données de contact, récupérée des variables d'environnement
  private apiUrl = environment.apiUrlContact; // Utilise l'URL de contact depuis l'environnement

  // Constructeur du service, injecte le client HTTP pour effectuer des requêtes
  constructor(private http: HttpClient) {}

  // Méthode pour envoyer le formulaire de contact
  sendContactForm(data: any): Observable<any> {
    // Effectue une requête POST vers l'URL de l'API avec les données du formulaire
    return this.http.post<any>(this.apiUrl, data);
  }
}
