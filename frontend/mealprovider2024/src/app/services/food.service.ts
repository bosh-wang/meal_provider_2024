import { Injectable } from '@angular/core';
import { Food } from '../shared/model/Food';
import { sample_foods, sample_tags } from '../../data';
import { Tag } from '../shared/model/Tag';

@Injectable({
  providedIn: 'root',
})
export class FoodService {
  sample_foods: any;
  constructor() {}

  getAll(): Food[] {
    return sample_foods;
  }
  getAllFoodBySearchTerm(searchterm: string) {
    return this.getAll().filter((food) =>
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
      ? this.getAll()
      : this.getAll().filter((food) => food.tags?.includes(tag));
  }
  //Get Food by Id (type: Food)
  getFoodById(foodId:string){
    return this.getAll().find(food => food.id == foodId)?? new Food();
  }
}
