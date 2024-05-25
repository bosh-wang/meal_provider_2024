import { ActivatedRoute, Router, RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';
import { Component, OnInit } from '@angular/core';
import { Food } from '../../../shared/model/Food';
import { FoodService } from '../../../services/food.service';
import { CommonModule } from '@angular/common';
import { CartService } from '../../../services/cart.service';
import { NotFoundComponent } from '../not-found/not-found.component';
import { MenuManipulateService } from '../../../services/menu-manipulate.service';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-food-page',
  standalone: true,
  imports: [CommonModule, FormsModule, NotFoundComponent, RouterOutlet, RouterLink, RouterLinkActive],
  templateUrl: './food-page.component.html',
  styleUrls: ['./food-page.component.css']
})
export class FoodPageComponent implements OnInit {
  food!: Food;
  newFood: Food = new Food();

  constructor(
    private activatedRoute: ActivatedRoute,
    private foodService: FoodService,
    private cartService: CartService,
    private menuService: MenuManipulateService,
    private router: Router
  ) {
    this.activatedRoute.params.subscribe((params) => {
      if (params['id']) {
        this.food = this.foodService.getFoodById(params['id']);
      }
    });
  }

  ngOnInit(): void {}

  addToCart() {
    this.cartService.addToCart(this.food);
    this.router.navigateByUrl('/cart-page');
  }

  addNewFood() {
    this.menuService.addFood(this.newFood);
    this.newFood = new Food(); // Reset the form
  }

  deleteFood() {
    this.menuService.deleteFood(this.food.id);
    this.router.navigateByUrl('/home'); // Redirect to home after deletion
  }

  updateFoodPrice() {
    const newPrice = prompt('Enter new price:', this.food.price.toString());
    if (newPrice) {
      this.menuService.updateFoodPrice(this.food.id, parseFloat(newPrice));
      this.food.price = parseFloat(newPrice); // Update the displayed price
    }
  }
}
