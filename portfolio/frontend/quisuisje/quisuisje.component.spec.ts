import { ComponentFixture, TestBed } from '@angular/core/testing';

import { QuisuisjeComponent } from './quisuisje.component';

describe('QuisuisjeComponent', () => {
  let component: QuisuisjeComponent;
  let fixture: ComponentFixture<QuisuisjeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [QuisuisjeComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(QuisuisjeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
