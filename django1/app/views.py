from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.ß
from app.models import Post


def index(request: HttpRequest) -> HttpResponse:
    qs = Post.objects.all()
    return render(request, "app/index.html", {"post_list": qs})
