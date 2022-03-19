from django.shortcuts import render, get_object_or_404
from .models import Category, File


def file_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    files= File.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        files = files.filter(category=category)
    return render(request, 'storage/file/list.html',
            {'category': category,
             'categories': categories,
             'files': files})


def file_detail(request, id, slug):
    file = get_object_or_404(File, id=id, slug=slug)
    return render(request, 'storage/file/detail.html', {'file': file})
