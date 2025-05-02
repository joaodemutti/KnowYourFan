import { Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { LoginComponent } from './pages/login/login.component';
import { SigninComponent } from './pages/signin/signin.component';
import { DocumentsComponent } from './pages/documents/documents.component';
import { AuthGuard } from './services/api.guard';
import { EsportsComponent } from './pages/esports/esports.component';

export const routes: Routes = [
  { path: '', component: HomeComponent },  // Home route
  { path: 'login', component:LoginComponent},
  { path: 'signin', component:SigninComponent},
  { path: 'documents', component:DocumentsComponent,canActivate:[AuthGuard]},
  { path: 'esports', component:EsportsComponent,canActivate:[AuthGuard]},
  { path: '**', redirectTo: '' } // Wildcard route for 404
];
