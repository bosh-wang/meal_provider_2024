import { Food } from "./app/shared/model/Food";
import { Tag } from "./app/shared/model/Tag";

export const sample_foods:Food[] = [
  {
    id: '1',
    restaurant_id: '1',
    name: 'Pizza Pepperoni',
    price: 10,
    stars: 4.5,
    imageUrl: 'assets/food-1.jpg',
    tags: ['FastFood', 'Pizza', 'Lunch'],
    description: "A classic favorite, our Pizza Pepperoni features a crispy crust topped with rich tomato sauce, melty mozzarella cheese, and generous slices of spicy pepperoni."
  },
  {
    id:'2',
    restaurant_id: '1',
    name: 'Meatball',
    price: 20,
    stars: 4.7,
    imageUrl: 'assets/food-2.jpg',
    tags: ['SlowFood', 'Lunch'],
    description: "Enjoy our hearty Meatballs made with a blend of seasoned beef and pork, slow-cooked in a savory tomato sauce. Perfect for a satisfying meal."
  },
  {
    id:'3',
    restaurant_id: '2',
    name: 'Hamburger',
    price: 5,
    stars: 3.5,
    imageUrl: 'assets/food-3.jpg',
    tags: ['FastFood', 'Hamburger'],
    description: "Our classic Hamburger is made with a juicy beef patty, fresh lettuce, ripe tomatoes, and tangy pickles, all nestled in a soft sesame seed bun."
  },
  {
    id:'4',
    restaurant_id: '2',
    name: 'Fried Potatoes',
    price: 2,
    stars: 3.3,
    imageUrl: 'assets/food-4.jpg',
    tags: ['FastFood', 'Fry'],
    description: "Crispy on the outside and fluffy on the inside, our Fried Potatoes are perfectly seasoned and fried to golden perfection. A perfect side dish."
  },
  {
    id:'5',
    restaurant_id: '3',
    name: 'Chicken Soup',
    price: 11,
    stars: 3.0,
    imageUrl: 'assets/food-5.jpg',
    tags: ['SlowFood', 'Soup'],
    description: "Warm up with our comforting Chicken Soup, made with tender chicken pieces, fresh vegetables, and herbs simmered to perfection in a savory broth."
  },
  {
    id:'6',
    restaurant_id: '3',
    name: 'Vegetables Pizza',
    price: 9,
    stars: 4.0,
    imageUrl: 'assets/food-6.jpg',
    tags: ['FastFood', 'Pizza', 'Lunch'],
    description: "Our Vegetables Pizza is a fresh and healthy choice, topped with a colorful array of garden-fresh vegetables, mozzarella cheese, and a delicious tomato sauce."
  },
  {
    id:'7',
    restaurant_id: '4',
    name: 'Spicy Cheese Burger',
    price: 12,
    stars: 4.0,
    imageUrl: 'assets/food-7.jpg',
    tags: ['FastFood', 'Burger', 'Lunch'],
    description: "Add some heat to your meal with our Spicy Cheese Burger, featuring a juicy beef patty, spicy cheese, jalapeños, and a zesty sauce, all in a toasted bun."

  },
  {
    id:'8',
    restaurant_id: '4',
    name: 'Vegetables Magento Pizza',
    price: 9,
    stars: 4.0,
    imageUrl: 'assets/food-8.jpg',
    tags: ['FastFood', 'Pizza', 'Lunch'],
    description: "Our Vegetables Magento Pizza is a delicious choice for veggie lovers, topped with a mix of fresh vegetables, flavorful tomato sauce, and gooey cheese."
  },
]

export const sample_tags:Tag[] = [
  { name: 'All', count: 8 },
  { name: 'FastFood', count: 4 },
  { name: 'Pizza', count: 3 },
  { name: 'Lunch', count: 3 },
  { name: 'SlowFood', count: 2 },
  { name: 'Hamburger', count: 2 },
  { name: 'Fry', count: 1 },
  { name: 'Soup', count: 1 },
]
