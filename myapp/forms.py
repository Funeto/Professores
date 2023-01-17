from myapp.models import Professor
from django.forms import ModelForm

class ProfessorForm(ModelForm):
    class Meta:
        model = Professor
        fields = ('nome', 'disciplina', 'area', 'formacao')
        labels = {
            "nome": "Nome do professor:",
            "disciplina": "Disciplina que leciona:",
            "area": "Área do Conhecimento:",
            "formacao": "Nível de Formação Acadêmica:",
        }