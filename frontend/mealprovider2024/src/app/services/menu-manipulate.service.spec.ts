import { TestBed } from '@angular/core/testing';

import { MenuManipulateService } from './menu-manipulate.service';

describe('MenuManipulateService', () => {
  let service: MenuManipulateService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(MenuManipulateService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
