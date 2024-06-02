import { campus_name } from './../../data';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { Restaurant } from '../shared/model/Restaurant';
import { Campus_name, campus_request } from '../shared/model/Campus_name';
import { Login } from '../shared/model/Login';
import { Order_HR ,Order_Kitchen,Order_employee} from '../shared/model/Order';
import { NewFood } from '../shared/model/addfood';
@Injectable({
  providedIn: 'root',
})
export class ApiService {
  getresaurantURL:string;
  loginURL:string;
  orderHR:string;
  order_paymentNotification:string;
  orderKitchen:string;
  orderstatus:string;
  orderEmployee:string;
  order_payment:string;
  order_rating:string;
  change_menu:string;
  corsURL = 'https://cors-anywhere.herokuapp.com/';
  constructor(private http : HttpClient){
    this.getresaurantURL='https://cors-anywhere.herokuapp.com/http://35.224.128.24:80/api/restaurants';
    this.loginURL='http://35.224.128.24/api/signin';
    this.orderHR='http://35.224.128.24/api/orderHistoryHR';
    this.order_paymentNotification='http://35.224.128.24/api/paymentNotification';
    this.orderKitchen='http://35.224.128.24/api/orderHistoryRestaurant';
    this.orderstatus='http://35.224.128.24/api/change_order_status';
    this.orderEmployee='http://35.224.128.24/api/orderHistoryEmployee';
    this.order_payment='http://35.224.128.24/api/payment';
    this.order_rating='http://35.224.128.24/api/updateRating';
    this.change_menu='http://35.224.128.24/api/change_menu_item';
  }
  getRestaurants(campus_name:campus_request):Observable<Restaurant>{
    return this.http.post<Restaurant>(this.getresaurantURL,campus_name);
  }
  login(logindata:Login):Observable<any>{
    console.log(this.loginURL)
    return this.http.post<any>(this.loginURL,logindata);
  }

  orderHistory_HR(order_HR:any):Observable<Order_HR>{
    
    return this.http.post<Order_HR>(this.orderHR,order_HR);
  }
  order_HRpaymentNotification(user_id:any):Observable<any>{
    
    return this.http.post<any>(this.order_paymentNotification,user_id);
  }
  orderHistory_Kitchen(Order_Kitchen:any):Observable<Order_Kitchen>{
    
    return this.http.post<Order_Kitchen>(this.orderKitchen,Order_Kitchen);
  }
  order_changestatus(Order_status:any):Observable<any>{
    
    return this.http.post<any>(this.orderstatus,Order_status);
  }
  orderHistory_Employee(Order_Employee:any):Observable<Order_employee>{
    
    return this.http.post<Order_employee>(this.orderEmployee,Order_Employee);
  }
  order_pay(order:any):Observable<any>{
    
    return this.http.post<any>(this.order_payment,order);
  }
  order_Rating(order:any):Observable<any>{
    
    return this.http.post<any>(this.order_rating,order);
  }
  Change_menu(menu_item:any):Observable<any>{
    
    return this.http.post<any>(this.change_menu,menu_item);
  }
}
