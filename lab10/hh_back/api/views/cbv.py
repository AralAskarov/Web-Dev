from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Company, Vacancy
from api.serializers import CompanySerializer, VacancySerializer


class CompanyListAPIView(APIView):
    def get(self, request):
        categories = Company.objects.all()
        serializer = CompanySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
    

class CompanyDetailAPIView(APIView):

    def get_object(self, pk=None):
        try:
            category = Company.objects.get(id=pk)
            return category
        except Company.DoesNotExist as e:
            return Response({"error": str(e)},
                            status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        category = self.get_object(pk)
        serializer = CompanySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk=None):
        category = self.get_object(pk)
        serializer = CompanySerializer(
            instance=category,
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()  # update table ...
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        category = self.get_object(pk)
        category.delete()
        return Response({"deleted": True})
    

class CompanyVacancyList(APIView):
    serializer_class = VacancySerializer

    def get_queryset(self):
        company_id = self.kwargs['company_id']
        return Vacancy.objects.filter(company_id=company_id)
    


class CompanyVacancyList(APIView):

    def get(self, request, company_id):
        vacancies = Vacancy.objects.filter(company_id=company_id)
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)
    def post(self, request, company_id):
        data = request.data
        data['company'] = company_id  
        serializer = VacancySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class VacancyListAPIView(APIView):
    def get(self, request):
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VacancySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
    

class VacancyDetailAPIView(APIView):

    def get_object(self, pk=None):
        try:
            vacancy = Vacancy.objects.get(id=pk)
            return vacancy
        except Company.DoesNotExist as e:
            return Response({"error": str(e)},
                            status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        vacancy = self.get_object(pk)
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data)

    def put(self, request, pk=None):
        vacancy = self.get_object(pk)
        serializer = VacancySerializer(
            instance=vacancy,
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()  # update table ...
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        vacancy = self.get_object(pk)
        vacancy.delete()
        return Response({"deleted": True})

class TopTenVacancies(APIView):
    serializer_class = VacancySerializer  
    def get(self, request):
        vacancies = Vacancy.objects.order_by('-salary')[:10]
        serializer = self.serializer_class(vacancies, many=True)
        return Response(serializer.data)
