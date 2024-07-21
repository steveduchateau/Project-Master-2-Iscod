import { Component, Inject } from '@angular/core';
import { MAT_DIALOG_DATA, MatDialogRef, MatDialogModule } from '@angular/material/dialog';
import { CommonModule } from '@angular/common';
import { MatButtonModule } from '@angular/material/button';

@Component({
  selector: 'app-competence-details-dialog',
  standalone: true,
  templateUrl: './competence-details-dialog.component.html',
  styleUrls: ['./competence-details-dialog.component.scss'],
  imports: [CommonModule, MatDialogModule, MatButtonModule]
})
export class CompetenceDetailsDialogComponent {
  constructor(
    public dialogRef: MatDialogRef<CompetenceDetailsDialogComponent>,
    @Inject(MAT_DIALOG_DATA) public data: any
  ) {}

  closeDialog(): void {
    console.log('Dialog closed'); // Ajouter un log pour vérifier si la méthode est appelée
    this.dialogRef.close();
  }
}
