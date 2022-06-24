import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AcceuilComponent } from './Components/acceuil/acceuil.component';
import { NoResultComponent } from './Components/no-result/no-result.component';
import { ResultComponent } from './Components/result/result.component';
import { TweetpolarityComponent } from './Components/tweetpolarity/tweetpolarity.component';
import { ErrorPageComponent } from './Components/error-page/error-page.component';

const routes: Routes = [
  {path : 'acceuil' , component : AcceuilComponent},
  { path: '', redirectTo : 'acceuil', pathMatch : 'full'},
  {path : 'resultats' , component : ResultComponent},
  {path : 'no-results' , component : NoResultComponent},
  {path : 'tweetpolarity' , component : TweetpolarityComponent},
  {path : 'error' , component : ErrorPageComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
