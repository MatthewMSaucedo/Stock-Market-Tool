import { Component, OnInit } from '@angular/core';

@Component({
    selector: 'app-home',
    template: `
        <body>
            <div class="container" >
                <h1>
                    Hey there
                </h1>
            </div>
        </body>
    `,
    styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

    constructor() { }

    ngOnInit() {
        ;
    }
}
