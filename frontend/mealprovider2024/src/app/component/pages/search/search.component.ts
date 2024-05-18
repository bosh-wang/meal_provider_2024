import { ActivatedRoute, Router} from '@angular/router';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-search',
  standalone: true,
  imports: [],
  templateUrl: './search.component.html',
  styleUrl: './search.component.css'
})
export class SearchComponent implements OnInit{
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
      this.router.navigateByUrl('/search/' + term);
  }
}
