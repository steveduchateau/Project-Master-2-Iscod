import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatButtonModule } from '@angular/material/button';
import { CompetencesService } from '../services/competences.service';
import { Router } from '@angular/router'; // Importation du Router pour la navigation

@Component({
  selector: 'app-skills',
  standalone: true,
  templateUrl: './skills.component.html',
  styleUrls: ['./skills.component.scss'],
  providers: [CompetencesService],
  imports: [CommonModule, MatButtonModule]
})
export class SkillsComponent implements OnInit {
  competences: any[] = [];
  hardSkills: any[] = [];
  softSkills: any[] = [];

  constructor(
    private competencesService: CompetencesService,
    private router: Router,  // Injection du Router
    private cdr: ChangeDetectorRef
  ) {}

  ngOnInit(): void {
    // Récupération des compétences
    this.competencesService.getCompetences('techniques').subscribe(
      (data: any[]) => {
        this.hardSkills = data;
        this.cdr.detectChanges();
      },
      (error) => {
        console.error('Erreur lors de la récupération des compétences techniques', error);
      }
    );

    this.competencesService.getCompetences('humaines').subscribe(
      (data: any[]) => {
        this.softSkills = data;
        this.cdr.detectChanges();
      },
      (error) => {
        console.error('Erreur lors de la récupération des compétences humaines', error);
      }
    );
  }

  // Méthode pour rediriger vers la page de détails d'une compétence
  goToDetails(competenceId: number): void {
    // Redirection vers la page de détails avec l'ID de la compétence
    this.router.navigate(['/competence', competenceId]);
  }
}
