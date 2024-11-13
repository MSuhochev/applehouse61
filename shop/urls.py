from django.urls import path
from shop import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home')
]
