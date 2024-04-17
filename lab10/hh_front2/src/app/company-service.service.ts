import { Injectable } from '@angular/core';
import {Observable, of} from 'rxjs';
import {HttpClient} from '@angular/common/http';
import {Company} from './models';
@Injectable({
  providedIn: 'root'
})
export class CompanyServiceService {
  BASE_URL = 'http://127.0.0.1:8000/api';

  constructor(private client: HttpClient) { }
  getCompanies(): Observable<Company[]> {
    return this.client.get<Company[]>(`${this.BASE_URL}/company`);
  }

  getCompany(id: number): Observable<Company> {
    return this.client.get<Company>(`${this.BASE_URL}/company/${id}`);
  }

  getCompanyVacancies(id: number): Observable<any> {
    return this.client.get(`${this.BASE_URL}/company/${id}/vacancy`)
  }
}
