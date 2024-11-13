from django.shortcuts import render
from django.views.generic import ListView
from shop.models import Product


class HomeView(ListView):
    model = Product
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Ремонт техники Apple в Ростове-на-Дону'
        return context


