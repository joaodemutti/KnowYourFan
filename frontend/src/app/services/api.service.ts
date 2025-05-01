// auth.service.ts
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { BehaviorSubject, Observable } from 'rxjs';
import { environment } from '../../environments/environment'; // Import environment for API URL
import { tap,switchMap } from 'rxjs/operators';

@Injectable({
  providedIn: 'root',
})
export class ApiService {
  private apiUrl = `${environment.apiUrl}`; // Use environment API URL
  private loggedIn = new BehaviorSubject<boolean>(this.hasToken());

  constructor(private http: HttpClient) {}

  login(credentials: { email: string; password: string }): Observable<any> {
    return this.http.post(`${this.apiUrl}/login`, credentials).pipe(
      tap((response: any) => {
        localStorage.setItem('token', response); // Store token
        this.loggedIn.next(true); // Update login state
      })
    );  
  }

  facebook(credentials:{access_token:string}): Observable<any> {
    return this.http.post(`${this.apiUrl}/facebook`,credentials).pipe(
      tap((response:any) => {
        localStorage.setItem('token', response); // Store token
        this.loggedIn.next(true); // Update login state
      })
    )
  }

  me(): Observable<any> {
        return this.http.get(`${this.apiUrl}/me`, {
          headers: new HttpHeaders().set('Authorization', `Bearer ${localStorage.getItem('token')}`)
        });
  }

  update(user: {
    email: string,
    name: string,
    address: string,
    cpf: string,
    interests: string[],
  }) : Observable<any> {
    return this.http.put(`${this.apiUrl}/users`,user, {
      headers: new HttpHeaders().set('Authorization', `Bearer ${localStorage.getItem('token')}`)
    });
  }

  create(user: {
    email: string,
    name: string,
    address: string,
    cpf: string,
    interests: string[],
  }){
    return this.http.post(`${this.apiUrl}/users`,user);
  }

  logout():void {
    localStorage.removeItem('token'); // Remove token
    this.loggedIn.next(false); // Update login state
  }

  isLoggedIn(): Observable<boolean> {
    return this.loggedIn.asObservable(); // Return login state
  }

  private hasToken(): boolean {
    return !!localStorage.getItem('token'); // Check if token exists
  }
}
