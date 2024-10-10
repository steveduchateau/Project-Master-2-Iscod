import { Component } from '@angular/core'; // Importation du décorateur Component pour définir un composant Angular
import { FormsModule } from '@angular/forms'; // Importation de FormsModule pour gérer les formulaires et la liaison des données
import { ContactService } from '../services/contact.service';

// Définition du composant ContactComponent
@Component({
  selector: 'app-contact', // Sélecteur du composant utilisé dans les templates HTML pour l'inclure
  standalone: true, // Indique que ce composant est autonome et n'a pas besoin d'être déclaré dans un module Angular
  templateUrl: './contact.component.html', // Chemin vers le fichier HTML du template du composant
  styleUrls: ['./contact.component.scss'], // Chemin vers le fichier SCSS pour les styles du composant
  imports: [FormsModule] // Importation du FormsModule pour utiliser les fonctionnalités des formulaires
})
export class ContactComponent {
  // Déclaration d'un objet contact pour stocker les données du formulaire
  contact = {
    first_Name: '', // Champ pour le prénom (modifié)
    last_Name: '', // Champ pour le nom de famille (modifié)
    email: '', // Champ pour l'adresse email
    message: '' // Champ pour le message
  };

  // Injection du service ContactService dans le constructeur pour permettre l'envoi des données
  constructor(private contactService: ContactService) {}

  // Méthode appelée lors de la soumission du formulaire
  onSubmit(): void {
    // Vérifie que tous les champs du formulaire sont remplis
    if (this.contact.first_Name && this.contact.last_Name && this.contact.email && this.contact.message) {
      // Appelle la méthode sendContactForm du ContactService pour envoyer les données du formulaire au serveur
      this.contactService.sendContactForm(this.contact).subscribe({
        // Gestion de la réponse du serveur en cas de succès
        next: (response) => {
          console.log('Message envoyé !', response); // Affiche une confirmation dans la console
          alert('Message envoyé avec succès !'); // Affiche une alerte pour indiquer le succès de l'envoi
          // Réinitialise le formulaire après l'envoi réussi
          this.contact = { first_Name: '', last_Name: '', email: '', message: '' }; // Réinitialisation modifiée
        },
        // Gestion des erreurs en cas d'échec de l'envoi
        error: (error) => {
          console.error('Erreur lors de l\'envoi du message', error); // Affiche l'erreur dans la console
          alert('Erreur lors de l\'envoi du message.'); // Affiche une alerte pour indiquer l'échec de l'envoi
        }
      });
    } else {
      // Affiche une alerte si des champs du formulaire sont manquants
      alert('Tous les champs doivent être remplis');
    }
  }
}
