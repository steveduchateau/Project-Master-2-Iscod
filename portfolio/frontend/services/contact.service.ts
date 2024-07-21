// contact.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ContactService {
  private apiUrl = 'http://127.0.0.1:5000/api/contact'; // URL de l'API Flask

  constructor(private http: HttpClient) { }

  sendContactForm(data: any): Observable<any> {
    return this.http.post<any>(this.apiUrl, data);
  }
}
