from typing import Any
from categories.models import Categories
from categories.forms import CategoriesForm


class CategoryEntyty:
    def get_categories_list(self):
        all_categories = Categories.objects.all()
        return all_categories


class Controller:

    def __init__(self):
        self._category_entyty = CategoryEntyty()

    def render_categories_page(self, request) -> dict[str, Any]:
        categories = self._category_entyty.get_categories_list()
        return {'test': 'test',
                'categories': categories}

    def add_category(self, request):
        form = CategoriesForm(request.POST)
        if form.is_valid():
            form.save()

