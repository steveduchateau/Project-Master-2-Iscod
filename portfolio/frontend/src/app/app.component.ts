import { Component } from '@angular/core';
import { Router, NavigationEnd } from '@angular/router';
import { CommonModule } from '@angular/common';

import { RouterOutlet } from '@angular/router';
import { AccueilComponent } from '../accueil/accueil.component';
import { ContactComponent } from '../contact/contact.component';
import { ExperienceComponent } from '../experience/experience.component';
import { FooterComponent } from '../footer/footer.component';
import { HeaderComponent } from '../header/header.component';
import { ProjetsComponent } from '../projets/projets.component';
import { QuisuisjeComponent } from '../quisuisje/quisuisje.component';
import { SkillsComponent } from '../skills/skills.component';


@Component({
  selector: 'app-root',
  standalone: true,
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
  imports: [
    HeaderComponent,
    AccueilComponent,
    QuisuisjeComponent,
    ExperienceComponent,
    SkillsComponent,
    ProjetsComponent,
    ContactComponent,
    FooterComponent,
    RouterOutlet,
    CommonModule,
    AccueilComponent,
    SkillsComponent
],
})
export class AppComponent {
  title = 'Mon Portfolio';
  currentRoute: string = '';

  constructor(private router: Router) {
    this.router.events.subscribe(event => {
      if (event instanceof NavigationEnd) {
        this.currentRoute = event.urlAfterRedirects;
      }
    });
  }
}
