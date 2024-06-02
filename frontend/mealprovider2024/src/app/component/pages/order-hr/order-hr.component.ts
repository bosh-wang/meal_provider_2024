import { Component ,Input} from '@angular/core';
import { Order_HR } from '../../../shared/model/Order';
import { CommonModule } from '@angular/common';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { ApiService } from '../../../services/api.service';
import { MatSnackBarModule ,MatSnackBar} from '@angular/material/snack-bar';

@Component({
  selector: 'app-order-hr',
  standalone: true,
  imports: [CommonModule,ReactiveFormsModule,MatSnackBarModule],
  templateUrl: './order-hr.component.html',
  styleUrl: './order-hr.component.css'
})
export class OrderHRComponent {
  orders: Order_HR[] = [];
  ngOnInit() {
    // Example data
    this.orders=[];
    
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

  constructor(private fb: FormBuilder,private apiService:ApiService,private _snackBar: MatSnackBar) {
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
      "start_date": firstDay.toISOString().split('T')[0],
      "end_date": lastDay.toISOString().split('T')[0]
    };
    console.log(dataToSend);
    this.apiService.orderHistory_HR(dataToSend).subscribe({
      next: res => {
        console.log(res);
        this.orders=res.orders;
      },
      error: err => {
        console.log(err);
      }
    });
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
  onClick() {
    const unpaidCustomerIds = this.getUnpaidCustomerIds(this.orders);
    console.log(unpaidCustomerIds);
    this.apiService.order_HRpaymentNotification({user_id:unpaidCustomerIds}).subscribe({
      next: res => {
        console.log(res);
        this.submit();
      },
      error: err => {
        console.log(err);
      }
    });
  }
  getUnpaidCustomerIds(orders: Order_HR[]): string[] {
    return Array.from(new Set(
      orders
        .filter(order => !order.paid)
        .map(order => order.customer_id)
    ));
  }
  
  // 调用函数并输出结果
  
}
