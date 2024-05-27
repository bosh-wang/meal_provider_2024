import { Component ,OnInit} from '@angular/core';
import { CommonModule } from '@angular/common';
import { Order } from '../../../shared/model/Order';

@Component({
  selector: 'app-order-list',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './order-list.component.html',
  styleUrl: './order-list.component.css'
})
export class OrderListComponent {
  orders: Order[] = [];

  ngOnInit() {
    // Example data
    this.orders = [
      {
        order_id: '1',
        orderNumber: 6,
        user_id: "u005",
        date: '5/26/2021, 3:06:21 AM',
        items: [
          { name: 'Fruit Salad', price: 165, quantity: 1 },
          { name: 'Spicy Beef Fry', price: 580, quantity: 1 },
        ],
        totalAmount: 745,
        order_status:'COMPLETED'
      },
      {
        order_id: '2',
        orderNumber: 5,
        user_id: "u005",
        date: '5/26/2021, 3:01:40 AM',
        items: [
          { name: 'Chinese Salad', price: 240, quantity: 2 },
          { name: 'Crispy Chilli Baby Corn', price: 265, quantity: 1 },
        ],
        totalAmount: 745,
        order_status:'CONFIRMED'
      }
    ];
  }
}
