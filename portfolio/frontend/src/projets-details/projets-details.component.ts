import { Component, OnInit } from '@angular/core'; // Importation de la classe Component et OnInit de Angular
import { ActivatedRoute } from '@angular/router'; // Importation de ActivatedRoute pour accéder aux paramètres de la route
import { ProjetsService } from '../services/projets.service'; // Importation du service ProjetsService pour interagir avec les données des projets
import { Location } from '@angular/common'; // Importation de Location pour manipuler l'historique de navigation
import { CommonModule } from '@angular/common'; // Importation du CommonModule pour utiliser les directives Angular communes
import { switchMap, catchError } from 'rxjs/operators'; // Importation des opérateurs RxJS pour transformer et gérer les erreurs des flux de données
import { throwError } from 'rxjs'; // Importation de throwError pour générer des erreurs dans les observables

@Component({
  selector: 'app-projets-details',  // Sélecteur pour utiliser ce composant dans les templates
  standalone: true,  // Indique que ce composant utilise une approche autonome pour les modules
  templateUrl: './projets-details.component.html',  // Chemin vers le template HTML du composant
  styleUrls: ['./projets-details.component.scss'],  // Chemin vers le fichier de styles SCSS du composant
  imports: [CommonModule],  // Modules Angular nécessaires pour ce composant
})
export class ProjetsDetailsComponent implements OnInit {
  projet: any;  // Variable pour stocker les détails du projet

  constructor(
    private route: ActivatedRoute,  // Service pour accéder aux paramètres de la route active
    private projetsService: ProjetsService,  // Service pour obtenir les données du projet
    private location: Location  // Service pour manipuler l'historique de navigation
  ) {}

  ngOnInit(): void {
    // Lors de l'initialisation du composant, récupérer les détails du projet
    this.route.paramMap.pipe(
      switchMap(params => {
        // Obtenir l'ID du projet depuis les paramètres de la route
        const id = params.get('id');
        if (id) {
          // Si l'ID est présent, utiliser le service pour récupérer les détails du projet
          return this.projetsService.getProjetById(id);
        } else {
          // Si l'ID est manquant, générer une erreur
          return throwError(() => new Error('ID de projet manquant'));
        }
      }),
      catchError(err => {
        // Gérer les erreurs qui surviennent lors de la récupération des données
        console.error('Erreur lors de la récupération du projet:', err);
        return throwError(() => err);  // Propager l'erreur pour gestion ultérieure
      })
    ).subscribe({
      next: (data) => {
        // Lorsque les données sont reçues, les stocker dans la variable projet
        this.projet = data;
        console.log('Projet:', this.projet);  // Afficher les données reçues pour le débogage

        // Assurez-vous que le lien GitHub est bien défini
        if (this.projet && this.projet.lien_Git_Hub) {
          this.projet.lien_Git_Hub = this.projet.lien_Git_Hub.trim();  // Éliminer les espaces superflus
        }
      },
      error: (err) => {
        // Gérer les erreurs survenues lors de la souscription
        console.error('Erreur lors de la récupération du projet:', err);
      }
    });
  }

  goBack(): void {
    // Méthode pour revenir à la page précédente en utilisant le service Location
    this.location.back();
  }
}
