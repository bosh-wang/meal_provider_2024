import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { Login } from '../../../shared/model/Login';
import { ApiService } from '../../../services/api.service';
import { UserService } from '../../../services/user.service';
import { HttpClientModule } from '@angular/common/http';
import { MatSnackBarModule ,MatSnackBar} from '@angular/material/snack-bar';
import { Router } from '@angular/router';
import CryptoJS from 'crypto-js';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule,HttpClientModule,MatSnackBarModule  ],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {

  loginForm: FormGroup;
  submitted = false;
  loginObj:Login=new Login();
  private snackBar!: MatSnackBar;
  constructor(
    private formBuilder: FormBuilder,
    private apiService:ApiService,
    private _snackBar: MatSnackBar,
    private router: Router,
    private userService: UserService 
  ) {  
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
    this.loginObj.password=this.loginForm.value.password;
    //this.loginObj.password_hash=passwordHash;

    this.apiService.login(this.loginObj).subscribe({
      next: res => {
        console.log(res);
        this.userService.setUserRole(this.loginObj.role);  // 使用 this.loginObj.role 設置用戶角色
        this.userService.setUserId(res.user_id); // 設置 user_id
        if(this.loginObj.role==='restaurant_staff'){
          this.userService.setrestaurantId(res.restaurant_id);
        }
        console.log(this.userService.getrestaurantId());
        this.navigateByRole(this.loginObj.role);  // 使用 this.loginObj.role 進行導航
      },
      error: err => {
        console.log(err);
        this.openSnackBar("登入失敗", "關閉",);
      }
    });
  }
  openSnackBar(message: string, action: string) {
    this._snackBar.open(message, action);
  }
  navigateByRole(role: string) {
    if (role === 'kitchen_staff') {
      this.router.navigate(['']);
    } else if (role === 'HR') {
      this.router.navigate(['']);
    } else {
      this.router.navigate(['']);
    }
  }
}
