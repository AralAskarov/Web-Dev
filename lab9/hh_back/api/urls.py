from django.urls import path
from . import views
from .views import CompaniesList, VacancyList, CompanyDetail, VacancyDetail,CompanyVacancyList,TopTenVacancies

urlpatterns = [
    path('', views.index, name='home'),
    path('api/company', CompaniesList.as_view(), name='company-list'),
    path('api/company/<int:pk>/', CompanyDetail.as_view(), name='company-detail'),
    path('api/company/<int:company_id>/vacancy/', CompanyVacancyList.as_view(), name='company-vacancy-list'),
    path('api/vacancy', VacancyList.as_view(), name='vacancy-list'),
    path('api/vacancy/<int:pk>/', VacancyDetail.as_view(), name='vacancy-detail'),
    path('api/vacancy/top_ten/', TopTenVacancies.as_view(), name='top-ten-vacancies'),
]
