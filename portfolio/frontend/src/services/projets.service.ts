import { Injectable } from '@angular/core'; 
import { HttpClient } from '@angular/common/http'; 
import { Observable } from 'rxjs'; 

@Injectable({
  providedIn: 'root'
})
export class ProjetsService {
  private apiUrl = 'https://project-master-2-iscod.onrender.com/api/projets'; 

  constructor(private http: HttpClient) {}

  getProjets(): Observable<any[]> {
    return this.http.get<any[]>(this.apiUrl);
  }

  getProjetById(id: string): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}/${id}`);
  }
}
