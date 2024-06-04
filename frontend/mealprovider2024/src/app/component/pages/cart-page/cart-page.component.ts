import { CommonModule } from '@angular/common';
import { Component, OnInit ,Input} from '@angular/core';
import { Cart } from '../../../shared/model/Cart';
import { CartService } from '../../../services/cart.service';
import { CartItem } from '../../../shared/model/CartItem';
import { TitleComponent } from '../title/title.component';
import { RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';
import { NotFoundComponent } from '../not-found/not-found.component';
import { ApiService } from '../../../services/api.service';
import { UserService } from '../../../services/user.service';
import { MatSnackBarModule ,MatSnackBar} from '@angular/material/snack-bar';
@Component({
  selector: 'app-cart-page',
  standalone: true,
  imports: [CommonModule, RouterOutlet, RouterLink, RouterLinkActive, TitleComponent, NotFoundComponent,MatSnackBarModule],
  templateUrl: './cart-page.component.html',
  styleUrl: './cart-page.component.css'
})
export class CartPageComponent implements OnInit{
  @Input() userid: string | null = null;
  private snackBar!: MatSnackBar;
  cart!: Cart;
  constructor(private cartService:CartService,private apiService:ApiService,private userService: UserService,private _snackBar: MatSnackBar){
    this.cartService.getCartObservable().subscribe((cart) => {
      this.cart = cart;
      this.userid = this.userService.getUserId();
    })
  }

  ngOnInit(): void {

  }
  removeFromCart(cartItem:CartItem){
    this.cartService.removeFromCart(cartItem.food.item_id);
    const dataToSend = {
      "cart_status": "update",
      "user_id": this.userid,
      "item_id": cartItem.food.item_id, 
      "quantity": Number(0)
    };
    console.log('Data to send:', dataToSend);
    this.apiService.updateCart(dataToSend).subscribe({
      next: res => {
        console.log(res);
      },
      error: err => {
        console.log(err);
      }
    });
  }
  UpdateItemQuantity(cartItem:CartItem,num:any){
    const dataToSend = {
      "cart_status": "update",
      "user_id": this.userid,
      "item_id": cartItem.food.item_id, 
      "quantity": Number(num)
    };
    console.log('Data to send:', dataToSend);
    this.apiService.updateCart(dataToSend).subscribe({
      next: res => {
        console.log(res);
      },
      error: err => {
        console.log(err);
      }
    });
  }
  changeQuantity(cartItem:CartItem, quantityInString:string){
    const quantity = parseInt(quantityInString);
    this.cartService.changeQuantity(cartItem.food.item_id, quantity);
  }
  clearcart(){
    const dataToSend = {
      "cart_status": "submit",
      "user_id": this.userid,
    };
    console.log('Data to send:', dataToSend);
    this.apiService.updateCart(dataToSend).subscribe({
      next: res => {
        console.log(res);
        this.openSnackBar("下訂成功", "關閉",);
        this.cartService.clearCart();
      },
      error: err => {
        console.log(err);
        this.openSnackBar("下訂失敗，請檢查是否相同餐廳", "關閉",);
      }
    });
  }
  openSnackBar(message: string, action: string) {
    this._snackBar.open(message, action);
  }
}