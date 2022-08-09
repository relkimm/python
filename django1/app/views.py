from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.ß
from app.models import Post


def index(request: HttpRequest) -> HttpResponse:
    qs = Post.objects.all()
    return render(request, "app/index.html", {"post_list": qs})


def post_detail(request: HttpRequest, id: int) -> HttpResponse:
    # post = Post.objects.get(pk=id)
    post = get_object_or_404(Post, pk=id)
    return render(
        request,
        "app/post_detail.html",
        {
            "post": post,
        },
    )
