from django.shortcuts import get_object_or_404, render

from .models import Post
from .models import Group
from django.conf import settings


def index(request):
    template = 'posts/index.html'
    text = Post.objects.order_by('-pub_date')[:settings.CONST]
    context = {
        'text': text,
    }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group
                                ).order_by('-pub_date')[:settings.CONST]
    template = 'posts/group_list.html'
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)

    # Для ревьера: в третьем спринте не было информации о том,
    # как избавляться от сортировки order_by (скорее всего,
    # что это тоже из 4-го спринта, который мне только предстоит).
    # Константу [:10] я вынес в settings.py и импортировал.
