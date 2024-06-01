import { Campus_name } from './app/shared/model/Campus_name';
import { Food } from './app/shared/model/Food';
import { Restaurant } from './app/shared/model/Restaurant';
import { Restaurant_Type } from './app/shared/model/Restaurant_Type';
import { Tag } from './app/shared/model/Tag';

export const sample_foods: Food[] = [
  {
    id: '1',
    restaurant_id: '1',
    name: 'Pizza Pepperoni',
    price: 10,
    stars: 4.5,
    imageUrl: 'assets/food-1.jpg',
    tags: ['FastFood', 'Pizza', 'Lunch'],
    description:
      'A classic favorite, our Pizza Pepperoni features a crispy crust topped with rich tomato sauce, melty mozzarella cheese, and generous slices of spicy pepperoni.',
    availibility: true,
    restaurant_name: '1號餐廳',
  },
  {
    id: '2',
    restaurant_id: '1',
    name: 'Meatball',
    price: 20,
    stars: 4.7,
    imageUrl: 'assets/food-2.jpg',
    tags: ['SlowFood', 'Lunch'],
    description:
      'Enjoy our hearty Meatballs made with a blend of seasoned beef and pork, slow-cooked in a savory tomato sauce. Perfect for a satisfying meal.',
    availibility: true,
    restaurant_name: '1號餐廳',
  },
  {
    id: '3',
    restaurant_id: '2',
    name: 'Hamburger',
    price: 5,
    stars: 3.5,
    imageUrl: 'assets/food-3.jpg',
    tags: ['FastFood', 'Hamburger'],
    description:
      'Our classic Hamburger is made with a juicy beef patty, fresh lettuce, ripe tomatoes, and tangy pickles, all nestled in a soft sesame seed bun.',
    availibility: true,
    restaurant_name: '2號餐廳',
  },
  {
    id: '4',
    restaurant_id: '2',
    name: 'Fried Potatoes',
    price: 2,
    stars: 3.3,
    imageUrl: 'assets/food-4.jpg',
    tags: ['FastFood', 'Fry'],
    description:
      'Crispy on the outside and fluffy on the inside, our Fried Potatoes are perfectly seasoned and fried to golden perfection. A perfect side dish.',
    availibility: true,
    restaurant_name: '2號餐廳',
  },
  {
    id: '5',
    restaurant_id: '3',
    name: 'Chicken Soup',
    price: 11,
    stars: 3.0,
    imageUrl: 'assets/food-5.jpg',
    tags: ['SlowFood', 'Soup'],
    description:
      'Warm up with our comforting Chicken Soup, made with tender chicken pieces, fresh vegetables, and herbs simmered to perfection in a savory broth.',
    availibility: true,
    restaurant_name: '3號餐廳',
  },
  {
    id: '6',
    restaurant_id: '3',
    name: 'Vegetables Pizza',
    price: 9,
    stars: 4.0,
    imageUrl: 'assets/food-6.jpg',
    tags: ['FastFood', 'Pizza', 'Lunch'],
    description:
      'Our Vegetables Pizza is a fresh and healthy choice, topped with a colorful array of garden-fresh vegetables, mozzarella cheese, and a delicious tomato sauce.',
    availibility: true,
    restaurant_name: '3號餐廳',
  },
  {
    id: '7',
    restaurant_id: '4',
    name: 'Spicy Cheese Burger',
    price: 12,
    stars: 4.0,
    imageUrl: 'assets/food-7.jpg',
    tags: ['FastFood', 'Burger', 'Lunch'],
    description:
      'Add some heat to your meal with our Spicy Cheese Burger, featuring a juicy beef patty, spicy cheese, jalapeños, and a zesty sauce, all in a toasted bun.',
    availibility: true,
    restaurant_name: '4號餐廳',
  },
  {
    id: '8',
    restaurant_id: '4',
    name: 'Vegetables Magento Pizza',
    price: 9,
    stars: 4.0,
    imageUrl: 'assets/food-8.jpg',
    tags: ['FastFood', 'Pizza', 'Lunch'],
    description:
      'Our Vegetables Magento Pizza is a delicious choice for veggie lovers, topped with a mix of fresh vegetables, flavorful tomato sauce, and gooey cheese.',
    availibility: true,
    restaurant_name: '4號餐廳',
  },
];

export const sample_tags: Tag[] = [
  { name: 'All', count: 8 },
  { name: 'FastFood', count: 4 },
  { name: 'Pizza', count: 3 },
  { name: 'Lunch', count: 3 },
  { name: 'SlowFood', count: 2 },
  { name: 'Hamburger', count: 2 },
  { name: 'Fry', count: 1 },
  { name: 'Soup', count: 1 },
];

export const sample_restaurants: Restaurant[] = [
  {
    id: '1',
    name: 'QuickBite Haven',
    type: ['台式'],
    imageUrl:
      'https://i0.wp.com/banbi.tw/wp-content/uploads/20211127184737_16.jpg',
    campus: ['竹科龍潭園區'],
    fab: '1',
    canteen_num: '2',
  },
  {
    id: '2',
    name: 'Speedy Snack Shack',
    type: ['中式'],
    imageUrl:
      'https://hsinchu.lakeshore.com.tw/wp-content/uploads/sites/12/2020/08/hs_mwr_gallery_3.jpg',
    campus: ['南科台南園區'],
    fab: '7',
    canteen_num: '4',
  },
  {
    id: '3',
    name: 'FastFuel Bistro',
    type: ['中式'],
    imageUrl:
      'https://hips.hearstapps.com/hmg-prod/images/12332323-1598782461.jpg?crop=0.492xw:0.984xh;0,0&resize=640:*',
    campus: ['中科台中園區'],
    fab: '5',
    canteen_num: '1',
  },
  {
    id: '4',
    name: 'Rapid Eats Express',
    type: ['台式'],
    imageUrl:
      'https://res.klook.com/image/upload/q_85/c_fill,w_750/v1688985978/irsrlcroisgaaulpbfpa.jpg',
    campus: ['竹科竹科園區'],
    fab: '3',
    canteen_num: '2',
  },
];

export const restaurant_type: Restaurant_Type[] = [
  {
    type: ['全部'],
  },
  {
    type: ['鍋物'],
  },
  {
    type: ['台式'],
  },
  {
    type: ['中式'],
  },
  {
    type: ['速食'],
  },
  {
    type: ['飲料'],
  },
  {
    type: ['甜點'],
  },
  {
    type: ['燒烤'],
  },
  {
    type: ['早餐'],
  },
  {
    type: ['健康餐'],
  },
  {
    type: ['日式'],
  },
  {
    type: ['牛排'],
  },
];
export const campus_name: Campus_name[] = [
  {
    name: ['竹科龍潭園區'],
  },
  {
    name: ['竹科竹科園區'],
  },
  {
    name: ['竹科竹南園區'],
  },
  {
    name: ['中科台中園區'],
  },
  {
    name: ['南科嘉義園區'],
  },
  {
    name: ['南科台南園區'],
  },
];
