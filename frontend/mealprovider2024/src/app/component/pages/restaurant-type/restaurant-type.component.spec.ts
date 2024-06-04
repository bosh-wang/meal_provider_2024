import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RestaurantTypeComponent } from './restaurant-type.component';

describe('RestaurantTypeComponent', () => {
  let component: RestaurantTypeComponent;
  let fixture: ComponentFixture<RestaurantTypeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [RestaurantTypeComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(RestaurantTypeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
