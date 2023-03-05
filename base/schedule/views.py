from django.shortcuts import render
from django.http import HttpResponse

#добавить папку schedule в template
# https://www.youtube.com/watch?v=Z4IwTFgXtrA



def index(request):

    return render(request, "schedule/index.html", context={"title": "Расписание"})
