import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { Login } from '../shared/model/Login';

@Injectable({
  providedIn: 'root',
})
export class ApiService {
  loginURL:string;
  corsURL = 'https://cors-anywhere.herokuapp.com/';
  constructor(private http : HttpClient){
    this.loginURL=this.corsURL +'http://35.224.128.24/api/signin';
  }

  login(logindata:Login):Observable<Login>{

    console.log(this.loginURL)
    return this.http.post<Login>(this.loginURL,logindata);
  }

}
