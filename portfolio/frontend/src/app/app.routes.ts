import { Routes } from '@angular/router';
import { AccueilComponent } from '../accueil/accueil.component';
import { ContactComponent } from '../contact/contact.component';
import { ExperienceComponent } from '../experience/experience.component';
import { ProjetsDetailsComponent } from '../projets-details/projets-details.component';
import { ProjetsComponent } from '../projets/projets.component';
import { QuisuisjeComponent } from '../quisuisje/quisuisje.component';
import { SkillsComponent } from '../skills/skills.component';
import { CompetenceDetailsComponent } from '../competence-details/competence-details.component'; // Import du nouveau composant de page de détails de compétence

export const routes: Routes = [
  { path: 'accueil', component: AccueilComponent },
  { path: 'quisuisje', component: QuisuisjeComponent },
  { path: 'experience', component: ExperienceComponent },
  { path: 'skills', component: SkillsComponent },
  { path: 'competence-details/:type/:id', component: CompetenceDetailsComponent }, // Utilisation du nouveau composant pour afficher les détails d'une compétence
  { path: 'projets', component: ProjetsComponent },
  { path: 'projets/:id', component: ProjetsDetailsComponent }, // Route pour les détails d'un projet
  { path: 'contact', component: ContactComponent },
  { path: '', redirectTo: '/accueil', pathMatch: 'full' }
];
