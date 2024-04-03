from django.shortcuts import render,redirect
from rest_framework import generics
from .forms import ProductForm
from .models import Product,Category
from .serializers import CategorySerializer, ProductSerializer
# Create your views here.
def index(request):
    
    return render(request, 'api/index.html')



class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
class CategoryProductList(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Product.objects.filter(category_id=category_id)
    
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('some-view-name')  # перенаправить на другую страницу после успешного добавления
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})