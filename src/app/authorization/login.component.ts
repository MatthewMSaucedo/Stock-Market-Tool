import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { NgForm } from '@angular/forms';
import { formArrayNameProvider } from '@angular/forms/src/directives/reactive_directives/form_group_name';
import { AuthService } from './auth.service';

@Component({
    selector: 'app-login',
    template: `
        <div class="input-container">
            <h1 class="input-header"> Login </h1>
            <div class="input-body">
                <form #registrationForm="ngForm" (ngSubmit)="onSubmit(registrationForm)">
                    <div class="form-group shorter-input-box">
                        <input type="text"
                            id="username"
                            class="form-control"
                            name="username"
                            ngModel
                            maxlength="12"
                            required
                            placeholder="Username"
                        />
                    </div>
                    <div class="form-group shorter-input-box">
                        <input type="password"
                            id="password"
                            class="form-control"
                            name="password"
                            type="password"
                            ngModel
                            minlength="6"
                            required
                            placeholder="Password"
                        />
                    </div>
                    <div class="text-center shorter-input-button">
                        <button
                            class="btn btn-primary btn-block"
                            type="submit"
                            [disabled]="!registrationForm.valid">
                            Login
                        </button>
                    </div>
                </form>
                <div class="text-center">
                    <h4>
                        Don't have an account? <br /> Click
                        <a (click)="onRegisterClick()" class="register-button">here</a>
                        to register. <br />
                    </h4>
                </div>
            </div>
        </div>
    `,
    styleUrls: ['login.component.css']
})
export class LoginComponent implements OnInit {

    constructor(
        public router: Router,
        public activatedRoute: ActivatedRoute,
        public authService: AuthService
    ) { }

    ngOnInit() {
        this.authService.currentView.next("login");
    }

    public onRegisterClick(): void {
        this.authService.currentView.next("register");
        this.router.navigate( ['../register'], {relativeTo: this.activatedRoute} );
    }

    public onSubmit( form: NgForm ): void {
        console.log(form.value);
        form.reset();
    }
}
