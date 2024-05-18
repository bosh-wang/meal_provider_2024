import { CommonModule } from '@angular/common';
import { Component, Input, OnInit } from '@angular/core';
import { RouterOutlet, RouterLink, RouterLinkActive } from '@angular/router';

@Component({
  selector: 'app-not-found',
  standalone: true,
  imports: [CommonModule, RouterOutlet, RouterLink, RouterLinkActive],
  templateUrl: './not-found.component.html',
  styleUrl: './not-found.component.css'
})
export class NotFoundComponent implements OnInit{
  @Input()
  visible = false;

  @Input()
  notFoundMessage = "Nothing Found!";

  @Input()
  resetLinkText = "Reset";

  @Input()
  resetLinkRoute = "/";

  constructor() {

  }

  ngOnInit(): void {

  }
}
