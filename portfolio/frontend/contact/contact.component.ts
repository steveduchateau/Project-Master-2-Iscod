import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { FormsModule } from '@angular/forms'; // Importez FormsModule ici

@Component({
  selector: 'app-contact',
  standalone: true,
  templateUrl: './contact.component.html',
  styleUrls: ['./contact.component.scss'],
  imports: [FormsModule] // Ajoutez FormsModule dans imports
})
export class ContactComponent {
  contact = {
    firstName: '',
    lastName: '',
    email: '',
    message: ''
  };

  private apiUrl = 'http://localhost:3000/contact'; // Assurez-vous que l'URL de l'API est correcte

  constructor(private http: HttpClient) {}

  onSubmit(): void {
    if (this.contact.firstName && this.contact.lastName && this.contact.email && this.contact.message) {
      this.http.post(this.apiUrl, this.contact).subscribe({
        next: (response) => {
          console.log('Message envoyé !', response);
          alert('Message envoyé avec succès !'); // Affiche un message de succès
          this.contact = { firstName: '', lastName: '', email: '', message: '' }; // Réinitialiser le formulaire
        },
        error: (error) => {
          console.error('Erreur lors de l\'envoi du message', error);
          alert('Erreur lors de l\'envoi du message.'); // Affiche un message d'erreur
        }
      });
    } else {
      alert('Tous les champs doivent être remplis');
    }
  }
}
