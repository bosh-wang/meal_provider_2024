import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Order } from '../../../shared/model/Order';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators,FormsModule } from '@angular/forms';
@Component({
  selector: 'app-order-dashboard',
  standalone: true,
  imports: [CommonModule,FormsModule,ReactiveFormsModule],
  templateUrl: './order-dashboard.component.html',
  styleUrl: './order-dashboard.component.css'
})
export class OrderDashboardComponent {
  orders: Order[] = [];
  orderObj : Order=new Order();
  ngOnInit() {
    // Example data
    this.orders = [
      {
        "order_id": "1",
        "orderNumber": 6,
        "date": "5/26/2021, 3:06:21 AM",
        "user_id": "u001",
        "items": [
          { "name": "Fruit Salad", "price": 165, "quantity": 1 },
          { "name": "Spicy Beef Fry", "price": 580, "quantity": 1 }
        ],
        "totalAmount": 745,
        "order_status": "COMPLETED"
      },
      {
        "order_id": "2",
        "orderNumber": 5,
        "date": "5/26/2021, 3:01:40 AM",
        "user_id": "u002",
        "items": [
          { "name": "Chinese Salad", "price": 240, "quantity": 2 },
          { "name": "Crispy Chilli Baby Corn", "price": 265, "quantity": 1 }
        ],
        "totalAmount": 745,
        "order_status": "CONFIRMED"
      },
      {
        "order_id": "3",
        "orderNumber": 7,
        "date": "5/27/2021, 12:15:30 PM",
        "user_id": "u003",
        "items": [
          { "name": "Grilled Chicken", "price": 300, "quantity": 1 },
          { "name": "Mango Smoothie", "price": 200, "quantity": 2 }
        ],
        "totalAmount": 700,
        "order_status": "PREPARED"
      },
      {
        "order_id": "4",
        "orderNumber": 8,
        "date": "5/27/2021, 1:45:00 PM",
        "user_id": "u004",
        "items": [
          { "name": "Caesar Salad", "price": 180, "quantity": 1 },
          { "name": "Tomato Soup", "price": 150, "quantity": 2 }
        ],
        "totalAmount": 480,
        "order_status": "PENDING"
      },
      {
        "order_id": "5",
        "orderNumber": 9,
        "date": "5/27/2021, 2:30:15 PM",
        "user_id": "u005",
        "items": [
          { "name": "Pasta Primavera", "price": 220, "quantity": 1 },
          { "name": "Garlic Bread", "price": 120, "quantity": 2 }
        ],
        "totalAmount": 460,
        "order_status": "CANCELLED"
      }
    ]
    ;
  }

  selectedOrder: any = null;
  selectOrder(order: any) {
    this.selectedOrder = order;
  }
  getProgressWidth(status: string): string {
    switch (status) {
      case 'PENDING':
        return '25%';
      case 'CONFIRMED':
        return '50%';
      case 'PREPARED':
        return '75%';
      case 'COMPLETED':
        return '100%';
      case 'CANCELLED':
        return '100%';
      default:
        return '0%';
    }
  }

  getProgressClass(status: string): string {
    switch (status) {
      case 'PENDING':
        return 'bg-warning';
      case 'CONFIRMED':
        return 'bg-info';
      case 'PREPARED':
        return 'bg-primary';
      case 'COMPLETED':
        return 'bg-success';
      case 'CANCELLED':
        return 'bg-danger';
      default:
        return 'bg-secondary';
    }
  }

  getProgressText(status: string): string {
    switch (status) {
      case 'PENDING':
        return 'PENDING';
      case 'CONFIRMED':
        return 'CONFIRMED';
      case 'PREPARED':
        return 'PREPARED';
      case 'COMPLETED':
        return 'COMPLETED';
      case 'CANCELLED':
        return 'Cancelled';
      default:
        return '0%';
    }
  }

  getProgressValue(status: string): number {
    switch (status) {
      case 'PENDING':
        return 25;
      case 'CONFIRMED':
        return 50;
      case 'PREPARED':
        return 75;
      case 'COMPLETED':
        return 100;
      case 'CANCELLED':
        return 0;
      default:
        return 0;
    }
  }

  OrderForm: FormGroup;
  constructor(private fb: FormBuilder) {
    this.OrderForm = this.fb.group({
      
      rating: ['', Validators.required]
    });
  }
  submit(user_id:string,item_id:string) {
    const formValue = this.OrderForm.value;

    const dataToSend = {
      "user_id":user_id,
      "item_id":item_id,
      "rating": formValue.rating,
      
    };
    
    console.log('Data to send:', dataToSend);
    // Here you can add the logic to send dataToSend to your server.
  }
  submit_completed(order_id:string,order_status_before:string) {
    const dataToSend = {
      "order_id":order_id,
      "order_status_before":order_status_before,
      "order_status_after":'COMPLETED',
      
    }
    console.log('Data to send:', dataToSend);
    
  }
}
