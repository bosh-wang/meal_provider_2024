import { Injectable } from '@angular/core';
import { Food } from '../shared/model/Food';
import { sample_foods, sample_tags } from '../../data';
import { Tag } from '../shared/model/Tag';

@Injectable({
  providedIn: 'root',
})
export class FoodService {
  sample_foods: any;
  restaurant_id: string = '';

  constructor() {}

  getAllRestaurant(restaurant_id: string): Food[] {
    this.restaurant_id = restaurant_id;
    return sample_foods.filter(food => food.availibility && food.restaurant_id === restaurant_id);
  }
  getAllFood(): Food[] {
    return sample_foods;
  }
  getAllFoodBySearchTerm(searchterm: string) {
    return this.getAllRestaurant(this.restaurant_id).filter((food) =>
      food.name.toLowerCase().includes(searchterm.toLowerCase())
    ); //回傳小寫型態包含搜尋字串的food.name
  }

  //Get All Tag (type: Tag[])
  getAllTags(): Tag[] {
    return sample_tags;
  }
  //Get Food by Tags (type: Food[])
  getAllFoodByTag(tag: string): Food[] {
    return tag === 'All'
      ? this.getAllRestaurant(this.restaurant_id)
      : this.getAllRestaurant(this.restaurant_id).filter((food) => food.tags?.includes(tag));
  }
  //Get Food by Id (type: Food)
  getRestaurantById(foodId:string){
    return this.getAllRestaurant(this.restaurant_id).find(food => food.id == foodId)?? new Food();
  }

  getFoodById(foodId:string){
    return this.getAllFood().find(food => food.id == foodId)?? new Food();
  }

}
