import { Component, Inject } from '@angular/core';
import { MAT_DIALOG_DATA, MatDialogRef, MatDialogModule } from '@angular/material/dialog';
import { CommonModule } from '@angular/common';
import { MatButtonModule } from '@angular/material/button';

/**
 * Composant pour afficher les détails d'une compétence dans une boîte de dialogue.
 */
@Component({
  selector: 'app-competence-details-dialog',
  standalone: true, // Indique que ce composant peut être utilisé seul, sans module Angular spécifique
  templateUrl: './competence-details-dialog.component.html', // Fichier template HTML pour ce composant
  styleUrls: ['./competence-details-dialog.component.scss'], // Fichier SCSS pour les styles de ce composant
  imports: [CommonModule, MatDialogModule, MatButtonModule] // Modules Angular nécessaires pour ce composant
})
export class CompetenceDetailsDialogComponent {
competence: any;
  
  /**
   * Constructeur du composant.
   * @param dialogRef Référence à la boîte de dialogue pour pouvoir la fermer
   * @param data Données injectées dans la boîte de dialogue (passées lors de son ouverture)
   */
  constructor(
    public dialogRef: MatDialogRef<CompetenceDetailsDialogComponent>, // Référence à la boîte de dialogue
    @Inject(MAT_DIALOG_DATA) public data: any // Données injectées dans la boîte de dialogue
  ) {}

  /**
   * Méthode pour fermer la boîte de dialogue.
   */
  closeDialog(): void {
    console.log('Dialog closed'); // Log pour vérifier que la méthode est appelée correctement
    this.dialogRef.close(); // Ferme la boîte de dialogue
  }
}
