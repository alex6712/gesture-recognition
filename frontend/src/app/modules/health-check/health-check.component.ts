import { Component, OnInit } from '@angular/core';
import { HealthCheckService } from '../../state/health-check/health-check.service';
import { CommonModule } from '@angular/common';

@Component({
    selector: 'app-health-check',
    imports: [CommonModule],
    standalone: true,
    templateUrl: './health-check.component.html',
    styleUrl: './health-check.component.scss',
})
export class HealthCheckComponent implements OnInit {
    apiState: string = '';
    modelState: string = '';

    constructor(private healthCheckService: HealthCheckService) {}

    ngOnInit(): void {
        this.healthCheckService.checkAPI().subscribe((apiState) => {
            apiState.code === 200
                ? (this.apiState = apiState.message)
                : (this.apiState = 'Not Available');
        });

        this.healthCheckService.checkModel().subscribe((modelState) => {
            modelState.code === 200
                ? (this.modelState = modelState.message)
                : (this.modelState = 'Not Available');
        });
    }
}
