from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import IndexView, SobreView, CursosView, CursoViewSet, ContatoView, Cadastro, erro, custom_logout
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from .views import IndexView, SobreView, CursosView
from . import views

router = SimpleRouter()
router.register('cursos', CursoViewSet)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('cursos/', CursosView.as_view(), name='cursos'),
    path('contato/', ContatoView.as_view(), name='contato'),
    path('login/', LoginView.as_view(), name='login'),
    path('cadastro/', Cadastro, name='cadastro'),
    path('erro-login/', erro, name='erro'),
    path('logout/', custom_logout, name='custom_logout'), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)