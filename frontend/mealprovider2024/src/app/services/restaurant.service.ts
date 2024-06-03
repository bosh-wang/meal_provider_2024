import { campus_name } from './../../data';
import { Injectable } from '@angular/core';
import { Food } from '../shared/model/Food';
import { restaurant_type, sample_foods, sample_restaurants, sample_tags } from '../../data';
import { Tag } from '../shared/model/Tag';
import { Restaurant } from '../shared/model/Restaurant';
import { Restaurant_Type } from '../shared/model/Restaurant_Type';
import { ApiService } from './api.service';

@Injectable({
  providedIn: 'root',
})
export class RestaurantService {
  sample_restaurants: any;
  constructor(private apiService:ApiService) {}

  getAll(): Restaurant[] {
    return sample_restaurants;
  }
  
  getAllRestaurantBySearchTerm(searchterm: string) {
    return this.getAll().filter((restaurant) =>
      restaurant.name.toLowerCase().includes(searchterm.toLowerCase())
    ); //回傳小寫型態包含搜尋字串的restaurant.name
  }

  //Get All Restaurant Tag (type: Restaurant[])
  getAllRestaurantTags(): Restaurant_Type[] {
    return restaurant_type;
  }
  //Get Restaurant by Tags (type: Restaurant[])
  getAllRestaurantByTag(tag: string): Restaurant[] {
    return tag === '全部'
      ? this.getAll()
      : this.getAll().filter((restaurant) => restaurant.type?.includes(tag));
  }
  getAllRestaurantByCampus(campus_name: string): Restaurant[] {
    return campus_name === '全部'
      ? this.getAll()
      : this.getAll().filter((restaurant) => restaurant.campus?.includes(campus_name));
  }
  //Get Food by Id (type: Food)
  getFoodById(foodId:string){
    return this.getAll().find(food => food.id == foodId)?? new Food();
  }
}
