from django.db import models
from django.urls import reverse


class Article(models.Model):
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    content = models.TextField()

    def get_absolute_url(self):
        return reverse("article_page", kwargs={"id": self.id})