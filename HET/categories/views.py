from django.shortcuts import render, redirect
from .forms import CategoriesForm


def categories_form(request):
    if request.method == 'POST':
        form = CategoriesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories_form')
        else:
            form = CategoriesForm()

        return render(request, 'categories/categories_form.html', {'form': form})


