from django.conf import settings
from django.db import models
from django.urls import reverse


class Word(models.Model):
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="words",
        related_query_name="word",
    )
    english = models.CharField(
        verbose_name="english word", max_length=250, unique=True
    )
    turkish = models.CharField(verbose_name="turkish word", max_length=250)

    class Meta:
        verbose_name = "Word"
        verbose_name_plural = "Words"
        ordering = ["english"]

    def __str__(self):
        return self.english

    def get_absolute_url(self):
        return reverse("word-detail", args=[str(self.id)])
