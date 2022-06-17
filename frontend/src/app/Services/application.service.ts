import { Injectable } from '@angular/core';
import { HttpClient} from '@angular/common/http';
import { Observable } from 'rxjs/internal/Observable';
import { Request } from 'src/app/Models/Request';
import { Result } from '../Models/Result';
import { Tweet } from '../Models/Tweet';

@Injectable({
  providedIn: 'root'
})


export class ApplicationService {

  public SERVER_URL: string = 'http://127.0.0.1:8081/api/';

constructor(private http : HttpClient) { }

private results : Result[] | any;

public analyse(requete : Request) : Observable<Result[]>{
  return this.http.post<Result[]>(`${this.SERVER_URL}analyse`,requete);
}

public setResults(resultats : Result[]) : void {
  this.results = resultats;
}

public getResults() : Result[]{
  return this.results;
}

private polarity: Number| any;

public GetPolarity(req : Tweet) : Observable<Result[]>{
  return this.http.post<Result[]>(`${this.SERVER_URL}GetPolarity`,req);
}



}
