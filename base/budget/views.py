from django.shortcuts import render
from django.http import HttpResponse

columns = ['Категория','Название','Количество','Измерение','Цена','Действие']
items = [
        ['яйца', 'яйца', 30, 'шт', 250],
        ['мясо', 'куриная грудка', 3, 'кг', 299.9 ],
    ]

def index(request):
    # добвить категории и единицы измерения ------------------------------------------------------------------------------------

    return render(request, "budget.html",context={"columns":columns,"items":items})



def additems(request):

    # получаем из данных запроса POST отправленные через форму данные
    name = request.POST.get("name_item", "Undefined")
    category = request.POST.get("category_item", 0)
    count = request.POST.get("count_item", 0)
    measurement = request.POST.get("measurement_item", 1)
    price = request.POST.get("price_item", 0)
    date = request.POST.get("date_item", "Undefined")

    items.append([category, name,count, measurement,price])

    #cделать переход на стартовую страницу!------------------------------------------------------------------------------------
    return render(request, "budget.html",context={"columns":columns,"items":items})


