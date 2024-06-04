import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OrderDashboardComponent } from './order-dashboard.component';

describe('OrderDashboardComponent', () => {
  let component: OrderDashboardComponent;
  let fixture: ComponentFixture<OrderDashboardComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [OrderDashboardComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(OrderDashboardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
