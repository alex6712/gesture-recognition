import { HttpInterceptorFn } from '@angular/common/http';
import { environment } from '../../../env/environment';

export const APIBaseUrlInterceptor: HttpInterceptorFn = (request, next) => {
    const urlRegexp = /https?:\/\/\S+\/api/;

    const url = request.url.startsWith('http')
        ? request.url.replace(urlRegexp, environment.APIBaseUrl)
        : `${environment.APIBaseUrl}/${request.url}`;

    const updatedRequest = request.clone({ url });
    return next(updatedRequest);
};
