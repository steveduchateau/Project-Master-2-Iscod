import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { CommonModule } from '@angular/common';

/**
 * Composant pour afficher les détails d'une compétence sur une page unique.
 */
@Component({
  selector: 'app-competence-details',
  standalone: true, // Indique que ce composant peut être utilisé seul, sans module Angular spécifique
  templateUrl: './competence-details-dialog.component.html', // Fichier template HTML pour ce composant
  styleUrls: ['./competence-details-dialog.component.scss'], // Fichier SCSS pour les styles de ce composant
  imports: [CommonModule] // Modules Angular nécessaires pour ce composant
})
export class CompetenceDetailsDialogComponent implements OnInit {
  
  competence: any; // Variable pour stocker les détails de la compétence
  anecdotes: any[] = []; // Variable pour stocker les anecdotes désérialisées

  /**
   * Constructeur du composant.
   * @param route Permet d'accéder aux paramètres de l'URL.
   * @param http Permet de faire des appels API.
   */
  constructor(
    private route: ActivatedRoute, 
    private http: HttpClient
  ) {}

  /**
   * Méthode d'initialisation du composant.
   */
  ngOnInit(): void {
    const competenceId = this.route.snapshot.paramMap.get('id'); // Récupère l'ID de la compétence depuis l'URL
    if (competenceId) {
      this.loadCompetence(competenceId); // Charge les données de la compétence
    }
  }

  /**
   * Charge les données de la compétence via une API.
   * @param id ID de la compétence à récupérer.
   */
  loadCompetence(id: string): void {
    this.http.get(`/api/competences/${id}`).subscribe((data: any) => {
      this.competence = data;

      // Désérialisation des anecdotes si elles sont en chaîne JSON
      if (typeof data.anecdotes === 'string') {
        try {
          this.anecdotes = JSON.parse(data.anecdotes);
        } catch (error) {
          console.error('Erreur lors de la désérialisation des anecdotes:', error);
        }
      } else {
        this.anecdotes = data.anecdotes;
      }
    });
  }
}
