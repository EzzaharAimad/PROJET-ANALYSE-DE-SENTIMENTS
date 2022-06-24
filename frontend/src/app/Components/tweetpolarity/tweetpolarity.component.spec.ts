import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TweetpolarityComponent } from './tweetpolarity.component';

describe('TweetpolarityComponent', () => {
  let component: TweetpolarityComponent;
  let fixture: ComponentFixture<TweetpolarityComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TweetpolarityComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(TweetpolarityComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
