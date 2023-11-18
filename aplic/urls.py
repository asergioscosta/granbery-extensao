from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import IndexView, SobreView, CursosView, CursoViewSet
from django.conf import settings
from django.conf.urls.static import static

router = SimpleRouter()
router.register('cursos', CursoViewSet)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('cursos/', CursosView.as_view(), name='cursos'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)