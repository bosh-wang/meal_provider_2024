import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OrderHRComponent } from './order-hr.component';

describe('OrderHRComponent', () => {
  let component: OrderHRComponent;
  let fixture: ComponentFixture<OrderHRComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [OrderHRComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(OrderHRComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
