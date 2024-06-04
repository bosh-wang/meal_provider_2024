import { campus_name } from './../../data';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError } from 'rxjs/operators';
import {
  AllRestaurant,
  ResIDUserRole,
  Restaurant,
  Restaurantinfomation,
} from '../shared/model/Restaurant';
import { Campus_name, campus_request } from '../shared/model/Campus_name';
import { Login } from '../shared/model/Login';
import { Order_HR, Order_Kitchen, Order_employee } from '../shared/model/Order';
import { NewFood } from '../shared/model/addfood';
import { Food, FoodRes } from '../shared/model/Food';

@Injectable({
  providedIn: 'root',
})
export class ApiService {

  loginURL: string;
  orderHR: string;
  order_paymentNotification: string;
  orderKitchen: string;
  orderstatus: string;
  orderEmployee: string;
  order_payment: string;
  order_rating: string;
  change_menu: string;
  getpdfURL: string;
  apiURL: string;
  updatecartURL: string;
  getrestaurantURL: string;
  getmenuURL: string;
  menu_itemURL: string;
  constructor(private http: HttpClient) {
    this.apiURL = 'http://backend:5000/api/';
    this.getrestaurantURL = this.apiURL + 'restaurants';
    this.getmenuURL = this.apiURL + 'menu';
    this.loginURL = this.apiURL + 'signin';
    this.orderHR = this.apiURL + 'orderHistoryHR';
    this.order_paymentNotification = this.apiURL + 'paymentNotification';
    this.orderKitchen = this.apiURL + 'orderHistoryRestaurant';
    this.orderstatus = this.apiURL + 'change_order_status';
    this.orderEmployee = this.apiURL + 'orderHistoryEmployee';
    this.order_payment = this.apiURL + 'api/payment';
    this.order_payment = this.apiURL + 'api/payment';
    this.order_rating = this.apiURL + 'updateRating';
    this.change_menu = this.apiURL + 'change_menu_item';
    this.getpdfURL = this.apiURL + 'generatePDF';
    this.updatecartURL = this.apiURL + 'update_cart';
    this.menu_itemURL = this.apiURL + 'menu_item';
  }
  getRestaurants(campus_name: campus_request): Observable<Restaurantinfomation[]> {
    return this.http.post<Restaurantinfomation[]>(
      this.getrestaurantURL,
      campus_name
    );
  }
  getFoods(res_id_user_role: ResIDUserRole): Observable<FoodRes[]> {
    return this.http.post<FoodRes[]>(this.getmenuURL, res_id_user_role);
  }
  getFoods_item(item_id: string): Observable<FoodRes> {
    console.log({ 'item_id': item_id });
    return this.http.post<FoodRes>(this.menu_itemURL, { 'item_id': item_id });
  }
  updateCart(cart_data: any): Observable<any> {
    return this.http.post<any>(this.updatecartURL, cart_data);
  }
  login(logindata: Login): Observable<any> {
    console.log(this.loginURL)
    return this.http.post<any>(this.loginURL, logindata);
  }
  orderHistory_HR(order_HR: any): Observable<any> {

    return this.http.post<any>(this.orderHR, order_HR);
  }
  order_HRpaymentNotification(user_id: any): Observable<any> {

    return this.http.post<any>(this.order_paymentNotification, user_id);
  }
  orderHistory_Kitchen(Order_Kitchen: any): Observable<any> {

    return this.http.post<any>(this.orderKitchen, Order_Kitchen);
  }
  order_changestatus(Order_status: any): Observable<any> {

    return this.http.post<any>(this.orderstatus, Order_status);
  }
  orderHistory_Employee(Order_Employee: any): Observable<any> {

    return this.http.post<any>(this.orderEmployee, Order_Employee);
  }
  order_pay(order: any): Observable<any> {

    return this.http.post<any>(this.order_payment, order);
  }
  order_Rating(order: any): Observable<any> {

    return this.http.post<any>(this.order_rating, order);
  }
  Change_menu(menu_item: any): Observable<any> {

    return this.http.post<any>(this.change_menu, menu_item);
  }
  Get_PDF(): Observable<any> {
    return this.http.get<any>(this.getpdfURL);
  }
}
