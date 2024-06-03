import { Food, FoodRes } from './Food';

export class CartItem {
  constructor(public food: FoodRes) {}
  quantity: number = 1;
  price: number = this.food.price;
}
