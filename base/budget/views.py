from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ProductForm
from .models import Product
from django.urls import reverse_lazy,reverse
#встроенные классы в ДЖанго - их еще много
from django.views.generic import DetailView,UpdateView,DeleteView

class NewdetailView(DetailView):
    model = Product
    template_name = 'budget/product.html'
    context_object_name = 'product'

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'budget.html'
    form_class = ProductForm

class ProductDeleteView(DeleteView):
    model = Product

    template_name = 'budget/product.html'

    def get_success_url(self):
        return reverse_lazy('products')


categories = [
    'Мясо',
    'Яйца',
    'Молочные продукты',
    'Хлебобулочные изделия'
]
columns = ['Категория','Название','Количество','Измерение','Цена','Действие']
items = [
        ['яйца', 'яйца', 30, 'шт', 250],
        ['мясо', 'куриная грудка', 3, 'кг', 299.9 ],
    ]

measure =['шт','гр','кг','л']

def index(request):
    error = ''
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()# сохранение в бд
            return redirect('products')
        else:
            print(request.POST)
            error = 'Форма неверна'
    form = ProductForm()

    return render(request, "budget.html",context={"columns":columns,"items":items,"form":form,"error":error})



def additems(request):
    # проверить получение данных из select с отправленными параметрами - исправить на автоматическое подставление строк в итоге ---------------------------------------------------------------
    # получаем из данных запроса POST отправленные через форму данные
    name = request.POST.get("name_item", "Undefined")
    category_item = request.POST.get("category_item", 0)
    category = categories[int(category_item)]
    count = request.POST.get("count_item", 0)
    measure_item = request.POST.get("measurement_item", 0)
    measurement = measure[int(measure_item)]
    price = request.POST.get("price_item", 0)
    date = request.POST.get("date_item", "Undefined")

    print([category, name,count, measurement,price])
    items.append([category, name,count, measurement,price])

    #cделать переход на стартовую страницу!------------------------------------------------------------------------------------
    return render(request, "budget.html",context={"columns":columns,"items":items})


