import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';

/**
 * Composant pour afficher les détails d'une compétence sur une page unique.
 */
@Component({
  selector: 'app-competence-details',
  standalone: true,
  templateUrl: './competence-details-dialog.component.html',
  styleUrls: ['./competence-details-dialog.component.scss'],
  imports: [CommonModule, HttpClientModule],
})
export class CompetenceDetailsDialogComponent implements OnInit {
  competence: any; // Variable pour stocker les détails de la compétence
  anecdotes: any[] = []; // Variable pour stocker les anecdotes désérialisées

  /**
   * Constructeur du composant.
   * @param route Permet d'accéder aux paramètres de l'URL.
   * @param http Permet de faire des appels API.
   */
  constructor(private route: ActivatedRoute, private http: HttpClient) {}

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
    // Utilisez l'URL correcte
    const url = `https://project-master-2-iscod.onrender.com/api/competences/${id}`;

    this.http.get(url).subscribe({
      next: (data: any) => {
        this.competence = data;

        // Désérialisation des anecdotes si elles sont en chaîne JSON
        if (data?.anecdotes) {
          if (typeof data.anecdotes === 'string') {
            try {
              this.anecdotes = JSON.parse(data.anecdotes);
            } catch (error) {
              console.error('Erreur lors de la désérialisation des anecdotes:', error);
            }
          } else if (Array.isArray(data.anecdotes)) {
            this.anecdotes = data.anecdotes;
          }
        }
      },
      error: (err) => {
        console.error('Erreur lors du chargement des données de la compétence:', err);
      },
    });
  }
}
