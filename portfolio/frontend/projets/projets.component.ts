import { Component, OnInit } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { ProjetsService } from '../services/projets.service';
import { MatDialog, MatDialogModule } from '@angular/material/dialog';
import { CommonModule } from '@angular/common';
import { MatButtonModule } from '@angular/material/button';
import { ProjetsDetailsDialogComponent } from '../projets-details-dialog/projets-details-dialog.component';

@Component({
  selector: 'app-projets',
  standalone: true,
  templateUrl: './projets.component.html',
  styleUrls: ['./projets.component.scss'],
  imports: [CommonModule, HttpClientModule, MatDialogModule, MatButtonModule], // Ajoutez CommonModule ici
  providers: [ProjetsService]
})
export class ProjetsComponent implements OnInit {
  projets: any[] = [];

  constructor(private projetsService: ProjetsService, public dialog: MatDialog) {}

  ngOnInit(): void {
    this.projetsService.getProjets().subscribe(
      (data: any[]) => {
        console.log('Projets reçus:', data);
        this.projets = data;
      },
      (error) => {
        console.error('Erreur lors de la récupération des projets:', error);
      }
    );
  }

  openDetailsDialog(project: any): void {
    this.dialog.open(ProjetsDetailsDialogComponent, {
      width: '400px',
      data: project
    });
  }
}
