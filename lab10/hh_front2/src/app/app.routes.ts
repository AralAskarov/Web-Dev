import { NgModule } from '@angular/core';
import { RouterModule} from '@angular/router';
import {HomeComponent} from './home/home.component';
import {CompaniesComponent} from './companies/companies.component';
import {CompanyDetailsComponent} from './company-details/company-details.component';
import {VacanciesComponent} from './vacancies/vacancies.component';
import { Routes } from '@angular/router';


export const routes: Routes = [
  {path: 'home', component: HomeComponent},
  {path: 'companies', component: CompaniesComponent},
  {path: 'companies/:id', component: CompanyDetailsComponent},
  {path: 'companies/:id/vacancies', component: VacanciesComponent},
  {path: '', redirectTo: 'home', pathMatch: 'full'},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
