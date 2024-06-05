import { Component, Input } from '@angular/core';
import { Order_Kitchen } from '../../../shared/model/Order';
import { CommonModule } from '@angular/common';
import { FormGroup, FormBuilder, FormControl, ReactiveFormsModule, Validators } from '@angular/forms';
import { ApiService } from '../../../services/api.service';
import { UserService } from '../../../services/user.service';
@Component({
  selector: 'app-order-admin',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
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
  monthForm: FormGroup;
  constructor(private fb: FormBuilder, private apiService: ApiService, private userService: UserService) {
    this.monthForm = this.fb.group({
      month: ['', Validators.required]
    });
    this.restaurantid = this.userService.getrestaurantId();
  }

  submit_month() {
    const formValue = this.monthForm.value;
    const monthValue = Number(formValue.month);
    const monthValue2 = monthValue + Number(1);
    const year = new Date().getFullYear();
    const firstDay = new Date(year, monthValue, 2);
    const lastDay = new Date(year, monthValue2, 1);

    const dataToSend = {
      "start_date": firstDay.toISOString().split('T')[0],
      "end_date": lastDay.toISOString().split('T')[0],
      "restaurant_id": this.restaurantid
    };

    console.log('Data to send:', dataToSend);
    this.apiService.orderHistory_Kitchen(dataToSend).subscribe({
      next: res => {
        console.log(res);
        this.orders = res.orders;
        console.log(this.orders[0]['order_date'])
      },
      error: err => {
        console.log(err);
      }
    });
  }
  selectedOrder: any = null;
  selectOrder(order: Order_Kitchen) {
    this.selectedOrder = order;
    console.log(this.selectedOrder.item)
  }
  submit(order_id: string, order_status_before: string, flag: number) {
    let order_status_after: string;

    switch (flag) {
      case 0:
        order_status_after = 'PREPARED';
        break;
      case 1:
        order_status_after = 'CONFIRMED';
        break;
      case 2:
        order_status_after = 'CANCELED';
        this.submit_month();
        break;
      default:
        console.error('Invalid flag value');
        return;
    }

    const dataToSend = {
      "order_id": order_id,
      "order_status_before": order_status_before,
      "order_status_after": order_status_after,
    };

    console.log('Data to send:', dataToSend);
    this.apiService.order_changestatus(dataToSend).subscribe({
      next: res => {
        console.log(res);
        // Update local order status
        const order = this.orders.find(o => o.order_id === order_id);
        if (order) {
          order.order_status = order_status_after;
        }
      },
      error: err => {
        console.error('Error occurred:', err);
      }
    });
  }

  updateOrderStatus(order_id: string, new_status: string) {
    const order = this.orders.find(o => o.order_id === order_id);
    if (order) {
      order.order_status = new_status;
    }
  }

  // Method to check if a step is active based on the order status
  isStepActive(status: string): boolean {
    const orderStatusSequence = ['PENDING', 'CONFIRMED', 'PREPARED', 'COMPLETED'];
    const currentIndex = orderStatusSequence.indexOf(this.selectedOrder?.order_status);
    const stepIndex = orderStatusSequence.indexOf(status);
    return stepIndex <= currentIndex;
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
}

