from django.db import models

class Company(models.Model):
    name=models.CharField('Имя компании', max_length=50)
    description=models.TextField('Описание')
    city=models.CharField('Город', max_length=50)
    address=models.TextField('Адрес')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

class Vacancy(models.Model):
    name=models.CharField('Название вакансии', max_length=50)
    description=models.TextField('Описание')
    salary=models.FloatField('Зарплата в тенге')
    company=models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Компания', related_name='vacancies')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'