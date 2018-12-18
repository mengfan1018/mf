from django.shortcuts import render
from django.http import HttpResponse

from .models import Post


def index(request):
    post_list = Post.objects.order_by('-modified_time')[:]
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)
