from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Post


def index(request):
    post_list = Post.objects.order_by('-modified_time')[:]
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/detail.html', {'post': post})
