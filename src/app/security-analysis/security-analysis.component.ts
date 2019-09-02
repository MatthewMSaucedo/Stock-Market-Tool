import { Component, OnInit } from '@angular/core';
import { AppEndpointService } from '../server-communication/app-endpoint.service';
import { device } from 'device.js';

export enum FinancialsDisplayEnum {
    'Healthy',
    'Unhealthy'
}

// TODO: Get real values from Jimmy.
export enum FinacialsEnum {
    Healthy,
    Unhealthy
}

// TODO: Replicate on backend.
export class OwnerSummary {
    public ticker: string;
    public intrinsicValue: number;
    public oneYearGrowth: number;
    public fiveYearGrowth: number;
    public historicFin: FinacialsEnum;
    public acuteFin: FinacialsEnum;
    public projectedFin: FinacialsEnum;
    public timeToValue: number;
    public growthRate: number;
    public effectOfIntrVal: number;
}

// TODO: Ticker enum that displays as follows:
// AXP : 0, then in display enum 'American express Co. (AXP)'
// export class tickerEnum {} export class tickerDisplayEnum

@Component({
    selector: 'app-security-analysis',
    templateUrl: 'security-analysis.component.html',
    styleUrls: ['security-analysis.component.scss']
})
export class SecurityAnalysisComponent implements OnInit {
    public testData: OwnerSummary = {
        ticker: 'AXP',
        intrinsicValue: 1212,
        oneYearGrowth: 12121,
        fiveYearGrowth: 1212,
        historicFin: 0,
        acuteFin: 0,
        projectedFin: 1,
        timeToValue: 1,
        growthRate: 12,
        effectOfIntrVal: 1211
    };
    public finEnum = FinancialsDisplayEnum;
    public isMobile: boolean;
    public loadedComponent = 'dashboard';
    public mobileViewNumber = 0;

    constructor(
        private _endpointService: AppEndpointService
    ) { }

    ngOnInit() {
        // Set view according to device type.
        device.addClasses(document.documentElement);
        this.isMobile = device.mobile;
    }

    public async handleTickerSearch(tickerInput: HTMLInputElement): Promise<void> {
        // TODO: Set display to load.
        const ticker = tickerInput.value;
        // this.testData = await this._endpointService.securityAnalysis(ticker);
        // TODO: End loading, display details.
    }

    public handleComponentClick(securityComponent: string): void {
        this.loadedComponent = securityComponent;
    }

    // Change numbered view on mobile.
    public handleMoreInfoClick(): void {
        if (this.mobileViewNumber < 3) {
            this.mobileViewNumber++;
        } else {
            this.mobileViewNumber = 0;
        }
    }
}
