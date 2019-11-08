import { Component, OnInit } from '@angular/core';

// IMPORT SERVICE 
import { HttpService } from './app.services';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [ HttpService ]
})
export class AppComponent implements OnInit{
  title = 'Dashboard';
  laptops = [];

  // CONSTRUCTOR FOR HTTP OBJECT
  constructor(private data:HttpService){}

  // SUBSCRIBE TO OBSERVABLE UPON INIT
  // RESPOSNE DATA IS STORED IN LIST <laptops>
  ngOnInit(){
    this.data.getData()
    .subscribe((resData => this.laptops = resData))
  }
}
