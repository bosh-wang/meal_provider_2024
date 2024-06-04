import { ActivatedRoute, Router} from '@angular/router';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-food-search',
  standalone: true,
  imports: [],
  templateUrl: './food-search.component.html',
  styleUrl: './food-search.component.css'
})
export class FoodSearchComponent {
  searchTerm: any;
  constructor(activatedRoute:ActivatedRoute, private router:Router){
    this.searchTerm = ''; // initial value
    activatedRoute.params.subscribe((params)=>{
      if(params.searchTerm)
        this.searchTerm = params.searchTerm;
    });
  }
  ngOnInit(): void {

  }
  search(term:string){
    if(term)
      this.router.navigateByUrl('/food-search/' + term);
  }
}
