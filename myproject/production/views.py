from django.views.generic import ListView, DetailView  # импортируем класс, который говорит нам о том, что в этом представлении мы будем выводить список объектов из БД
from .models import Product


class ProductsList(ListView):
    model = Product  # указываем модель, объекты которой мы будем выводить
    template_name = 'products.html'  # указываем имя шаблона, в котором будет лежать HTML, в нем будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'products'  # это имя списска, в котором будут лежать все объекты, его надо указать, чтобв обратиться к самому списку объектов через HTML-шаблон


class ProductDetail(DetailView):
    model = Product  # указываем модель, объекты которой мы будем выводить
    template_name = 'products.html'  # указываем имя шаблона, в котором будет лежать HTML, в нем будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'products'  # это имя списска, в котором будут лежать все объекты, его надо указать, чтобв обратиться к самому списку объектов через HTML-шаблон

       




