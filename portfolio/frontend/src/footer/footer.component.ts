import { Component } from '@angular/core'; // Importation du décorateur Component depuis Angular

@Component({
  selector: 'app-footer', // Déclaration du sélecteur du composant, utilisé pour intégrer le composant dans le template
  standalone: true, // Indique que ce composant est autonome et peut être utilisé indépendamment, sans nécessiter de module Angular spécifique
  imports: [], // Liste des imports nécessaires pour ce composant. Ici, aucun import supplémentaire n'est requis
  templateUrl: './footer.component.html', // Chemin vers le fichier de template HTML du composant
  styleUrls: ['./footer.component.scss'] // Chemin vers le fichier de styles SCSS du composant
})
export class FooterComponent {
  // Classe du composant pour le pied de page
  // Actuellement, cette classe ne contient aucune logique spécifique, mais elle peut être étendue pour inclure des méthodes ou des propriétés
}
