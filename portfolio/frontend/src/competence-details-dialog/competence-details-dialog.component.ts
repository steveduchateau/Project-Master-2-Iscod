import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-competence-details-dialog', // Changement du sélecteur pour correspondre à "competence-details-dialog"
  templateUrl: './competence-details-dialog.component.html', // Chemin du template mis à jour
  styleUrls: ['./competence-details-dialog.component.scss'], // Chemin de la feuille de style mise à jour
  standalone: true,
  imports: [CommonModule, HttpClientModule],
})
export class CompetenceDetailsDialogComponent implements OnInit { // Changement du nom de la classe pour correspondre à "CompetenceDetailsDialogComponent"
  competence: any; // Variable pour stocker les détails de la compétence
  anecdotes: any[] = []; // Variable pour stocker les anecdotes désérialisées

  constructor(private route: ActivatedRoute, private http: HttpClient) {}

  ngOnInit(): void {
    const competenceType = this.route.snapshot.paramMap.get('type'); // 'humaines' ou 'techniques'
    const competenceId = this.route.snapshot.paramMap.get('id'); // L'ID de la compétence
    if (competenceType && competenceId) {
      this.loadCompetence(competenceType, competenceId);
    }
  }

  loadCompetence(type: string, id: string): void {
    // Mise à jour de l'URL pour pointer vers l'URL correcte
    const url = `https://project-master-2-iscod.onrender.com/api/competences/${type}/${id}`;
    this.http.get(url).subscribe((data: any) => {
      this.competence = data;
      if (data.anecdotes) {
        this.anecdotes = data.anecdotes;
      }
    });
  }
}
