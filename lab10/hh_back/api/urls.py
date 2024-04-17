from django.urls import path
from . import views
from .views import CompanyListAPIView, CompanyDetailAPIView, CompanyVacancyList, VacancyListAPIView, VacancyDetailAPIView, TopTenVacancies
from .views import company_list, company_detail, company_vacancies, vacancy_list, vacancy_detail, top_ten_vacancies
from api.views import index
urlpatterns = [
    path('', index, name='home'),
    path('api/company', CompanyListAPIView.as_view(), name='company-list'),
    path('api/company/<int:pk>/', CompanyDetailAPIView.as_view(), name='company-detail'),
    path('api/company/<int:company_id>/vacancy/', CompanyVacancyList.as_view(), name='company-vacancy-list'),
    path('api/vacancy', VacancyListAPIView.as_view(), name='vacancy-list'),
    path('api/vacancy/<int:pk>/', VacancyDetailAPIView.as_view(), name='vacancy-detail'),
    path('api/vacancy/top_ten/', TopTenVacancies.as_view(), name='top-ten-vacancies'),


    path("api/companiesFUNC/", company_list),
    path("api/companiesFUNC/<int:pk>/", company_detail),
    path("api/companiesFUNC/<int:pk>/vacancy/", company_vacancies),
    path("api/vacanciesFUNC/", vacancy_list),
    path("api/vacanciesFUNC/<int:pk>/", vacancy_detail),
    path('api/vacanciesFUNC/top_ten/', top_ten_vacancies),

]
