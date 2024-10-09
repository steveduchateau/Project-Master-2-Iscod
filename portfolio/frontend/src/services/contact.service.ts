// Importation des modules nécessaires depuis Angular
import { Injectable } from '@angular/core'; // Importation du décorateur Injectable pour indiquer que la classe peut être injectée comme dépendance
import { HttpClient } from '@angular/common/http'; // Importation de HttpClient pour effectuer des requêtes HTTP
import { Observable } from 'rxjs'; // Importation de Observable pour travailler avec des flux de données asynchrones

// Déclaration du service en tant que fournisseur injectable dans toute l'application
@Injectable({
  providedIn: 'root' // Spécifie que le service sera disponible dans toute l'application
})
// Définition de la classe du service
export class ContactService {
  // URL de l'API pour envoyer les données de contact
  private apiUrl = 'https://portfolio-backend.onrender.com/api/contact'; // URL de l'API Flask pour la gestion des contacts

  // Constructeur du service, injecte le client HTTP pour effectuer des requêtes
  constructor(private http: HttpClient) { }

  // Méthode pour envoyer le formulaire de contact
  sendContactForm(data: any): Observable<any> {
    // Effectue une requête POST vers l'URL de l'API avec les données du formulaire
    return this.http.post<any>(this.apiUrl, data);
  }
}







