import { TestBed } from '@angular/core/testing';

import { ProjetsService } from './projets.service';

describe('ProjectsService', () => {
  let service: ProjetsService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ProjetsService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
