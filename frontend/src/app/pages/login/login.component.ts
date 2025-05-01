import { Component, OnInit, inject } from '@angular/core';
import { FacebookLoginComponent } from '../../components/facebook-login/facebook-login.component';
import { ApiService } from '../../services/api.service';
import { Router, RouterModule } from '@angular/router';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-login',
  imports: [FacebookLoginComponent,FormsModule,RouterModule],
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
  standalone: true,
  })
export class LoginComponent implements OnInit {
  credentials = { email: '', password: '' }; // Declare the credentials object

  constructor(private authService: ApiService, private router: Router) {}

  ngOnInit(): void {
    // Check if the user is already logged in
    this.authService.isLoggedIn().subscribe(isLoggedIn => {
      if (isLoggedIn) {
        // If logged in, redirect to the home page
        this.router.navigate(['/']);
      }

    });
  }

  login(): void {
    if (this.credentials.email && this.credentials.password) {
      this.authService.login(this.credentials).subscribe(() => {
        // On successful login, redirect to the home page
        this.router.navigate(['/']);
      });
    } else {  
      // Handle invalid login (optional)
      console.log("Please enter email and password");
    }
  }
}
