import { Component, OnInit } from '@angular/core';
// Importation du service pour récupérer les compétences
import { CompetencesService } from '../services/competences.service';
// Importation des modules Angular Material pour les dialogues et les boutons
import { MatDialog, MatDialogModule } from '@angular/material/dialog';
import { CommonModule } from '@angular/common';
import { MatButtonModule } from '@angular/material/button';
// Importation du composant de dialogue pour afficher les détails d'une compétence
import { CompetenceDetailsDialogComponent } from '../competence-details-dialog/competence-details-dialog.component';

// Définition du composant Angular
@Component({
  selector: 'app-skills', // Sélecteur pour utiliser ce composant dans les templates HTML
  standalone: true, // Composant autonome, il n'a pas besoin d'un module pour être utilisé
  templateUrl: './skills.component.html', // URL du template HTML associé à ce composant
  styleUrls: ['./skills.component.scss'], // URL de la feuille de style SCSS associée à ce composant
  providers: [CompetencesService], // Déclaration du service comme provider spécifique à ce composant
  imports: [CommonModule, MatDialogModule, MatButtonModule] // Déclaration des modules nécessaires pour ce composant
})
export class SkillsComponent implements OnInit {
  // Déclaration des propriétés pour stocker les compétences et les différentes catégories
  competences: any[] = [];
  hardSkills: any[] = [];
  softSkills: any[] = [];

  // Injection des dépendances dans le constructeur
  constructor(private competencesService: CompetencesService, public dialog: MatDialog) {}

  // Méthode exécutée lors de l'initialisation du composant
  ngOnInit(): void {
    // Appel au service pour récupérer les compétences depuis l'API
    this.competencesService.getCompetences().subscribe((data: any[]) => {
      // Stockage des compétences récupérées
      this.competences = data;
      // Filtrage des compétences pour les hard skills (techniques) et les soft skills (humaines)
      this.hardSkills = data.filter(comp => comp.type === 'technique');
      this.softSkills = data.filter(comp => comp.type === 'humaine');
    });
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
