import { HomeComponent } from './component/pages/home/home.component';
import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { HeaderComponent } from './component/header/header.component';
import { UserService } from './services/user.service';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, HeaderComponent, HomeComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
})
export class AppComponent {
  title = 'mealprovider2024';
  userRole: string | null = null;
  userId: string | null = null;
  constructor(private userService: UserService) {}

  ngOnInit() {
    this.userRole = this.userService.getUserRole();
    this.userId = this.userService.getUserId();
  }

  updateUserState() {
    this.userRole = this.userService.getUserRole();
    this.userId = this.userService.getUserId();
  }
}
