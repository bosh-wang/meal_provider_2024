import { Injectable } from '@angular/core';
import { FoodService } from './food.service';
import { Food } from '../shared/model/Food';

@Injectable({
  providedIn: 'root'
})
export class MenuManipulateService {

  constructor(private foodService: FoodService) {}

  addFood(food: Food) {
    this.foodService.sample_foods.push(food);
  }

  deleteFood(foodId: string) {
    const index = this.foodService.sample_foods.findIndex((food: { id: string; }) => food.id === foodId);
    if (index !== -1) {
      this.foodService.sample_foods.splice(index, 1);
    }
  }

  updateFoodPrice(foodId: string, newPrice: number) {
    const food = this.foodService.sample_foods.find((f: { id: string; }) => f.id === foodId);
    if (food) {
      food.price = newPrice;
    }
  }
}
