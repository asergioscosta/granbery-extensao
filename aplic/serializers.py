from rest_framework import serializers

from aplic.models import Curso

class CursoSerializer(serializers.ModelSerializer):
    disciplinas = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='disciplina-detail')

    class Meta:
        model = Curso
        fields = (
            'nome_curso',
            'descricao',
            'instituicao',
            'imagem',
            'professor',
            'aluno'
        )