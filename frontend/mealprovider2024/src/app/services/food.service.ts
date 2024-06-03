import { Injectable } from '@angular/core';
import { Food, FoodRes, MenuInfo } from '../shared/model/Food';
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
    return sample_foods.filter(
      (food) => food.availibility && food.restaurant_id === restaurant_id
    );
  }
  getAllFood(): Food[] {
    return sample_foods;
  }
  getAllFoodBySearchTerm(data: FoodRes[], searchterm: string) {
    console.log(data, 'input data');
    return data.filter((food) =>
      food.item_name.toLowerCase().includes(searchterm.toLowerCase())
    ); //回傳小寫型態包含搜尋字串的food.name
  }

  //Get All Tag (type: Tag[])
  getAllTags(): Tag[] {
    return sample_tags;
  }
  //Get Food by Tags (type: Food[])
  getAllFoodByTag(data: FoodRes[], tag: string): FoodRes[] {
    return tag === 'All'
      ? data
      : data.filter((food) => food.category?.includes(tag));
  }
  //Get Food by Id (type: Food)
  getRestaurantById(foodId: string) {
    return (
      this.getAllRestaurant(this.restaurant_id).find(
        (food) => food.item_id == foodId
      ) ?? new Food()
    );
  }

  getFoodById(data: FoodRes[], foodId: string): FoodRes[] {
    const foodItem = data.find((food) => food.item_id === foodId);
    return foodItem ? [foodItem] : [];
  }
}
