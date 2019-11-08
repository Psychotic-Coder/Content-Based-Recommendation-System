import { Component, OnInit } from '@angular/core';
import { HttpService } from './app.services';

@Component({
  selector: 'laptop-list',
  template: '<h2>{{laptops}}</h2>',
  styleUrls: ['./app.component.css'],
  providers: [ HttpService ]
})
export class LaptopListComponent{
  
}
