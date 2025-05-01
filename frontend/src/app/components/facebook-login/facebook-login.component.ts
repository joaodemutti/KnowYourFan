import { Component } from '@angular/core';
import { ApiService } from '../../services/api.service';
import { Router } from '@angular/router';
declare const FB: any;

@Component({
  selector: 'app-facebook-login',
  imports: [],
  templateUrl: './facebook-login.component.html',
  styleUrl: './facebook-login.component.css'
})
export class FacebookLoginComponent {
  constructor(private apiService: ApiService, private router: Router) {}

  loginWithFacebook(): void {
    FB.getLoginStatus((response:any) =>{
      if (response.status === 'connected') {
        this.apiService.facebook({access_token:response.authResponse.accessToken}).subscribe(()=>{
            this.router.navigate(['/signin'])
        })
      }
      else {
        FB.login((response:any) => {
          if (response.authResponse) {
            console.log('Successfully logged in!', response);
            this.apiService.facebook({access_token:response.authResponse.accessToken}).subscribe(()=>{
              this.router.navigate(['/signin'])
            })
            
          } else {
            console.log('User cancelled login or did not fully authorize.');
          
          }
        }, { scope: 'email,public_profile' });
      }
    })
    
  }
}
