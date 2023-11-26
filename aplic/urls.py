from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import IndexView, SobreView, CursosView, ContatoView


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('cursos/', CursosView.as_view(), name='cursos'),
    path('contato/', ContatoView.as_view(), name='contato'),
]