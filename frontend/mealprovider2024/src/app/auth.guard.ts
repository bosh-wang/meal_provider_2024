import { CanActivateFn, Router } from '@angular/router';
import { inject } from '@angular/core';
import { UserService } from './services/user.service';

export const authGuard: CanActivateFn = (route, state) => {
  const userService = inject(UserService);
  const router = inject(Router);

  const userRole = userService.getUserRole();

  if (userRole === null) {
    return router.parseUrl('/login');
  }

  return true;
};
