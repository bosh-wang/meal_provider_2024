import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  constructor() {}
  
  private userRole: string | null = null;

  setUserRole(role: string) {
    this.userRole = role;
  }

  getUserRole(): string | null {
    return this.userRole;
  }
  clearUserRole() {
    this.userRole = null;
  }
}
