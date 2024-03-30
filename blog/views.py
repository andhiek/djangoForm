from django.shortcuts import render

# Create your views here.

from .models import PostForm


def index(request):
    post = PostForm.objects.all()
    categories = PostForm.objects.values('category').distinct()
    print(categories)
    context = {
        'page_title': 'Blog',
        'title': 'My BLog',
        'subtitle': 'Selamat Datang Di My Blog',
        'heading': '',
        'Posts': post,
        'categories': categories

    }

    return render(request, 'blog/index.html', context)


def categoryPost(request, categoryInput):
    post = PostForm.objects.filter(category=categoryInput)
    categories = PostForm.objects.values('category').distinct()
    print(categories)
    context = {
        'page_title': categoryInput,
        'title': categoryInput,
        'subtitle': '',
        'heading': '',
        'Posts': post,
        'categories': categories

    }

    return render(request, 'blog/category.html', context)


def detailPost(request, slugInput):
    post = PostForm.objects.get(slug=slugInput)
    categories = PostForm.objects.values('category').distinct()
    print(post)
    context = {
        'page_title': '',
        'title': 'Blog',
        'subtitle': '',
        'heading': '',
        'Posts': post,
        'categories': categories

    }

    return render(request, 'blog/detail.html', context)
