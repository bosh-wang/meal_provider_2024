import { campus_name } from './../../../data';
import { CartService } from './../../services/cart.service';
import { CommonModule } from '@angular/common';
import { Component, OnInit ,Input } from '@angular/core';
import { RouterLink, RouterLinkActive, RouterOutlet ,Router} from '@angular/router';
import { RestaurantService } from '../../services/restaurant.service';
import { Campus_name } from '../../shared/model/Campus_name';
import { UserService } from '../../services/user.service';  // 引入 UserService
@Component({
  selector: 'app-header',
  standalone: true,
  imports: [CommonModule, RouterOutlet, RouterLink, RouterLinkActive],
  templateUrl: './header.component.html',
  styleUrl: './header.component.css'
})
export class HeaderComponent implements OnInit{
  campus_name: Campus_name[] = [];
  @Input() userRole: string | null = null;
  cartQuantity = 0;
  constructor(cartService:CartService, restaurantService:RestaurantService,private userService: UserService, private router: Router){
    cartService.getCartObservable().subscribe((newCart) => {
      this.cartQuantity = newCart.totalCount;
      this.userRole = this.userService.getUserRole();
      console.log('header',this.userRole);
    })
    
  }

  ngOnInit(): void {

  }
  logout() {
    this.userService.clearUserRole();
    this.router.navigate(['/login']);
  }
}
