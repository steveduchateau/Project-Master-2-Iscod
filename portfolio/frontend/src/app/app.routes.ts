import { Routes } from '@angular/router';
import { AccueilComponent } from '../accueil/accueil.component';
import { ContactComponent } from '../contact/contact.component';
import { ExperienceComponent } from '../experience/experience.component';
import { ProjetsDetailsComponent } from '../projets-details/projets-details.component';
import { ProjetsComponent } from '../projets/projets.component';
import { QuisuisjeComponent } from '../quisuisje/quisuisje.component';
import { SkillsComponent } from '../skills/skills.component';
import { CompetenceDetailsDialogComponent } from '../competence-details-dialog/competence-details-dialog.component'; // Import du composant des détails de compétence

export const routes: Routes = [
  { path: 'accueil', component: AccueilComponent },
  { path: 'quisuisje', component: QuisuisjeComponent },
  { path: 'experience', component: ExperienceComponent },
  { path: 'skills', component: SkillsComponent },
  { path: 'competence-details/:id', component: CompetenceDetailsDialogComponent }, // Route modifiée pour afficher les détails d'une compétence par ID
  { path: 'projets', component: ProjetsComponent },
  { path: 'projets/:id', component: ProjetsDetailsComponent }, // Route pour les détails d'un projet
  { path: 'contact', component: ContactComponent },
  { path: '', redirectTo: '/accueil', pathMatch: 'full' } // Redirection par défaut vers l'accueil
];
