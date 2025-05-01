import { Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { LoginComponent } from './pages/login/login.component';
import { SigninComponent } from './pages/signin/signin.component';
import { DocumentsComponent } from './pages/documents/documents.component';

export const routes: Routes = [
  { path: '', component: HomeComponent },  // Home route
  { path: 'login', component:LoginComponent},
  { path: 'signin', component:SigninComponent},
  { path: 'documents', component:DocumentsComponent},
  { path: '**', redirectTo: '' } // Wildcard route for 404
];
