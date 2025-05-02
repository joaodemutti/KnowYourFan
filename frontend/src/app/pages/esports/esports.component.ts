import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';
import { FacebookLoginComponent } from '../../components/facebook-login/facebook-login.component';
import { CommonModule } from '@angular/common';
import { ApiService } from '../../services/api.service';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-esports',
  imports: [FacebookLoginComponent, CommonModule,FormsModule],
  templateUrl: './esports.component.html',
  styleUrl: './esports.component.css'
})
export class EsportsComponent implements OnInit {
  @ViewChild('requestTextArea') requestTextArea!: ElementRef;
  @ViewChild('responseTextArea') responseTextArea!: ElementRef;

  request = '';
  response = '';
  interests: string[] = [];

  constructor(private api: ApiService) {}

  ngOnInit(): void {
    this.api.me().subscribe(r => {
      this.interests = r.interests;
    });
  }

  ResizeRequest(): void {
    const el = this.requestTextArea.nativeElement;
    el.style.height = 'auto';
    el.style.height = el.scrollHeight+5 + 'px';
    window.scrollTo(0, document.documentElement.scrollHeight);
    setTimeout(()=>{
      window.scrollTo(0, document.documentElement.scrollHeight);
    },0)
  }

  ResizeResponse(): void {
    const el = this.responseTextArea.nativeElement;
    el.style.height = 'auto';
    el.style.height = el.scrollHeight+5 + 'px';
    window.scrollTo(0, document.documentElement.scrollHeight);
    setTimeout(()=>{
      window.scrollTo(0, document.documentElement.scrollHeight);
    },0)
  }

  onGoClick(): void {
    const prompt = "Compartilhe links de perfis relevantes em sites de E-Sports com base nesses interesses.";
    const fullPrompt = `${prompt}\nInteresses do usuário: ${this.interests.join('\n')}`;
    this.typeRequest(fullPrompt);
    this.api.esports().subscribe({
      next:r=>{this.typeResponse(r)},
      complete:()=>{}
    })
  }

  typeRequest(text: string): void {
    this.request = '';
    let index = 0;

    const interval = setInterval(() => {
      if (index < text.length) {
        this.request += text[index];
        this.ResizeRequest();
        index++;
      } else {
        clearInterval(interval);
      }
    }, 5); // typing speed in ms
  }

  typeResponse(text: string): void {
    this.response = '';
    let index = 0;

    const interval = setInterval(() => {
      if (index < text.length) {
        this.response += text[index];
        this.ResizeResponse();
        index++;
      } else {
        clearInterval(interval);
      }
    }, 5); // typing speed in ms
  }

}
