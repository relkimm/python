from django.urls import path
from app.views import index, post_detail

urlpatterns = [
    path("", index),
    path("<int:id>/", post_detail),
]
