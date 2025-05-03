import { Component, ElementRef, ViewChild, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ApiService } from '../../services/api.service';
import { BackdropService } from '../../services/backdrop.service';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

declare var bootstrap: any;

@Component({
  selector: 'app-documents',
  templateUrl: './documents.component.html',
  styleUrls: ['./documents.component.css'],
  imports: [FormsModule, CommonModule]
})
export class DocumentsComponent implements OnInit {
  @ViewChild('fileInput') fileInput!: ElementRef;

  documents: any[] = [];
  form: any = {
    type: '',
    file: null
  };
  selectedUploadImage: string | ArrayBuffer | null = null; // Image preview for upload modal
  selectedViewImage: string | ArrayBuffer | null = null; // Image preview for view document modal
  documentType: string = ''; // Store the document type for modal
  documentId: string = ''; // Store the document type for modal
  documentValid: boolean = false;

  constructor(private apiService: ApiService, private router: Router) {}

  ngOnInit(): void {
    this.loadDocuments();
  }

  loadDocuments() {
    this.apiService.documents().subscribe(
      (response: any) => {
        this.documents = response;
      }
    );
  }

  onFileChange(event: any): void {
    this.form.file = event.target.files[0];
    this.previewUploadImage(this.form.file); // Preview the image for the upload modal
  }

  // Function to preview the selected image for the upload modal
  previewUploadImage(file: File) {
    const reader = new FileReader();
    reader.onload = () => {
      this.selectedUploadImage = reader.result; // Store the file data as image URL for the upload modal
    };
    reader.readAsDataURL(file);
  }

  onSubmit(): void {
    if (this.form.type && this.form.file) {
      const formData = new FormData();
      formData.append('type', this.form.type);
      formData.append('file', this.form.file);

      this.apiService.upload(formData).subscribe(
        (response: any) => {
          console.log('Document uploaded successfully', response);
          this.loadDocuments(); // Reload documents
          this.resetForm();     // Clear the form
          this.closeModal();    // Close the modal
        }
      );
    }
  }

  resetForm(): void {
    this.form = { type: '', file: null };
    this.selectedUploadImage = null; // Reset the image preview for the upload modal
    this.fileInput.nativeElement.value = '';
  }

  closeModal(): void {
    const modalEl = document.getElementById('uploadModal');
    if (modalEl) {
      const modal = bootstrap.Modal.getInstance(modalEl) || new bootstrap.Modal(modalEl);
      modal.hide();
    }
  }

  onViewDocumentClick(documentId: string): void {
    this.apiService.image(documentId).subscribe(
      (imageData: Blob) => {
        const reader = new FileReader();
        reader.onloadend = () => {
          this.selectedViewImage = reader.result; // Store the image data as a URL for the view document modal
        };
        reader.readAsDataURL(imageData); // Convert Blob to a data URL

        const doc = this.documents.find(d => d.id === documentId);
        if (doc) {
          this.documentValid = doc.valid
          this.documentType = doc.type;
          this.documentId = doc.id
        }

        const modalEl = document.getElementById('viewDocumentModal');
        if (modalEl) {
          const modal = bootstrap.Modal.getInstance(modalEl) || new bootstrap.Modal(modalEl);
          modal.show();
        }
      }
    );
  }

  validateDocument() {
    this.apiService.validate(this.documentId).subscribe(r => {
      if (r === "1") {
        this.documentValid = true;
        alert("Documento Válido.")
      } else {
        this.documentValid = false;
        alert("Documento Inválido.")
      }
      this.loadDocuments();
    });
  }
}
