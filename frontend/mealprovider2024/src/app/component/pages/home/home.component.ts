import { campus_request } from './../../../shared/model/Campus_name';
import { campus_name } from './../../../../data';
import { Observable, filter } from 'rxjs';
import { Component, OnInit, inject } from '@angular/core';
import { FoodService } from '../../../services/food.service';
import { Food } from '../../../shared/model/Food';
import { CommonModule } from '@angular/common';
import {
  ActivatedRoute,
  RouterLink,
  RouterLinkActive,
  RouterOutlet,
} from '@angular/router';
import { SearchComponent } from '../search/search.component';
import { TagComponent } from '../tag/tag.component';
import { NotFoundComponent } from '../not-found/not-found.component';
import { Restaurant } from '../../../shared/model/Restaurant';
import { RestaurantService } from '../../../services/restaurant.service';
import { RestaurantTypeComponent } from '../restaurant-type/restaurant-type.component';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { json } from 'stream/consumers';
import { ApiService } from '../../../services/api.service';
import { Campus_name } from '../../../shared/model/Campus_name';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [
    CommonModule,
    HttpClientModule,
    RouterOutlet,
    RouterLink,
    RouterLinkActive,
    SearchComponent,
    TagComponent,
    NotFoundComponent,
    RestaurantTypeComponent,
  ],
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
})
export class HomeComponent implements OnInit {
  food: Food[] = [];
  restaurant: Restaurant[] = [];
  data: any[] = [];
  campus_name: Campus_name[] = [];
  private apiUrl = 'http://35.224.128.24:80';

  constructor(
    private restaurantService: RestaurantService,
    private activateRoute: ActivatedRoute,
    private apiService: ApiService
  ) {
    this.activateRoute.params.subscribe((params) => {
      if (params['searchTerm']) {
        this.restaurant = this.restaurantService.getAllRestaurantBySearchTerm(
          params['searchTerm']
        );
      } else if (params['tag-type']) {
        this.restaurant = this.restaurantService.getAllRestaurantByTag(
          params['tag-type']
        );
      } else if (params['campus-name']) {
        this.campus_name = [{ name: [params['campus-name']] }];
        var name: campus_request = {
          campus: this.campus_name[0] ? this.campus_name[0].name[0] : '',
        };

        this.apiService.getRestaurants(name).subscribe((res) => {
          console.log(res, 'response');
          this.restaurant = [res];
        });

        this.restaurant = this.restaurantService.getAllRestaurantByCampus(
          params['campus-name']
        );
      } else {
        this.restaurant = this.restaurantService.getAll();
      }
    });
  }

  ngOnInit(): void {}

  httpClient = inject(HttpClient);

  fetchData() {
    this.httpClient
      .get('http://35.224.128.24:80/api/restaurants')
      .subscribe((data: any) => {
        console.log(data);
        this.data = data;
      });
  }
  getRestaurant(): Observable<Restaurant> {
    return this.httpClient.post<Restaurant>(
      '${this.apiUrl}/api/restaurants',
      {}
    );
  }
}
