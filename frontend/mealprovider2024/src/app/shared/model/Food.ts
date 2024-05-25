export class Food{
  id!: string;  //item_id
  name!: string;  //item_name
  price!: number; //price
  tags?: string[];  //category
  stars!: number; //star_rating
  imageUrl!: string;  //image_url
  restaurant_id!: string; //restaurant_id
  description?: string; //description
}
