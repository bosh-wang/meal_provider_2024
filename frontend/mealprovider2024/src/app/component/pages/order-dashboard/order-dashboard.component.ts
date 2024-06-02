import { Component,Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Order_employee } from '../../../shared/model/Order';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators,FormsModule } from '@angular/forms';
import { ApiService } from '../../../services/api.service';
import { UserService } from '../../../services/user.service';
import { MatSnackBarModule ,MatSnackBar} from '@angular/material/snack-bar';
@Component({
  selector: 'app-order-dashboard',
  standalone: true,
  imports: [CommonModule,FormsModule,ReactiveFormsModule,MatSnackBarModule],
  templateUrl: './order-dashboard.component.html',
  styleUrl: './order-dashboard.component.css'
})
export class OrderDashboardComponent {
  orders: Order_employee[] = [];
  orderObj : Order_employee=new Order_employee();
  filteredOrders: Order_employee[] = [];
  filterForm: FormGroup;

  ngOnInit() {

    // Example data
    this.orders=[];
  const dataToSend = {
    "start_date": "2024-01-01",
    "end_date": "2024-12-31",
    "customer_id":this.userid
  };
  console.log(dataToSend);
  this.apiService.orderHistory_Employee(dataToSend).subscribe({
    next: res => {
      console.log(res);
      this.orders=res.orders;
    },
    error: err => {
      console.log(err);
    }
  });
  this.filteredOrders = this.orders;
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
  statuses = [
    { value: 'PENDING', name: 'Pending' },
    { value: 'CONFIRMED', name: 'Confirmed' },
    { value: 'PREPARED', name: 'Prepared' },
    { value: 'COMPLETED', name: 'Completed' },
    { value: 'CANCELED', name: 'Canceled' }
  ];

  selectedOrder: any = null;
  selectOrder(order: any) {
    this.selectedOrder = order;
  }
  applyFilters() {
    const { month, status } = this.filterForm.value;
    console.log('Selected month:', month);
    console.log('Selected status:', status);
    this.filteredOrders = this.orders.filter(order => {
      const orderDate = new Date(order.order_date);
      const orderMonth = orderDate.getMonth();
      //console.log('Order month:', orderMonth, orderDate.toString());

      return (!month || orderMonth === parseInt(month)) && (!status || order.order_status === status);
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
      "customer_id":this.userid
    };
    console.log('Data to send:', dataToSend);
    this.apiService.orderHistory_Employee(dataToSend).subscribe({
      next: res => {
        console.log(res);
      },
      error: err => {
        console.log(err);
      }
    });
  }
  clearFilters() {
    this.filterForm.reset();
    this.filteredOrders = this.orders;
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
  getOrderStatusClass(status: string): string {
    switch (status) {
      case 'PENDING':
        return 'badge-status badge-pending';
      case 'CONFIRMED':
        return 'badge-status badge-confirmed';
      case 'PREPARED':
        return 'badge-status badge-prepared';
      case 'COMPLETED':
        return 'badge-status badge-completed';
      default:
        return 'badge-status badge-default';
    }
  }
  
  monthForm: FormGroup;
  OrderForm: FormGroup;
  payForm :FormGroup;
  @Input() userid: string | null = null;
  constructor(private fb: FormBuilder,private apiService:ApiService,private userService: UserService,private _snackBar: MatSnackBar) {
    this.OrderForm = this.fb.group({
      rating: ['', Validators.required]
    });
    this.monthForm = this.fb.group({
      month: ['', Validators.required]
    });
    this.payForm = this.fb.group({
      payment_method: ['', Validators.required]
    });
    this.filterForm = this.fb.group({
      month: [''],
      status: ['']
    });
    this.userid=this.userService.getUserId();
  }
  submit(user_id:string,item_id:string) {
    const formValue = this.OrderForm.value;

    const dataToSend = {
      "user_id":this.userid,
      "item_id":item_id,
      "rating": formValue.rating,
    };
    
    console.log('Data to send:', dataToSend);
    this.apiService.order_Rating(dataToSend).subscribe({
      next: res => {
        console.log(res);
        this.openSnackBar("評分成功", "關閉",);
      },
      error: err => {
        console.log(err);
        this.openSnackBar("評分失敗", "關閉",);
      }
    });
  }
  openSnackBar(message: string, action: string) {
    this._snackBar.open(message, action);
  }
  submit_completed(order_id:string,order_status_before:string) {
    const dataToSend = {
      "order_id":order_id,
      "order_status_before":order_status_before,
      "order_status_after":'COMPLETED',
    }
    console.log('Data to send:', dataToSend);
    this.apiService.order_changestatus(dataToSend).subscribe({
      next: res => {
        console.log(res);
        this.submit_month();
      },
      error: err => {
        console.log(err);
      }
    });
  }
  submit_payment(customer_id:string,order_id:string) {
    const formValue = this.payForm.value;
    const dataToSend = {
      "customer_id":this.userid,
      "order_id":order_id,
      "payment_method": formValue.payment_method, 
    };
    console.log('Data to send:', dataToSend);
    this.apiService.order_pay(dataToSend).subscribe({
      next: res => {
        console.log(res);
      },
      error: err => {
        console.log(err);
      }
    });
  }
  
}
