import { Component } from '@angular/core';
import { ApiService } from '../../services/api.service';
import { CommonModule } from '@angular/common'
import { Router } from '@angular/router';

declare const FB: any;

@Component({
  selector: 'app-navbar',
  standalone:true,
  imports: [CommonModule],
  templateUrl: './navbar.component.html',
  styleUrl: './navbar.component.css'
})
export class NavbarComponent {
  username: string | null = null

  
  constructor(public api: ApiService, private router: Router) {}

  ngOnInit(): void {
    this.api.isLoggedIn().subscribe(isLoggedIn=>{
      if(isLoggedIn){
        this.api.me().subscribe(user=>{
          this.username = user.name
        })
      }
    })
  }

  logout(): void {
    // Call the logout method from AuthService
    this.api.logout();
    
    FB.getLoginStatus((response:any) =>{
      if (response.status === 'connected')
        FB.logout(()=>{
          // Redirect to the login page after logging out
          this.router.navigate(['/']);
        })
      else{
  
        this.router.navigate(['/']);
      }
    })
      
    
  }
}
