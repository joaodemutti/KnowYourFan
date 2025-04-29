import { Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';

export const routes: Routes = [
  { path: '', component: HomeComponent },  // Home route
  { path: '**', redirectTo: '' }  // Wildcard route for 404
];
