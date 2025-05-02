import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { BehaviorSubject, Observable, throwError } from 'rxjs';
import { environment } from '../../environments/environment';
import { catchError, tap } from 'rxjs/operators';
import { BackdropService } from './backdrop.service';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private apiUrl = `${environment.apiUrl}`;
  private loggedIn = new BehaviorSubject<boolean>(this.hasToken());

  constructor(
    private http: HttpClient,
    private backdropService: BackdropService,
    private router: Router // ✅ Injected router
  ) {}

  login(credentials: { email: string; password: string }): Observable<any> {
    this.backdropService.show();
    return this.http.post(`${this.apiUrl}/login`, credentials).pipe(
      tap((response: any) => {
        localStorage.setItem('token', response);
        this.loggedIn.next(true);
        this.backdropService.hide();
      }),
      catchError(e => this.handleAuthError(e))
    );
  }

  facebook(credentials: { access_token: string }): Observable<any> {
    this.backdropService.show();
    return this.http.post(`${this.apiUrl}/facebook`, credentials).pipe(
      tap((response: any) => {
        localStorage.setItem('token', response);
        this.loggedIn.next(true);
        this.backdropService.hide();
      }),
      catchError(e => this.handleAuthError(e))
    );
  }

  me(): Observable<any> {
    this.backdropService.show();
    return this.http.get(`${this.apiUrl}/me`, {
      headers: this.authHeaders()
    }).pipe(
      tap(() => this.backdropService.hide()),
      catchError(e => this.handleAuthError(e))
    );
  }

  update(user: {
    email: string,
    name: string,
    address: string,
    cpf: string,
    interests: string[]
  }): Observable<any> {
    this.backdropService.show();
    return this.http.put(`${this.apiUrl}/users`, user, {
      headers: this.authHeaders()
    }).pipe(
      tap(() => this.backdropService.hide()),
      catchError(e => this.handleAuthError(e))
    );
  }

  create(user: {
    email: string,
    name: string,
    address: string,
    cpf: string,
    interests: string[]
  }) {
    this.backdropService.show();
    return this.http.post(`${this.apiUrl}/users`, user).pipe(
      tap(() => this.backdropService.hide()),
      catchError(e => this.handleAuthError(e))
    );
  }

  documents(): Observable<any> {
    this.backdropService.show();
    return this.http.get(`${this.apiUrl}/documents`, {
      headers: this.authHeaders()
    }).pipe(
      tap(() => this.backdropService.hide()),
      catchError(e => this.handleAuthError(e))
    );
  }

  upload(data: FormData): Observable<any> {
    this.backdropService.show();
    return this.http.post(`${this.apiUrl}/documents`, data, {
      headers: this.authHeaders()
    }).pipe(
      tap(() => this.backdropService.hide()),
      catchError(e => this.handleAuthError(e))
    );
  }

  image(documentId: string): Observable<any> {
    this.backdropService.show();
    return this.http.get(`${this.apiUrl}/documents/${documentId}/image`, {
      headers: this.authHeaders(),
      responseType: 'blob' // Assuming the image is returned as a blob
    }).pipe(
      tap(() => this.backdropService.hide()),
      catchError(e => this.handleAuthError(e))
    );
  }
  
  validate(documentId: string): Observable<any> {
    this.backdropService.show();
    return this.http.post(`${this.apiUrl}/documents/${documentId}`, {}, { // You can pass an empty body if nothing is required for validation
      headers: this.authHeaders()
    }).pipe(
      tap(() => this.backdropService.hide()),
      catchError(e => this.handleAuthError(e))
    );
  }

  esports(): Observable<any>{
    return this.http.get(`${this.apiUrl}/esports`,{
      headers: this.authHeaders()
    }).pipe(
      catchError(e=>this.handleAuthError(e,false))
    )
  }

  logout(): void {
    localStorage.removeItem('token');
    this.loggedIn.next(false);
    this.router.navigate(['/login']); // ✅ Redirect
  }

  isLoggedIn(): Observable<boolean> {
    return this.loggedIn.asObservable();
  }

  private hasToken(): boolean {
    return !!localStorage.getItem('token');
  }

  // ✅ Centralized auth error handler
  private handleAuthError(error: any,hide = true) {
    if(hide)
      this.backdropService.hide();
    if (error.status === 401) {
      this.logout();
    }
    return throwError(() => error);
  }

  // ✅ Centralized auth header builder
  private authHeaders(): HttpHeaders {
    return new HttpHeaders().set('Authorization', `Bearer ${localStorage.getItem('token')}`);
  }
}
