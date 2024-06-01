import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { Login } from '../shared/model/Login';
import { Order_HR ,Order_Kitchen,Order_employee} from '../shared/model/Order';
@Injectable({
  providedIn: 'root',
})
export class ApiService {
  loginURL:string;
  orderHR:string;
  order_paymentNotification:string;
  orderKitchen:string;
  orderstatus:string;
  orderEmployee:string;
  order_payment:string;
  order_rating:string;
  constructor(private http : HttpClient){
    this.loginURL='http://35.224.128.24/api/signin';
    this.orderHR='http://35.224.128.24/api/orderHistoryHR';
    this.order_paymentNotification='http://35.224.128.24/api/paymentNotification';
    this.orderKitchen='http://35.224.128.24/api/orderHistoryRestaurant';
    this.orderstatus='http://35.224.128.24/api/change_order_status';
    this.orderEmployee='http://35.224.128.24/api/orderHistoryEmployee';
    this.order_payment='http://35.224.128.24/api/payment';
    this.order_rating='http://35.224.128.24/api/updateRating';
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
  orderHistory_Kitchen(Order_Kitchen:any):Observable<Order_Kitchen>{
    console.log(Order_Kitchen)
    return this.http.post<Order_Kitchen>(this.orderKitchen,Order_Kitchen);
  }
  order_changestatus(Order_status:any):Observable<any>{
    //console.log(Order_status)
    return this.http.post<any>(this.orderstatus,Order_status);
  }
  orderHistory_Employee(Order_Employee:any):Observable<Order_employee>{
    console.log(Order_Employee)
    return this.http.post<Order_employee>(this.orderEmployee,Order_Employee);
  }
  order_pay(order:any):Observable<any>{
    console.log(order)
    return this.http.post<any>(this.order_payment,order);
  }
  order_Rating(order:any):Observable<any>{
    console.log(order)
    return this.http.post<any>(this.order_rating,order);
  }
}
