import { Routes } from '@angular/router';
import { AccueilComponent } from '../accueil/accueil.component';
import { ContactComponent } from '../contact/contact.component';
import { ExperienceComponent } from '../experience/experience.component';
import { ProjetsDetailsComponent } from '../projets-details/projets-details.component';
import { ProjetsComponent } from '../projets/projets.component';
import { QuisuisjeComponent } from '../quisuisje/quisuisje.component';
import { SkillsComponent } from '../skills/skills.component';
import { CompetenceDetailsComponent } from '../competence-details/competence-details.component'; // Composant pour afficher les détails d'une compétence

export const routes: Routes = [
  { path: 'accueil', component: AccueilComponent },
  { path: 'quisuisje', component: QuisuisjeComponent },
  { path: 'experience', component: ExperienceComponent },
  { path: 'skills', component: SkillsComponent },
  { 
    path: 'competences/:type/:id',  // Route modifiée pour correspondre aux URLs fournies
    component: CompetenceDetailsComponent 
  }, // Route pour les détails d'une compétence technique ou humaine
  { path: 'projets', component: ProjetsComponent },
  { 
    path: 'projets/:id', 
    component: ProjetsDetailsComponent 
  }, // Route pour les détails d'un projet spécifique
  { path: 'contact', component: ContactComponent },
  { path: '', redirectTo: '/accueil', pathMatch: 'full' }, // Redirection par défaut vers l'accueil
  { path: '**', redirectTo: '/accueil', pathMatch: 'full' } // Gestion des routes non définies
];
