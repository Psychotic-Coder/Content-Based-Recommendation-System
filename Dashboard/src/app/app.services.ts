import { Injectable } from '@angular/core';
import { Http,Response } from '@angular/http';

//IMPORT FOR MAP FUNCTION
import 'rxjs/add/operator/map';

@Injectable()
export class HttpService {
    // CONSTRUCTOR FOR HTTP 
    constructor(private http: Http){}

    // URL FOR THE SERVER
    private url = "http://localhost:8000/rec"
    
    // FUNCTION FOR GETTING RESPONSE AND CONVERT TO JSON
    getData(){
        return this.http.get(this.url)
        .map((res: Response) => res.json())
    }
}