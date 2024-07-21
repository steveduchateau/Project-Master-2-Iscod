import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ProjetsDetailsDialogComponent } from './projets-details-dialog.component';

describe('ProjetsDetailsDialogComponent', () => {
  let component: ProjetsDetailsDialogComponent;
  let fixture: ComponentFixture<ProjetsDetailsDialogComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ProjetsDetailsDialogComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ProjetsDetailsDialogComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
