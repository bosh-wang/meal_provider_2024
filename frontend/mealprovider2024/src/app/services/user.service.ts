import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  constructor() {}
  
  private userRoleKey = '';

  setUserRole(role: string) {
    if (this.isBrowser()) {
      console.log(role);
      localStorage.setItem(this.userRoleKey, role);
    }
  }

  getUserRole(): string | null {
    if (this.isBrowser()) {
      return localStorage.getItem(this.userRoleKey);
    }
    return null;
  }

  clearUserRole() {
    if (this.isBrowser()) {
      localStorage.removeItem(this.userRoleKey);
    }
  }
  private isBrowser(): boolean {
    return typeof window !== 'undefined' && typeof localStorage !== 'undefined';
  }
}
