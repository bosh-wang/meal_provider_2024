import { campus_name } from './../../data';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { Restaurant } from '../shared/model/Restaurant';
import { Campus_name, campus_request } from '../shared/model/Campus_name';

@Injectable({
  providedIn: 'root',
})
export class ApiService {
  loginURL:string;
  corsURL = 'https://cors-anywhere.herokuapp.com/';
  constructor(private http : HttpClient){
    this.loginURL='https://cors-anywhere.herokuapp.com/http://35.224.128.24:80/api/restaurants';
  }

  getRestaurants(campus_name:campus_request):Observable<Restaurant>{
    return this.http.post<Restaurant>(this.loginURL,campus_name);
  }
}
