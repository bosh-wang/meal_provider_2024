import { Component ,Input} from '@angular/core';
import { Order_Kitchen } from '../../../shared/model/Order';
import { CommonModule } from '@angular/common';
import { FormGroup,FormBuilder,FormControl,ReactiveFormsModule, Validators} from '@angular/forms';
import { ApiService } from '../../../services/api.service';
import { UserService } from '../../../services/user.service'; 
@Component({
  selector: 'app-order-admin',
  standalone: true,
  imports: [CommonModule,ReactiveFormsModule],
  templateUrl: './order-admin.component.html',
  styleUrl: './order-admin.component.css'
})
export class OrderAdminComponent {
  orders: Order_Kitchen[] = [];
  @Input() restaurantid: string | null = null;
  ngOnInit() {
    // Example data
    this.orders = [
      
    ]
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
  constructor(private fb: FormBuilder,private apiService:ApiService,private userService: UserService) {
    this.monthForm = this.fb.group({
      month: ['', Validators.required]
    });
    this.restaurantid=this.userService.getrestaurantId();
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
      "restaurant_id":this.restaurantid
    };
    
    console.log('Data to send:', dataToSend);
    this.apiService.orderHistory_Kitchen(dataToSend).subscribe({
      next: res => {
        console.log(res);
        this.orders=res.orders;
      },
      error: err => {
        console.log(err);
      }
    });
  }
  selectedOrder: any = null;
  selectOrder(order: Order_Kitchen) {
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
    else if(flag===1){
      const dataToSend = {
        "order_id":order_id,
        "order_status_before":order_status_before,
        "order_status_after":'CONFIRMED',
        
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
    else if(flag===2){
      const dataToSend = {
        "order_id":order_id,
        "order_status_before":order_status_before,
        "order_status_after":'CANCELED',
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
    
    
  }
  

}
