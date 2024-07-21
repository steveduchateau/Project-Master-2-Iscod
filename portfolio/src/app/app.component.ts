import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { AccueilComponent } from "../../frontend/accueil/accueil.component";
import { QuisuisjeComponent } from "../../frontend/quisuisje/quisuisje.component";
import { SkillsComponent } from "../../frontend/skills/skills.component";
import { ProjetsComponent } from "../../frontend/projets/projets.component";
import { ExperienceComponent } from "../../frontend/experience/experience.component";
import { HeaderComponent } from "../../frontend/header/header.component";
import { FooterComponent } from "../../frontend/footer/footer.component";
import { ContactComponent } from "../../frontend/contact/contact.component";

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, AccueilComponent, QuisuisjeComponent, SkillsComponent, ProjetsComponent, ExperienceComponent, HeaderComponent, FooterComponent, ContactComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'portfolio Steve DUCHATEAU';
}
