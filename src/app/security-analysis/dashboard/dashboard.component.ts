import { Component } from '@angular/core';

@Component({
    selector: 'app-dashboard',
    template: `
        <div class="default-info">
            <div class="body-col">
                <h3>Discounted Cashflow</h3>
                <div class="col-row">
                    <span>Cash and Equivalents</span>
                    <span>1232</span>
                </div>
                <div class="col-row">
                    <span>Short-Term Assets</span>
                    <span>1232</span>
                </div>
                <div class="col-row">
                    <span>Long-Term Assets</span>
                    <span>1232</span>
                </div>
                <div class="col-row">
                    <span>Discounted Cashflow</span>
                    <span>1232</span>
                </div>
                <hr style="border-color: black" />
                <div class="col-row">
                    <span>Intrinsic Value</span>
                    <span>1232</span>
                </div>
                <div class="col-row">
                    <span>Price</span>
                    <span>1232</span>
                </div>
                <hr style="border-color: black" />
                <div class="col-row">
                    <span>Net Margin of Safety</span>
                    <span>1232</span>
                </div>
                <div class="col-row">
                    <span>Margin of Safety</span>
                    <span>1232</span>
                </div>
            </div>
            <div class="body-col">
                <h3 align="center">Capital Structure</h3>
                <h4 align="center" style="color: orange">Moderate Leverage</h4>
                <div class="col-row">
                    <span>Debt-to-Capital-Ratio</span>
                    <span>1232</span>
                </div>
                <div class="col-row">
                    <span>Debt-to-Equity-Ratio <br> (D/E)</span>
                    <span>1232</span>
                </div>
                <div class="col-row">
                    <span>Interest Coverage <br> Ratio</span>
                    <span>1232</span>
                </div>
                <div class="col-row">
                    <span>Degree of Combined <br> Leverage</span>
                    <span>1232</span>
                </div>
                <div class="col-row">
                    <span>Degree of Operating <br> Leverage (DOL)</span>
                    <span>1232</span>
                </div>
                <div class="col-row">
                    <span>Degree of Financial <br> Leverage</span>
                    <span>1232</span>
                </div>
            </div>
            <div class="body-col">
                <h3 align="center">Management Effectiveness</h3>
                <div class="col-row">
                    <span>Price to Earnings Ration (P/E)</span>
                    <span>1232</span>
                </div>
                <div class="col-row">
                    <span>Earning Yield (E/P)</span>
                    <span>1232</span>
                </div>
                <div class="col-row">
                    <span>Absolue P/E</span>
                    <span>1232</span>
                </div>
                <div class="col-row">
                    <span>Relative P/E</span>
                    <span>1232</span>
                </div>
                <div class="col-row">
                    <span>Return on Equity (ROE)</span>
                    <span>1232</span>
                </div>
                <div class="col-row">
                    <span>Return on Invested Capital (ROIC)</span>
                    <span>1232</span>
                </div>
                <div class="col-row">
                    <span>Retention Ratio</span>
                    <span>1232</span>
                </div>
                <div class="col-row">
                    <span>Sustainable Growth Rate</span>
                    <span>1232</span>
                </div>
                <div class="col-row">
                    <span>Return on Assets (ROA)</span>
                    <span>1232</span>
                </div>
                <div class="col-row">
                    <span>Price to Book (P/B)</span>
                    <span>1232</span>
                </div>
            </div>
        </div>
    `,
    styleUrls: ['dashboard.component.scss']
})
export class DashboardComponent { }
