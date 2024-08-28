from django import forms
from .models import Categories


class CategoriesForm(forms.ModelForm):
    class Meta:
        models = Categories
        fields = ['section', 'name']
        labels = {
            'section': 'Раздел',
            'name': 'Название',
        }

