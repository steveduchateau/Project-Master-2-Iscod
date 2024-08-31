import { bootstrapApplication } from '@angular/platform-browser';
import { AppComponent } from './app/app.component';
import { provideHttpClient, withFetch } from '@angular/common/http'; // Importez avecFetch si nécessaire
import { provideRouter } from '@angular/router';
import { routes } from './app/app.routes';



bootstrapApplication(AppComponent, {
  providers: [
    provideHttpClient(withFetch()), // Configure HttpClient avec les options souhaitées
    provideRouter(routes) // Fournissez vos routes ici
  ]
});
