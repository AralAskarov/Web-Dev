import { Component, OnInit } from '@angular/core';
import {Company, Vacancy} from '../models';
import {ActivatedRoute} from '@angular/router';
import {Location} from '@angular/common';
import { CompanyServiceService } from '../company-service.service';
import { CommonModule } from '@angular/common'; 
import { RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router'; 
@Component({
  selector: 'app-company-details',
  standalone: true,
  imports: [CommonModule, RouterOutlet, RouterLink, RouterLinkActive,],
  templateUrl: './company-details.component.html',
  styleUrl: './company-details.component.css'
})

export class CompanyDetailsComponent implements OnInit {
  company!: Company;
  loaded!: boolean;
  vacancies: Vacancy[];
  name!: string;
  constructor(private route: ActivatedRoute,
              private location: Location,
              private companyService: CompanyServiceService) {
    this.vacancies = [];
  }

  ngOnInit(): void {
    this.getCompany();
  }

  getCompany(): void {
    this.route.paramMap.subscribe((params) => {
      const idParam = params.get('id');
      if (idParam !== null) {
        const id = +idParam;
        this.loaded = false;
        this.companyService.getCompany(id).subscribe((company) => {
          this.company = company;
          this.loaded = true;
      
      });
      }
    });
  }


  goBack(): void {
    this.location.back();
  }
}
