import { HttpErrorResponse } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { Request } from 'src/app/Models/Request';
import { Result } from 'src/app/Models/Result';
import { ApplicationService } from 'src/app/Services/application.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-acceuil',
  templateUrl: './acceuil.component.html',
  styleUrls: ['./acceuil.component.css']
})
export class AcceuilComponent implements OnInit {

  public requete : Request = new Request();
  public hidePage = false;
  public dots : String = "...";
	public i=0;

  constructor(private router: Router, private applicationService : ApplicationService) { }

  ngOnInit(): void {

  }

  public analyse(requestForm : NgForm){
    console.log(this.requete);
    this.applicationService.analyse(this.requete).subscribe(
      (response: Result[]) => {
        this.applicationService.setResults(response);
        if(response[0].value!=0)
          this.router.navigate(['/resultats']);
        else
        this.router.navigate(['/no-results']);
        requestForm.reset();
      },
      (error: HttpErrorResponse) => {
        alert(error.message);
        requestForm.reset();
      }
    );
    this.hidePage = true;
    //this.printDots();
  }

  /*public printDots(){
    while(true){
      this.dots = this.dots + ".";
      this.i ++;
      if(this.i%5 == 0)
        this.dots = "";
    }
  }*/
}
