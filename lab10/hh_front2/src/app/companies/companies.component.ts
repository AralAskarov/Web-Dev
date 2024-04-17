import { Component, OnInit } from '@angular/core';
import { Company } from '../models';
import { CompanyServiceService } from '../company-service.service';
import { CommonModule } from '@angular/common'; 
import { RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router'; 
@Component({
  selector: 'app-companies',
  standalone: true,
  imports: [CommonModule, RouterOutlet, RouterLink, RouterLinkActive,],
  templateUrl: './companies.component.html',
  styleUrl: './companies.component.css'
})

export class CompaniesComponent implements OnInit {
  companies!: Company[];
  loaded: boolean;
  newCompany: string;
  constructor(private companiesservice: CompanyServiceService) { 
    this.newCompany = '';
    this.loaded = false;
  }

  ngOnInit(): void {
    this.getCompanies();
  }
  getCompanies():void{
    this.loaded = false;
    this.companiesservice.getCompanies().subscribe((companies) => {
      this.companies = companies;
      this.loaded = true;
    });
  }
  
}
