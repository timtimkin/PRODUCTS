from django.views.generic import ListView, DetailView  # импортируем класс, который говорит нам о том, что в этом представлении мы будем выводить список объектов из БД
from .models import Product
from datetime import datetime
from django.views import View    #  импортируем простую вьюшку
from django.core.paginator import Paginator    #  импортируем класс, позволяющий удобно осуществлять постраничный вывод
from django.shortcuts import render

 
class ProductsList(ListView):
    model = Product  
    template_name = 'products.html'
    context_object_name = 'products'
    queryset = Product.objects.order_by('-id')

    # метод get_context_data нужен нам для того, чтобы мы могли передать переменные в шаблон. В возвращаемом словаре context будут храниться все переменные. Ключи этого словари и есть переменные, к которым мы сможем потом обратиться через шаблон
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow() # добавим переменную текущей даты time_now
        context['value1'] = None # добавим ещё одну пустую переменную, чтобы на её примере посмотреть работу другого фильтра
        return context
 
 
# создаём представление, в котором будут детали конкретного отдельного товара
class ProductDetail(DetailView):
    model = Product # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'product.html' # название шаблона будет product.html
    context_object_name = 'product' # название объекта

class Products(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    ordering = ['-price']
    paginate_by = 1 # поставим постраничный вывод в один элемент

class Products(View):
    
    def get(self, request):
        products = Product.objects.order_by('-price')
        p = Paginator(products, 1) # создаём объект класса пагинатор, передаём ему список наших товаров и их количество для одной страницы
 
        products = p.get_page(request.GET.get('page', 1)) # берём номер страницы из get-запроса. Если ничего не передали, будем показывать первую страницу.
        # теперь вместо всех объектов в списке товаров хранится только нужная нам страница с товарами
        
        data = {
            'products': products,
        }
        return render(request, 'production/product_list.html', data)
