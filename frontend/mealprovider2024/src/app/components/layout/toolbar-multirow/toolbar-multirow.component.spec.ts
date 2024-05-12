import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ToolbarMultirowComponent } from './toolbar-multirow.component';

describe('ToolbarMultirowComponent', () => {
  let component: ToolbarMultirowComponent;
  let fixture: ComponentFixture<ToolbarMultirowComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ToolbarMultirowComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ToolbarMultirowComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
