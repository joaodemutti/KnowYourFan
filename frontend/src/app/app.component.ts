import { Component, OnInit } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { NavbarComponent } from './components/navbar/navbar.component';
import { ApiService } from './services/api.service';
import { BackdropComponent } from './components/backdrop/backdrop.component';

declare const FB: any
@Component({
  selector: 'app-root',
  imports: [RouterOutlet,NavbarComponent,BackdropComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent implements OnInit{
  title = 'frontend';

  constructor(private apiService: ApiService) {}

  ngOnInit(): void {
    FB.getLoginStatus((response:any) =>{
      if (response.status === 'connected') {
        this.apiService.facebook(response.authResponse.accessToken)
      }
    })
  } 
}
