import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { RouterOutlet, RouterLink, RouterLinkActive } from '@angular/router';
import { Restaurant } from '../../../shared/model/Restaurant';
import { RestaurantService } from '../../../services/restaurant.service';
import { Restaurant_Type } from '../../../shared/model/Restaurant_Type';

@Component({
  selector: 'app-restaurant-type',
  standalone: true,
  imports: [CommonModule, RouterOutlet, RouterLink, RouterLinkActive],
  templateUrl: './restaurant-type.component.html',
  styleUrl: './restaurant-type.component.css'
})
export class RestaurantTypeComponent implements OnInit {
  type?:Restaurant_Type[];
  constructor(restaurantService:RestaurantService) {
    this.type = restaurantService.getAllRestaurantTags();
   }

  ngOnInit(): void {
  }

}
