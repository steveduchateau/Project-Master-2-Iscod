import { Component, Inject } from '@angular/core';
import { MAT_DIALOG_DATA, MatDialogRef, MatDialogModule } from '@angular/material/dialog';
import { CommonModule } from '@angular/common';
import { MatButtonModule } from '@angular/material/button';

@Component({
  selector: 'app-projets-details-dialog',
  standalone: true,
  templateUrl: './projets-details-dialog.component.html',
  styleUrls: ['./projets-details-dialog.component.scss'],
  imports: [CommonModule, MatDialogModule, MatButtonModule]
})
export class ProjetsDetailsDialogComponent {
  constructor(
    public dialogRef: MatDialogRef<ProjetsDetailsDialogComponent>,
    @Inject(MAT_DIALOG_DATA) public data: any
  ) {}

  closeDialog(): void {
    this.dialogRef.close();
  }
}
