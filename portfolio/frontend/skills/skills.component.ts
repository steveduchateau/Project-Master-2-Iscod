import { Component, OnInit } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { CompetencesService } from '../services/competences.service';
import { MatDialog, MatDialogModule } from '@angular/material/dialog';
import { CommonModule } from '@angular/common';
import { MatButtonModule } from '@angular/material/button';
import { CompetenceDetailsDialogComponent } from '../competence-details-dialog/competence-details-dialog.component';

@Component({
  selector: 'app-skills',
  standalone: true,
  templateUrl: './skills.component.html',
  styleUrls: ['./skills.component.scss'],
  providers: [CompetencesService],
  imports: [CommonModule, HttpClientModule, MatDialogModule, MatButtonModule]
})
export class SkillsComponent implements OnInit {
  competences: any[] = [];
  hardSkills: any[] = [];
  softSkills: any[] = [];

  constructor(private competencesService: CompetencesService, public dialog: MatDialog) {}

  ngOnInit(): void {
    this.competencesService.getCompetences().subscribe((data: any[]) => {
      this.competences = data;
      this.hardSkills = data.filter(comp => comp.type === 'technique');
      this.softSkills = data.filter(comp => comp.type === 'humaine');
    });
  }

  openDetailsDialog(competence: any): void {
    this.dialog.open(CompetenceDetailsDialogComponent, {
      width: '400px',
      data: competence
    });
  }
}
