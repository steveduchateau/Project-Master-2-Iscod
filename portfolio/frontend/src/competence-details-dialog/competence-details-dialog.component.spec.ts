import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CompetenceDetailsDialogComponent } from './competence-details-dialog.component';

describe('CompetenceDetailsDialogComponent', () => {
  let component: CompetenceDetailsDialogComponent;
  let fixture: ComponentFixture<CompetenceDetailsDialogComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CompetenceDetailsDialogComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CompetenceDetailsDialogComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
