import { Routes } from '@angular/router';
import { HealthCheckComponent } from './modules/health-check/health-check.component';

export const routes: Routes = [
    { path: '', redirectTo: 'health-check', pathMatch: 'full' },
    {
        path: 'health-check',
        title: 'Heal Check',
        component: HealthCheckComponent,
    },
];
