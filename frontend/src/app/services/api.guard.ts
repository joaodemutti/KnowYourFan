import { Injectable } from '@angular/core';
import { CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot, Router } from '@angular/router';
import { Observable } from 'rxjs';
import { ApiService } from './api.service';  // Import AuthService to check authentication state

@Injectable({
  providedIn: 'root',
})
export class AuthGuard implements CanActivate {
  constructor(
    private authService: ApiService,   // Inject AuthService to check if the user is logged in
    private router: Router             // Inject Router to navigate the user if they are not authenticated
  ) {}

  /**
   * This method checks if the user is authenticated before activating the route
   * @param next The ActivatedRouteSnapshot contains information about the route the user is navigating to.
   * @param state The RouterStateSnapshot contains information about the router state.
   * @returns Observable<boolean> | Promise<boolean> | boolean
   *     - true: allows the navigation
   */
  canActivate(
    next: ActivatedRouteSnapshot,
    state: RouterStateSnapshot
  ): Observable<boolean> | Promise<boolean> | boolean {
    // If the user is logged in, allow access to the route
    if (this.authService.isLoggedIn()) {
      return true;
    }

    this.router.navigate(['/login'], {
      queryParams: { returnUrl: state.url } // Store the attempted URL for redirect after login
    });

    return false;
  }
}
