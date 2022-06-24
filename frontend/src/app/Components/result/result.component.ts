import { Component, OnInit } from '@angular/core';
import { Result } from 'src/app/Models/Result';
import { ApplicationService } from 'src/app/Services/application.service';
import { Chart,registerables } from 'node_modules/chart.js';

@Component({
  selector: 'app-result',
  templateUrl: './result.component.html',
  styleUrls: ['./result.component.css']
})
export class ResultComponent implements OnInit {

  constructor(private applicationService : ApplicationService) { 
    Chart.register(...registerables);
  }

  public results : Result[] = [];

  public drawResults(){
    this.results = this.applicationService.getResults();
    console.log(this.results);
    var chartExist1 = Chart.getChart("graphe_bar"); // <canvas> id
    var chartExist2 = Chart.getChart("graphe_circle");
    if (chartExist1 != undefined)
      chartExist1.destroy();
    if (chartExist2 != undefined)
      chartExist2.destroy();


    const graphe_bar = new Chart("graphe_bar",{
      type : 'bar',
      data : {
        datasets : [{
          label : "Sentiments analysés",
          data : this.results,
          backgroundColor: [
            'rgb(0, 0, 255)',
            'rgb(255, 0, 0)'
          ]
        }]
      },
      options: {
        responsive : true,
        parsing: {
          xAxisKey: 'name',
          yAxisKey: 'value'
        },
        scales : {
          x : {
            title : {
              display : true,
              text : "Sentiments",
              font : {
                size : 20,
                weight : "bold"
              },
              color : "#000"
            }
          },
          y : {
            title : {
              display : true,
              text : "Nombre de Tweets",
              font : {
                size : 20,
                weight : "bold"
              },
              color : "#000"
            }
          }
        }
      }
    })


    const graphe_circle = new Chart("graphe_circle",{
      type : 'pie',
      data : {
        datasets : [{
          label : "Sentiments analysés",
          data : this.results,
          backgroundColor: [
            'rgb(0, 0, 255)',
            'rgb(255, 0, 0)'
          ]
        }],
        labels : ['positif','négatif']
      },
      options: {
        responsive : true,
        plugins : {
          legend : {
            display : true,
            position : "top"
          }
        }
      }
    })
    
  }

  ngOnInit(): void {
    this.drawResults()
  }

}
