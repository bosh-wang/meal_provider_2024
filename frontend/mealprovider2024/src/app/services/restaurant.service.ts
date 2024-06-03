import { campus_name } from './../../data';
import { Injectable } from '@angular/core';
import { Food } from '../shared/model/Food';
import {
  restaurant_type,
  sample_foods,
  sample_restaurants,
  sample_tags,
} from '../../data';
import { Tag } from '../shared/model/Tag';
import {
  AllRestaurant,
  Restaurant,
  Restaurantinfomation,
} from '../shared/model/Restaurant';
import { Restaurant_Type } from '../shared/model/Restaurant_Type';

@Injectable({
  providedIn: 'root',
})
export class RestaurantService {
  sample_restaurants: any;
  constructor() {}

  getAll(): Restaurant[] {
    return sample_restaurants;
  }
  getAllRestaurantBySearchTerm(
    data: Restaurantinfomation[],
    searchterm: string
  ) {
    return data.filter((restaurant) =>
      restaurant.name.toLowerCase().includes(searchterm.toLowerCase())
    ); //回傳小寫型態包含搜尋字串的restaurant.name
  }

  //Get All Restaurant Tag (type: Restaurant[])
  getAllRestaurantTags(): Restaurant_Type[] {
    return restaurant_type;
  }
  //Get Restaurant by Tags (type: Restaurant[])
  getAllRestaurantByTag(
    data: Restaurantinfomation[],
    tag: string
  ): Restaurantinfomation[] {
    return tag === '全部'
      ? data
      : data.filter((restaurant) => restaurant.type?.includes(tag));
  }
  getAllRestaurantByCampus(
    data: Restaurantinfomation[],
    campus_name: string
  ): Restaurantinfomation[] {
    return campus_name === '全部'
      ? data
      : data.filter((restaurant) => restaurant.campus?.includes(campus_name));
  }
  //Get Food by Id (type: Food)
  getFoodById(foodId: string) {
    return (
      this.getAll().find((food) => food.restaurant_id == foodId) ?? new Food()
    );
  }
}
