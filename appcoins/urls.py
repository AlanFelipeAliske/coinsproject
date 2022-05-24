from django.urls import path

from appcoins.views import inicio, sobre, servicos, contato


urlpatterns = [
    path('', inicio),
    path('sobre/', sobre),
    path('servicos/', servicos),
    path('contato/', contato),
]