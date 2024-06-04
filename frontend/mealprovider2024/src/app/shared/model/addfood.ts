export class NewFood{
    "change_status"!:string;
    "restaurant_id"!:string|null;
    "category"!:string; 
    "item_name"!: string;  //item_name
    "price"!: number; //price
    "image_url"!: string;  //image_url
    "description"?: string; //description
    "availability"!: boolean; //availibility
  }