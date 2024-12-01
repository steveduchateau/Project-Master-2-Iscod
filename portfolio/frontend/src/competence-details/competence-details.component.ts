import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-competence-details',
  templateUrl: './competence-details.component.html',
  styleUrls: ['./competence-details.component.scss'],
  standalone: true,
  imports: [CommonModule, HttpClientModule],
})
export class CompetenceDetailsComponent implements OnInit {
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
    const url = `http://localhost:5001/api/competences/${type}/${id}`;
    this.http.get(url).subscribe((data: any) => {
      this.competence = data;
      if (data.anecdotes) {
        this.anecdotes = data.anecdotes;
      }
    });
  }
}
