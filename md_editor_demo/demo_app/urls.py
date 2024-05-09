from django.urls import path
from .views import index, article


urlpatterns = [
    path('', index, name='index'),
    path("articles/<int:id>", article, name="article_page"),
]