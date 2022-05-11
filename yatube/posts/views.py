from django.shortcuts import get_object_or_404, render
from .models import Post
from .models import Group


def index(request):
    template = 'posts/index.html'
    text = Post.objects.order_by('-pub_date')[:10]
    context = {
        'text': text,
    }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    template = 'posts/group_list.html'
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
