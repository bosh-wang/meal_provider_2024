import { Component, OnInit } from '@angular/core';
import { FoodService } from '../../../services/food.service';
import { Food } from '../../../shared/model/Food';
import { CommonModule } from '@angular/common';
import { ActivatedRoute, RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';
import { SearchComponent } from '../search/search.component';
import { TagComponent } from '../tag/tag.component';
import { NotFoundComponent } from '../not-found/not-found.component';
import { RestaurantTypeComponent } from '../restaurant-type/restaurant-type.component';
import { FoodSearchComponent } from '../food-search/food-search.component';

@Component({
  selector: 'app-restaurant-page',
  standalone: true,
  imports: [CommonModule, RouterOutlet, RouterLink, RouterLinkActive, SearchComponent, TagComponent, NotFoundComponent, RestaurantTypeComponent, FoodSearchComponent],
  templateUrl: './restaurant-page.component.html',
  styleUrl: './restaurant-page.component.css'
})
export class RestaurantPageComponent {
  food: Food[] = [];

  constructor(private foodService: FoodService, private activateRoute: ActivatedRoute) {
    this.activateRoute.params.subscribe((params) => {
      if (params['food-searchTerm']) {
        this.food = this.foodService.getAllFoodBySearchTerm(params['food-searchTerm']);
      } else if (params['tag']) {
        this.food = this.foodService.getAllFoodByTag(params['tag']);
      } else {
        this.food = this.foodService.getAllRestaurant(params['id']);
      }
    });
  }

  ngOnInit(): void {}
}
