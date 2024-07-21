// competences.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root' // Assure que le service est disponible dans toute l'application
})
export class CompetencesService {
  private apiUrl = 'http://127.0.0.1:5000/api/competences';

  constructor(private http: HttpClient) {}

  getCompetences(): Observable<any[]> {
    return this.http.get<any[]>(this.apiUrl);
  }
}
