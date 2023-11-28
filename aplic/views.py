from django.urls import reverse_lazy
from django.views.generic import TemplateView

from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework import permissions
from aplic.serializers import CursoSerializer

from .models import Curso

from django.utils.translation import gettext as _
from django.utils import translation

from .forms import ContatoForm

from django.contrib import messages

from django.db.models import Q

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

    def get_context_data(self, **kwargs):
        context = super(CursosView, self).get_context_data(**kwargs)
        
        query = self.request.GET.get("iptText")
        print(query)
        
        if (query is None):
            context['cursos'] = Curso.objects.order_by('id').all()
            print('não tinha nada digitado no iptText')
        else:
            context['cursos'] = Curso.objects.filter(Q(nome_curso__icontains=query))
            context['cursos'] = Curso.objects.filter(Q(descricao__icontains=query))

        return context

class CursoViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions, )

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class ContatoView(TemplateView):
    template_name = 'contato.html'
    form_class = ContatoForm
    success_url = reverse_lazy('contato')

    def get_context_data(self, **kwargs):
        context = super(ContatoView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, _('E-mail enviado com sucesso'), extra_tags='success')
        return super(ContatoView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, _('Falha ao enviar e-mail'), extra_tags='danger')
        return super(ContatoView, self).form_invalid(form, *args, **kwargs)
