from django.urls import path, re_path
from django.conf.urls import include
from django.views.generic import ListView, DetailView
from .models import Product
from . import views

urlpatterns = [

    path('products/<int:pk>', views.NewdetailView.as_view(), name='detail'),
    path('products/<int:pk>/update/', views.ProductUpdateView.as_view(), name='update-product'),
    path('products/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='delete-product'),
    path('products/',
         ListView.as_view(queryset=Product.objects.all().order_by('-date'),
                          template_name='budget/products.html'),name='products'),
    path('', views.index, name='budget'),
]

# urlpatterns = [
#     path('<int:pk>/', DetailView.as_view(model = Product,template_name = "budget\product.html")),
#     path("", ListView.as_view(queryset=Product.objects.all().order_by("date"),template_name="budget/products.html" )),
#     # re_path(r'^$', views.index, name='budget'),
#
# ]
