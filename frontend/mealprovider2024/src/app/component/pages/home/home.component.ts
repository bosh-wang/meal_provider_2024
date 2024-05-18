import { Component, OnInit } from '@angular/core';
import { FoodService } from '../../../services/food.service';
import { Food } from '../../../shared/model/Food';
import { CommonModule } from '@angular/common';
import { ActivatedRoute, RouterLink, RouterLinkActive, RouterModule, RouterOutlet } from '@angular/router';
import { SearchComponent } from '../search/search.component';
import { TagComponent } from '../tag/tag.component';
import { NotFoundComponent } from '../not-found/not-found.component';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule, RouterOutlet, RouterLink, RouterLinkActive, SearchComponent, TagComponent, NotFoundComponent],
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  food:Food[] = [];

  constructor(private api:FoodService, activateRoute:ActivatedRoute){
    activateRoute.params.subscribe((params)=>{
      if(params.searchTerm)
        this.food = this.api.getAllFoodBySearchTerm(params.searchTerm) // get data satisfy search term
      else if(params.tag)
        this.food = this.api.getAllFoodByTag(params.tag)
      else
        this.food = api.getAll() //get All data return
    })
  }
  ngOnInit(){}
}
