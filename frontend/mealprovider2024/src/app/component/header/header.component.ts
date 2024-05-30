import { campus_name } from './../../../data';
import { CartService } from './../../services/cart.service';
import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';
import { RestaurantService } from '../../services/restaurant.service';
import { Campus_name } from '../../shared/model/Campus_name';

@Component({
  selector: 'app-header',
  standalone: true,
  imports: [CommonModule, RouterOutlet, RouterLink, RouterLinkActive],
  templateUrl: './header.component.html',
  styleUrl: './header.component.css'
})
export class HeaderComponent implements OnInit{
  campus_name: Campus_name[] = [];
  cartQuantity = 0;
  constructor(cartService:CartService, restaurantService:RestaurantService){
    cartService.getCartObservable().subscribe((newCart) => {
      this.cartQuantity = newCart.totalCount;
    })
  }

  ngOnInit(): void {

  }
}
