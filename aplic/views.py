from django.views.generic import TemplateView, ListView
from django.utils import translation
from .models import Curso
from rest_framework import permissions
from rest_framework import viewsets
from aplic.serializers import CursoSerializer
from .forms import CursoSearchForm

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        lang = translation.get_language()
        context['cursos'] = Curso.objects.order_by('?').all()
        context['lang'] = lang
        translation.activate(lang)
        return context

class SobreView(TemplateView):
    template_name = 'sobre-nos.html'

class CursosView(TemplateView):
    template_name = 'cursos.html'

class CursoViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions, )

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

def curso(request):
    template_name = 'cursos.html'
    form = CursoSearchForm(request.GET)
    objects = Curso.objects.all()

    if form.is_valid():
        search = form.cleaned_data['search']
        if search:
            objects = objects.filter(nome_curso__icontains=search)

    context = {'object_list': objects, 'form': form}
    return render(request, template_name, context)
