import { Component, OnInit } from '@angular/core'; // Importation des classes Component et OnInit pour définir et initialiser le composant Angular
import { ActivatedRoute } from '@angular/router'; // Importation de ActivatedRoute pour accéder aux paramètres de la route active
import { ProjetsService } from '../services/projets.service'; // Importation du service ProjetsService pour obtenir les données du projet
import { Location } from '@angular/common'; // Importation de Location pour manipuler l'historique de navigation
import { CommonModule } from '@angular/common'; // Importation de CommonModule pour utiliser des directives Angular communes
import { switchMap, catchError } from 'rxjs/operators'; // Importation des opérateurs RxJS pour transformer les flux de données et gérer les erreurs
import { throwError } from 'rxjs'; // Importation de throwError pour créer des erreurs dans les observables

@Component({
  selector: 'app-projets-details',  // Déclaration du sélecteur du composant pour l'utiliser dans les templates HTML
  standalone: true,  // Indique que le composant est autonome, ce qui signifie qu'il n'a pas besoin d'être inclus dans un module Angular spécifique
  templateUrl: './projets-details.component.html',  // Chemin vers le fichier de template HTML associé au composant
  styleUrls: ['./projets-details.component.scss'],  // Chemin vers le fichier de styles SCSS associé au composant
  imports: [CommonModule],  // Modules Angular nécessaires pour ce composant, ici le CommonModule pour les directives comme *ngIf
})
export class ProjetsDetailsComponent implements OnInit {
  projet: any;  // Variable pour stocker les détails du projet récupérés depuis le service

  constructor(
    private route: ActivatedRoute,  // Service pour accéder aux paramètres de la route active, tel que l'ID du projet dans l'URL
    private projetsService: ProjetsService,  // Service pour obtenir les données du projet à partir d'une API ou d'une autre source
    private location: Location  // Service pour manipuler l'historique de navigation, permettant de revenir à la page précédente
  ) {}

  ngOnInit(): void {
    // Méthode appelée lors de l'initialisation du composant, utilisée pour récupérer les données du projet
    this.route.paramMap.pipe(
      switchMap(params => {
        // Utilisation de switchMap pour transformer les données du flux de paramètres de la route
        const id = params.get('id');  // Récupération de l'ID du projet à partir des paramètres de la route
        if (id) {
          // Vérification que l'ID est présent
          return this.projetsService.getProjetById(id);  // Utilisation du service pour récupérer les détails du projet par son ID
        } else {
          // Gestion du cas où l'ID est manquant
          return throwError(() => new Error('ID de projet manquant'));  // Création et propagation d'une erreur si l'ID est absent
        }
      }),
      catchError(err => {
        // Gestion des erreurs qui surviennent lors de la récupération des données
        console.error('Erreur lors de la récupération du projet:', err);  // Affichage de l'erreur dans la console pour le débogage
        return throwError(() => err);  // Propagation de l'erreur pour une gestion ultérieure
      })
    ).subscribe({
      next: (data) => {
        // Lorsque les données du projet sont reçues
        this.projet = data;  // Stockage des données du projet dans la variable projet
        console.log('Projet:', this.projet);  // Affichage des données du projet dans la console pour le débogage

        // Assurez-vous que le lien GitHub est bien défini
        if (this.projet && this.projet.lien_Git_Hub) {
          this.projet.lien_Git_Hub = this.projet.lien_Git_Hub.trim();  // Suppression des espaces superflus autour du lien GitHub
        }
      },
      error: (err) => {
        // Gestion des erreurs lors de la souscription
        console.error('Erreur lors de la récupération du projet:', err);  // Affichage de l'erreur dans la console pour le débogage
      }
    });
  }

  goBack(): void {
    // Méthode pour revenir à la page précédente
    this.location.back();  // Utilisation du service Location pour naviguer vers la page précédente dans l'historique de navigation
  }
}
