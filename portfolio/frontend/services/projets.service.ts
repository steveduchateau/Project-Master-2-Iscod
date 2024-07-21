import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root' // Assurez-vous que le service est fourni à la racine
})
export class ProjetsService {
  private apiUrl = 'http://127.0.0.1:5000/api/projets'; // Assurez-vous que cette URL est correcte

  constructor(private http: HttpClient) {}

  getProjets(): Observable<any[]> {
    return this.http.get<any[]>(this.apiUrl);
  }
}
