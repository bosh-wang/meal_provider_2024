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
  user_order!:any;
  user_payment!:any;
  order_time!:any;
  ngOnInit() {
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
    this.order_time=firstDay.toISOString().split('T')[0]+"~"+lastDay.toISOString().split('T')[0];
    this.apiService.orderHistory_HR(dataToSend).subscribe({
      next: res => {
        console.log(res);
        // 按照 customer_id 排序
        res.orders.sort((a:Order_HR, b:Order_HR) => {
          if (a.order_id < b.order_id) {
            return -1;
          }
          if (a.order_id > b.order_id) {
            return 1;
          }
          return 0;
        });
        res.orders.sort((a:Order_HR, b:Order_HR) => {
          if (a.customer_id < b.customer_id) {
            return -1;
          }
          if (a.customer_id > b.customer_id) {
            return 1;
          }
          return 0;
        });
        let groupedOrders: { [key: string]: Order_HR[] } = res.orders.reduce((groups:any, order:any) => {
          // 如果 groups 中沒有這個 customer_id，則初始化為空數組
          if (!groups[order.customer_id]) {
            groups[order.customer_id] = [];
          }
          // 將訂單添加到對應 customer_id 的數組中
          groups[order.customer_id].push(order);
          return groups;
        }, {} as { [key: string]: Order_HR[] });
        //console.log(groupedOrders);
        this.user_order=groupedOrders;
        console.log(this.user_order);
        let totalSpendingByCustomer: { [key: string]: number } = res.orders.reduce((totals:any, order:any) => {
          // 如果 totals 中沒有這個 customer_id，則初始化為 0
          if (!totals[order.customer_id]) {
            totals[order.customer_id] = Number(0);
          }
          // 將訂單的 total_price 加到對應 customer_id 的總花費中
          totals[order.customer_id] += Number(order.total_price);
          return totals;
        }, {} as { [key: string]: number });
        /*let uniqueCustomers = res.orders.reduce((acc:Order_HR[], order:Order_HR) => {
          let existingCustomer = acc.find(o => o.customer_id === order.customer_id);
          if (!existingCustomer) {
            acc.push({ ...order, paid: order.paid });
          } else {
            existingCustomer.paid = existingCustomer.paid && order.paid;
          }
          return acc;
        }, [] as Order_HR[]);*/
        let uniqueCustomers = res.orders.reduce((acc: Order_HR[], order: Order_HR) => {
          // 过滤掉不符合条件的订单
          if (order.department === formValue.department && order.position === formValue.position) {
            let existingCustomer = acc.find(o => o.customer_id === order.customer_id);
            if (!existingCustomer) {
              acc.push({ ...order, paid: order.paid });
            } else {
              existingCustomer.paid = existingCustomer.paid && order.paid;
            }
          }
          return acc;
        }, []);
        
        console.log(uniqueCustomers);
        this.user_payment=totalSpendingByCustomer;
        this.orders=uniqueCustomers;
        console.log(this.orders);
      },
      error: err => {
        console.log(err);
      }
    });
  }
  selectedUser: any = null;
  selectUser(user_id: string) {
    this.selectedUser = this.user_order[user_id];
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
  onClickforPDF() {
    this.apiService.Get_PDF().subscribe({
      next: res => {
        console.log(res);
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
