import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { Login } from '../../../shared/model/Login';
import { ApiService } from '../../../services/api.service';
import { HttpClient,HttpClientModule } from '@angular/common/http';
import CryptoJS from 'crypto-js';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule,HttpClientModule ],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {

  loginForm: FormGroup;
  submitted = false;
  loginObj:Login=new Login();
  //constructor(private formBuilder: FormBuilder,private apiService:ApiService,private http: HttpClient) {
  constructor(private formBuilder: FormBuilder,private apiService:ApiService,private http: HttpClient) {  
    const formModel = new Login();

    this.loginForm = this.formBuilder.group({
      email: [formModel.email, [Validators.required, Validators.email]],
      password: [formModel.password_hash, [Validators.required, Validators.minLength(6)]],
      role: [formModel.role, Validators.required]
    });
  }

  get formControls() {
    return this.loginForm.controls;
  }

  onSubmit() {
    this.submitted = true;
    // Stop here if form is invalid
    if (this.loginForm.invalid) {
      return;
    }
    // Hash the password
    const passwordHash = CryptoJS.SHA256(this.loginForm.value.password).toString();

    // Create the final form value object
    const formValue = {
      "email": this.loginForm.value.email,
      "password_hash": this.loginForm.value.password,
      "role": this.loginForm.value.role
    };
    // Process login
    //console.log('Login successful');
    //console.log(formValue);

    this.loginObj.email=this.loginForm.value.email;
    this.loginObj.role=this.loginForm.value.role;
    this.loginObj.password_hash=this.loginForm.value.password;
    console.log(123456)
    //this.loginObj.password_hash=passwordHash;
    this.apiService.login(this.loginObj).subscribe({
      next: res => {
        console.log(res);
      },
      error: err => {
        console.log(err);
      }
    });

    
  }
}
