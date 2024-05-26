import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { Login } from '../../../shared/model/Login';
import CryptoJS from 'crypto-js';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {
  loginForm: FormGroup;
  submitted = false;

  constructor(private formBuilder: FormBuilder) {
    const formModel = new Login();
    this.loginForm = this.formBuilder.group({
      email: [formModel.email, [Validators.required, Validators.email]],
      password: [formModel.password, [Validators.required, Validators.minLength(6)]],
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
      email: this.loginForm.value.email,
      password_hash: passwordHash,
      role: this.loginForm.value.role
    };
    // Process login
    console.log('Login successful');
    console.log(formValue);
  }
}
