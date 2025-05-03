import { CommonModule } from '@angular/common';
import { ChangeDetectorRef, Component, ElementRef, ViewChild } from '@angular/core';
import { BackdropService } from '../../services/backdrop.service';


@Component({
  selector: 'app-backdrop',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './backdrop.component.html',
  styleUrl: './backdrop.component.css'
})
export class BackdropComponent {
  @ViewChild('backdropRef') backdropRef!: ElementRef<HTMLDivElement>;
  isVisible = false;

  constructor(private backdropService: BackdropService,private cdr: ChangeDetectorRef) {}

  ngAfterViewInit() {
    this.backdropService.visible$.subscribe((visible) => {
      this.isVisible = visible;
      // Optional direct DOM manipulation (if needed):
      this.cdr.detectChanges()
      // this.backdropRef.nativeElement.style.display = visible ? 'block' : 'none';
    });
  }
}
