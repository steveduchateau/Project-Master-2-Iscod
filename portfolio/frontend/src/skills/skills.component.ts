import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatButtonModule } from '@angular/material/button';
import { CompetencesService } from '../services/competences.service';
import { Router, RouterModule } from '@angular/router';

@Component({
  selector: 'app-skills',
  standalone: true,
  templateUrl: './skills.component.html',
  styleUrls: ['./skills.component.scss'],
  providers: [CompetencesService],
  imports: [CommonModule, MatButtonModule, RouterModule] // Ajout de RouterModule
})
export class SkillsComponent implements OnInit {
  competences: any[] = [];
  hardSkills: any[] = [];
  softSkills: any[] = [];
  skill: any;

  constructor(
    private competencesService: CompetencesService,
    private router: Router,
    private cdr: ChangeDetectorRef
  ) {}

  ngOnInit(): void {
    // Récupération des compétences techniques
    this.competencesService.getCompetences('techniques').subscribe(
      (data: any[]) => {
        this.hardSkills = data;
        this.cdr.detectChanges();
      },
      (error) => {
        console.error('Erreur lors de la récupération des compétences techniques', error);
      }
    );

    // Récupération des compétences humaines
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
  goToCompetenceDetails(type: string, competenceId: number): void {
    // Redirection dynamique basée sur le type de compétence
    this.router.navigate(['/competences', type, competenceId]);
  }
}
