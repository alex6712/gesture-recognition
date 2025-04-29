import { ApplicationConfig, provideZoneChangeDetection } from '@angular/core';
import { provideRouter } from '@angular/router';

import { routes } from './app.routes';
import { provideHttpClient, withInterceptors } from '@angular/common/http';
import { HealthCheckService } from './state/health-check/health-check.service';
import { APIBaseUrlInterceptor } from './core/interceptors/api-base-url.interseptor';
import { catchErrorInterceptor } from './core/interceptors/catch-error.interceptor';

export const appConfig: ApplicationConfig = {
    providers: [
        HealthCheckService,
        provideHttpClient(
            withInterceptors([APIBaseUrlInterceptor, catchErrorInterceptor]),
        ),
        provideRouter(routes),
        provideZoneChangeDetection({ eventCoalescing: true }),
    ],
};
