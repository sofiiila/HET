from typing import Any


class CategoryEntyty:
    def get_categories_list(self):
        return ['pussy', 'ASS']



class Controller:

    def __init__(self):
        self._category_entyty = CategoryEntyty()

    def render_categories_page(self) -> dict[str, Any]:
        categories = self._category_entyty.get_categories_list()
        return {'test': 'test',
                'categories': categories}


name = Controller()
print(name.render_categories_page())
