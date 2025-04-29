import { HttpInterceptorFn } from '@angular/common/http';
import { catchError, throwError } from 'rxjs';

import { ApiErrorModel } from '../../models/api-response.model';

export const catchErrorInterceptor: HttpInterceptorFn = (request, next) => {
    return next(request).pipe(
        catchError((err: ApiErrorModel) => {
            return throwError(() => err);
        }),
    );
};
