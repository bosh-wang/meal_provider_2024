import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { Login } from '../shared/model/Login';
import { Order_HR } from '../shared/model/Order';
@Injectable({
  providedIn: 'root',
})
export class ApiService {
  loginURL:string;
  orderHR:string;
  order_paymentNotification:string;
  constructor(private http : HttpClient){
    this.loginURL='http://35.224.128.24/api/signin';
    this.orderHR='http://35.224.128.24/api/orderHistoryHR';
    this.order_paymentNotification='http://35.224.128.24/api/paymentNotification';
  }

  login(logindata:Login):Observable<Login>{
    console.log(this.loginURL)
    return this.http.post<Login>(this.loginURL,logindata);
  }

  orderHistory_HR(order_HR:any):Observable<Order_HR>{
    console.log(order_HR)
    return this.http.post<Order_HR>(this.orderHR,order_HR);
  }
  order_HRpaymentNotification(user_id:any):Observable<any>{
    console.log(user_id)
    return this.http.post<any>(this.order_paymentNotification,user_id);
  }
}
