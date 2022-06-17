import { HttpErrorResponse } from '@angular/common/http';
import { NgForm } from '@angular/forms';
import { Component, OnInit } from '@angular/core';
import { ApplicationService } from 'src/app/Services/application.service';
import { Router } from '@angular/router';
import { Tweet } from 'src/app/Models/Tweet';
import { Result } from 'src/app/Models/Result';

@Component({
  selector: 'app-tweetpolarity',
  templateUrl: './tweetpolarity.component.html',
  styleUrls: ['./tweetpolarity.component.css']
})
export class TweetpolarityComponent implements OnInit {

  public req : Tweet= new Tweet();
  public sentiment : String = new String();
  public polarity : Number = new Number();
  public hideResult = true;

  constructor(private applicationService : ApplicationService) { }

  ngOnInit(): void {
  }

  onClickSubmit(data: any) {
     console.log("Entered Email id : " + data.txt);
   }

  public resetSentiment(){
    this.sentiment = ''
    this.hideResult = true
  }

   public GetPolarity(requestForm : NgForm){
    this.hideResult = false
    this.applicationService.GetPolarity(this.req).subscribe(
      (response: Result[]) => {
        if(response[0].value==1){
          this.sentiment = "Positif"
          this.polarity = 1
        }  
        else{
          this.sentiment = "Negatif"
          this.polarity = 0
        }   
      },
      (error: HttpErrorResponse) => {
        alert(error.message);
        requestForm.reset();
      }
    );
  }

}
