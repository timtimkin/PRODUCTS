from django.views.generic import ListView, DetailView  # импортируем класс, который говорит нам о том, что в этом представлении мы будем выводить список объектов из БД
from .models import Product
from django.shortcuts import render
def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)


class ProductsList(ListView):
    model = Product  # указываем модель, объекты которой мы будем выводить
    template_name = 'products.html'  # указываем имя шаблона, в котором будет лежать HTML, в нем будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'products'  # это имя списска, в котором будут лежать все объекты, его надо указать, чтобв обратиться к самому списку объектов через HTML-шаблон


class ProductDetail(DetailView):
    model = Product  # указываем модель, объекты которой мы будем выводить
    template_name = 'products.html'  # указываем имя шаблона, в котором будет лежать HTML, в нем будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'products'  # это имя списска, в котором будут лежать все объекты, его надо указать, чтобв обратиться к самому списку объектов через HTML-шаблон

       




