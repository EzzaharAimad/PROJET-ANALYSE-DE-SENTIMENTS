import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { AcceuilComponent } from './Components/acceuil/acceuil.component';
import { ResultComponent } from './Components/result/result.component';
import { HttpClientModule } from '@angular/common/http';
import { NoResultComponent } from './Components/no-result/no-result.component';
import { TweetpolarityComponent } from './Components/tweetpolarity/tweetpolarity.component';


@NgModule({
  declarations: [
    AppComponent,
    AcceuilComponent,
    ResultComponent,
    NoResultComponent,
    TweetpolarityComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
