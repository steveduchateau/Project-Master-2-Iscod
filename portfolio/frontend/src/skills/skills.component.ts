import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
// Importation du service pour récupérer les compétences

// Importation des modules Angular Material pour les dialogues et les boutons
import { MatDialog } from '@angular/material/dialog';
import { CommonModule } from '@angular/common';
import { MatButtonModule } from '@angular/material/button';
// Importation du composant de dialogue pour afficher les détails d'une compétence
import { CompetenceDetailsDialogComponent } from '../competence-details-dialog/competence-details-dialog.component';
import { CompetencesService } from '../services/competences.service';


// Définition du composant Angular
@Component({
  selector: 'app-skills', // Sélecteur pour utiliser ce composant dans les templates HTML
  standalone: true, // Composant autonome, il n'a pas besoin d'un module pour être utilisé
  templateUrl: './skills.component.html', // URL du template HTML associé à ce composant
  styleUrls: ['./skills.component.scss'], // URL de la feuille de style SCSS associée à ce composant
  providers: [CompetencesService], // Déclaration du service comme provider spécifique à ce composant
  imports: [CommonModule, MatButtonModule] // Déclaration des modules nécessaires pour ce composant
})
export class SkillsComponent implements OnInit {
  // Déclaration des propriétés pour stocker les compétences et les différentes catégories
  competences: any[] = [];
  hardSkills: any[] = [];
  softSkills: any[] = [];

  // Injection des dépendances dans le constructeur
  constructor(
    private competencesService: CompetencesService,
    public dialog: MatDialog,
    private cdr: ChangeDetectorRef
  ) {}

  // Méthode exécutée lors de l'initialisation du composant
  ngOnInit(): void {
    // Appel au service pour récupérer les compétences techniques et humaines depuis l'API
    this.competencesService.getCompetences('techniques').subscribe(
      (data: any[]) => {
        this.hardSkills = data;
        console.log('Compétences techniques récupérées :', data); // Affiche les données dans la console pour vérifier
        this.cdr.detectChanges(); // Forcer la détection des changements
      },
      (error) => {
        console.error('Erreur lors de la récupération des compétences techniques', error); // Affiche l'erreur
      }
    );

    this.competencesService.getCompetences('humaines').subscribe(
      (data: any[]) => {
        this.softSkills = data;
        console.log('Compétences humaines récupérées :', data); // Affiche les données dans la console pour vérifier
        this.cdr.detectChanges(); // Forcer la détection des changements
      },
      (error) => {
        console.error('Erreur lors de la récupération des compétences humaines', error); // Affiche l'erreur
      }
    );
  }

  // Méthode pour ouvrir le dialogue des détails d'une compétence
  openDetailsDialog(competence: any): void {
    // Ouverture du dialogue en passant les données de la compétence
    this.dialog.open(CompetenceDetailsDialogComponent, {
      width: '400px', // Largeur du dialogue
      data: competence // Données de la compétence à afficher dans le dialogue
    });
  }
}
