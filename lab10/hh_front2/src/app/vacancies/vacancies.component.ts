import { Component, OnInit } from '@angular/core';
import {Company, Vacancy} from '../models';
import {ActivatedRoute} from '@angular/router';
import {Location} from '@angular/common';
import {CompanyServiceService} from '../company-service.service';
import { CommonModule } from '@angular/common'; 
import { RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router'; 
@Component({
  selector: 'app-vacancies',
  standalone: true,
  imports: [CommonModule, RouterOutlet, RouterLink, RouterLinkActive,],
  templateUrl: './vacancies.component.html',
  styleUrl: './vacancies.component.css'
})

export class VacanciesComponent implements OnInit {
  company!: Company;
  loaded!: boolean;
  vacancies: Vacancy[];

  constructor(private route: ActivatedRoute,
              private location: Location,
              private vacancyService: CompanyServiceService) {
    this.vacancies = [];
  }

  ngOnInit(): void {
    this.getCompanyVacancies();
  }

  getCompanyVacancies(): void {
    this.route.paramMap.subscribe((params) => {
      const idParam = params.get('id');
      if(idParam!=null){
        const id = +idParam;
        this.vacancyService.getCompanyVacancies(id).subscribe((vacancy) => {
          this.vacancies = vacancy;
          this.loaded = true;
        });
      }
      
    });
  }

  goBack(): void {
    this.location.back();
  }
}
