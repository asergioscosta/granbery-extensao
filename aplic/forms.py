from django import forms

class CursoSearchForm(forms.Form):
    search = forms.CharField(required=False)
