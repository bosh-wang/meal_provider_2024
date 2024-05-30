import { Component } from '@angular/core';
import { Order } from '../../../shared/model/Order';
import { CommonModule } from '@angular/common';
import { FormGroup,FormBuilder,FormControl,ReactiveFormsModule, Validators} from '@angular/forms';

@Component({
  selector: 'app-order-admin',
  standalone: true,
  imports: [CommonModule,ReactiveFormsModule],
  templateUrl: './order-admin.component.html',
  styleUrl: './order-admin.component.css'
})
export class OrderAdminComponent {
  orders: Order[] = [];
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
  months = [
    { name: 'January', value: 0 },
    { name: 'February', value: 1 },
    { name: 'March', value: 2 },
    { name: 'April', value: 3 },
    { name: 'May', value: 4 },
    { name: 'June', value: 5 },
    { name: 'July', value: 6 },
    { name: 'August', value: 7 },
    { name: 'September', value: 8 },
    { name: 'October', value: 9 },
    { name: 'November', value: 10 },
    { name: 'December', value: 11 }
  ];
  monthForm:FormGroup;
  constructor(private fb: FormBuilder) {
    this.monthForm = this.fb.group({
      month: ['', Validators.required]
    });
  }
  submit_month() {
    const formValue = this.monthForm.value;
    const monthValue = Number(formValue.month);
    const monthValue2 = monthValue +Number(1);
    const year = new Date().getFullYear();
    const firstDay = new Date(year, monthValue, 2);
    const lastDay = new Date(year, monthValue2, 1);
    
    const dataToSend = {
      "start_date": firstDay.toISOString().split('T')[0],
      "end_date": lastDay.toISOString().split('T')[0],
      "restaurant_id":"C46"
      //firstDay: firstDay,
      //lastDay: lastDay
    };
    
    console.log('Data to send:', dataToSend);
    // Here you can add the logic to send dataToSend to your server.
  }
  selectedOrder: any = null;
  selectOrder(order: any) {
    this.selectedOrder = order;
  }
  submit(order_id:string,order_status_before:string,flag:Number) {
    
    if(flag===0){
      const dataToSend = {
        "order_id":order_id,
        "order_status_before":order_status_before,
        "order_status_after":'PREPARED',
        
      }
      console.log('Data to send:', dataToSend);
    }
    else if(flag===1){
      const dataToSend = {
        "order_id":order_id,
        "order_status_before":order_status_before,
        "order_status_after":'CONFIRMED',
        
      }
      console.log('Data to send:', dataToSend);
    }
    else if(flag===2){
      const dataToSend = {
        "order_id":order_id,
        "order_status_before":order_status_before,
        "order_status_after":'CANCELED',
      }
      console.log('Data to send:', dataToSend);
    }
  
    
  }
  

}
