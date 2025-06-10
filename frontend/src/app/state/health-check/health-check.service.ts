import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { catchError, Observable, tap, throwError } from 'rxjs';
import { ApiResMessageModel } from '../../models/api-response.model';

@Injectable({ providedIn: 'root' })
export class HealthCheckService {
    constructor(private http: HttpClient) {}

    checkAPI(): Observable<ApiResMessageModel> {
        return this.http.get<ApiResMessageModel>('').pipe(
            tap((apiState) => {
                return apiState;
            }),
            catchError((err) => {
                return throwError(() => err);
            }),
        );
    }

    checkModel(): Observable<ApiResMessageModel> {
        return this.http.get<ApiResMessageModel>('model/').pipe(
            tap((modelState) => {
                return modelState;
            }),
            catchError((err) => {
                return throwError(() => err);
            }),
        );
    }
}
