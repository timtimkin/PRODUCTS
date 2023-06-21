from django.views.generic import ListView, DetailView  # импортируем класс, который говорит нам о том, что в этом представлении мы будем выводить список объектов из БД
from .models import Product

 
class ProductsList(ListView):
    model = Product  
    template_name = 'products.html'
    context_object_name = 'products'
 
 
# создаём представление, в котором будут детали конкретного отдельного товара
class ProductDetail(DetailView):
    model = Product # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'one_product.html' # название шаблона будет product.html
    context_object_name = 'product' # название объекта



