import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  private userRoleKey = 'userRole';
  private userIdKey = 'userId';
  private restaurantIdKey = 'restaurantId';
  constructor() {}

  setUserRole(role: string) {
    if (this.isBrowser()) {
      console.log('Setting Role:', role);
      localStorage.setItem(this.userRoleKey, role);
    }
  }

  getUserRole(): string | null {
    if (this.isBrowser()) {
      return localStorage.getItem(this.userRoleKey);
    }
    return null;
  }

  setUserId(userId: string) {
    if (this.isBrowser()) {
      console.log('Setting userId:', userId);
      localStorage.setItem(this.userIdKey, userId);
    }
  }

  getUserId(): string | null {
    if (this.isBrowser()) {
      return localStorage.getItem(this.userIdKey);
    }
    return null;
  }
  setrestaurantId(restaurantId: string) {
    if (this.isBrowser()) {
      console.log('Setting restaurantId:', restaurantId);
      localStorage.setItem(this.restaurantIdKey, restaurantId);
    }
  }

  getrestaurantId(): string | null {
    if (this.isBrowser()) {
      return localStorage.getItem(this.restaurantIdKey);
    }
    return null;
  }

  clearUserRole() {
    if (this.isBrowser()) {
      localStorage.removeItem(this.userRoleKey);
      console.log('Cleared role:', this.userRoleKey);
    }
  }

  clearUserId() {
    if (this.isBrowser()) {
      localStorage.removeItem(this.userIdKey);
      console.log('Cleared userId:', this.userIdKey);
    }
  }
  clearrestaurantId() {
    if (this.isBrowser()) {
      localStorage.removeItem(this.restaurantIdKey);
      console.log('Cleared userId:', this.restaurantIdKey);
    }
  }

  clearUser() {
    this.clearUserRole();
    this.clearUserId();
    this.clearrestaurantId();
  }

  private isBrowser(): boolean {
    return typeof window !== 'undefined' && typeof localStorage !== 'undefined';
  }
}
