import { Component } from '@angular/core';
import { Order_HR } from '../../../shared/model/Order';
import { CommonModule } from '@angular/common';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';

@Component({
  selector: 'app-order-hr',
  standalone: true,
  imports: [CommonModule,ReactiveFormsModule],
  templateUrl: './order-hr.component.html',
  styleUrl: './order-hr.component.css'
})
export class OrderHRComponent {
  orders: Order_HR[] = [];
  ngOnInit() {
    // Example data
    this.orders = [
      {
        customer_id: 'C001',
        order_id: 'O1001',
        order_date: '2024-05-01',
        total_price: 150.75,
        paid: true
      },
      {
        customer_id: 'C002',
        order_id: 'O1002',
        order_date: '2024-05-02',
        total_price: 89.99,
        paid: false
      },
      {
        customer_id: 'C003',
        order_id: 'O1003',
        order_date: '2024-05-03',
        total_price: 200.50,
        paid: true
      },
      {
        customer_id: 'C004',
        order_id: 'O1004',
        order_date: '2024-05-04',
        total_price: 75.00,
        paid: true
      },
      {
        customer_id: 'C005',
        order_id: 'O1005',
        order_date: '2024-05-05',
        total_price: 120.20,
        paid: false
      }
    ];
  }
  departments = ['Human Resources','Administration','Technology'];
  positions = ['HR Manager','Engineer','Administrator'];
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

  searchForm: FormGroup;

  constructor(private fb: FormBuilder) {
    this.searchForm = this.fb.group({
      department: ['', Validators.required],
      position: ['', Validators.required],
      month: ['', Validators.required]
    });
  }

  submit() {
    const formValue = this.searchForm.value;
    const monthValue = Number(formValue.month);
    const monthValue2 = monthValue +Number(1);
    const year = new Date().getFullYear();
    const firstDay = new Date(year, monthValue, 2);
    const lastDay = new Date(year, monthValue2, 1);
    
    const dataToSend = {
      "department": formValue.department,
      "position": formValue.position,
      "firstDay": firstDay.toISOString().split('T')[0],
      "lastDay": lastDay.toISOString().split('T')[0]
      //firstDay: firstDay,
      //lastDay: lastDay
    };
    
    console.log('Data to send:', dataToSend);
    // Here you can add the logic to send dataToSend to your server.
  }
  
  

  paymentNotification(user_id:string) {
    const dataToSend = {
      "user_id":user_id,
    };
    console.log('Data to send:', dataToSend);
  }
  selectedEmployee: any = null;
  selectEmployee(employee: any) {
    this.selectedEmployee = employee;
  }
  onClick(employee: any,user_id:string) {
    this.paymentNotification(user_id);
    this.selectEmployee(employee);
  }
}
