import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CompetenceDetailsComponent } from './competence-details.component';

describe('CompetenceDetailsDialogComponent', () => {
  let component: CompetenceDetailsComponent;
  let fixture: ComponentFixture<CompetenceDetailsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CompetenceDetailsComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CompetenceDetailsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
