import { Component, OnInit } from '@angular/core';
import { FoodService } from '../../../services/food.service';
import { Food } from '../../../shared/model/Food';
import { CommonModule } from '@angular/common';
import { ActivatedRoute, RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';
import { SearchComponent } from '../search/search.component';
import { TagComponent } from '../tag/tag.component';
import { NotFoundComponent } from '../not-found/not-found.component';
import { RestaurantTypeComponent } from '../restaurant-type/restaurant-type.component';
import { FoodSearchComponent } from '../food-search/food-search.component';
import { FormGroup,FormBuilder,FormControl,ReactiveFormsModule } from '@angular/forms';
import { NewFood } from '../../../shared/model/addfood';
@Component({
  selector: 'app-restaurant-page',
  standalone: true,
  imports: [CommonModule, RouterOutlet, RouterLink, RouterLinkActive, SearchComponent, TagComponent, NotFoundComponent, RestaurantTypeComponent, FoodSearchComponent,ReactiveFormsModule],
  templateUrl: './restaurant-page.component.html',
  styleUrl: './restaurant-page.component.css'
})
export class RestaurantPageComponent {
  food: Food[] = [];
  restaurant_id:string='';
  newfood !:FormGroup;
  newfoodObj:NewFood=new NewFood()
  constructor(private foodService: FoodService, private activateRoute: ActivatedRoute,private formBuilder:FormBuilder) {
    this.activateRoute.params.subscribe((params) => {
      if (params['food-searchTerm']) {
        this.food = this.foodService.getAllFoodBySearchTerm(params['food-searchTerm']);
      } else if (params['tag']) {
        this.food = this.foodService.getAllFoodByTag(params['tag']);
      } else {
        this.food = this.foodService.getAllRestaurant(params['id']);
        this.restaurant_id=params['id'];
      }
    });
    this.newfood=this.formBuilder.group({
      "category":[''],
      "item_name":[''],
      "description":[''],
      "price": [''],
      "image_url":['']
    });
  }
  
  ngOnInit(): void {}
  addFood(){
    this.newfoodObj.category=this.newfood.value.category;
    this.newfoodObj.item_name=this.newfood.value.item_name;
    this.newfoodObj.description=this.newfood.value.description;
    this.newfoodObj.price=this.newfood.value.price;
    this.newfoodObj.imageUrl=this.newfood.value.image_url;
    this.newfoodObj.availibility=true;
    this.newfoodObj.change_status="ADD";
    this.newfoodObj.restaurant_id=this.restaurant_id;
    console.log(this.newfoodObj);
  }
}
