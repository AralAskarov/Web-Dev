from django.urls import path, include
from .views import ProductList, ProductDetail,CategoryList,CategoryDetail, CategoryProductList
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('api/products', ProductList.as_view(), name='product-list'),
    path('api/products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('api/category', CategoryList.as_view(), name='product-list'),
    path('api/category/<int:pk>/', CategoryDetail.as_view(), name='product-detail'),
    path('api/category/<int:category_id>/products/', CategoryProductList.as_view(), name='category-product-list'),
]
