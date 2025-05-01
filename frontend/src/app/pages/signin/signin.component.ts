import { Component, OnInit } from '@angular/core';
import { FormsModule, NgForm } from '@angular/forms';
import { Router, RouterModule } from '@angular/router';
import { ApiService } from '../../services/api.service';
import { CommonModule } from '@angular/common';

declare const FB: any

@Component({
  selector: 'app-signin',
  imports: [FormsModule,CommonModule,RouterModule],
  templateUrl: './signin.component.html',
  styleUrls: ['./signin.component.css']
})
export class SigninComponent implements OnInit {
  user = {
    email: '',
    name: '',
    password: '',
    address: '',
    cpf: '',
    interests: [] as string[],
  };

  newInterest: string = '';  

  constructor(public api: ApiService, private router: Router) {}

  ngOnInit(): void {
    this.api.isLoggedIn().subscribe(isLoggedIn => {
      if (isLoggedIn) {
  
        this.api.me().subscribe(user=>{
          if((!user.interests)||user.interests.length==0){

            FB.getLoginStatus((response: any) => {
              if (response.status === 'connected') {
                this.getUserLikes();
              }
            });

          }
          else{
            this.user.interests = user.interests
          }
          this.user.email = user.email
          this.user.name = user.name
          this.user.address = user.address
          this.user.cpf = user.cpf
        })
        
      }
    });
  }

  onSubmit() {
    this.api.isLoggedIn().subscribe(isLoggedOn=>{
      if(isLoggedOn){
        this.api.update(this.user).subscribe(r=>{
          this.router.navigate(["/"])
        })
      }
      else{
          this.api.create(this.user).subscribe(r=>{
            this.router.navigate(["/"])
          })
      }
    })
  }

  getUserLikes(): void {
    // Calculate the date one year ago
    const oneYearAgo = new Date();
    oneYearAgo.setFullYear(oneYearAgo.getFullYear() - 1);
    const oneYearAgoTimestamp = oneYearAgo.getTime() / 1000;  // Convert to UNIX timestamp

    // Fetch user's likes from Facebook
    FB.api('/me/likes', { fields: 'name,created_time' }, (response: any) => {
      if (response && response.data) {
        // Filter the likes to include only those from the last year
        const filteredLikes = response.data.filter((like: any) => {
          const likeTime = new Date(like.created_time).getTime() / 1000;  // Convert to UNIX timestamp
          return (like.created_time == null) || likeTime >= oneYearAgoTimestamp;
        });

        // Save the filtered likes to the user's interests
        this.user.interests = filteredLikes.map((like: any) => like.name);
        console.log('User Interests:', this.user.interests);
      } else {
        console.log('Error fetching likes', response);
      }
    });
  }

  addInterest(): void {
    if (this.newInterest.trim() && !this.user.interests.includes(this.newInterest.trim())) {
      this.user.interests.push(this.newInterest.trim());
    }
    this.newInterest = '';  // Clear the input
  }

  // Remove an interest
  removeInterest(interest: string): void {
    const index = this.user.interests.indexOf(interest);
    if (index >= 0) {
      this.user.interests.splice(index, 1);
    }
  }
}
