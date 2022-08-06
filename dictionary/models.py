from django.conf import settings
from django.db import models
from django.urls import reverse


class Word(models.Model):
    english = models.CharField(
        verbose_name="english word", max_length=250, unique=True
    )
    turkish = models.CharField(verbose_name="turkish word", max_length=250)
    is_approved = models.BooleanField(
        verbose_name="is approved?", default=False
    )  # The word must be approved via admin to be visible across the site.

    # ForeignKey relations.
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="words",
        related_query_name="word",
    )

    # Date fields.
    date_created = models.DateTimeField(
        verbose_name="date created", auto_now_add=True
    )
    date_updated = models.DateTimeField(
        verbose_name="date updated", auto_now=True
    )

    class Meta:
        verbose_name = "Word"
        verbose_name_plural = "Words"
        ordering = ["english"]

    def __str__(self):
        return self.english

    def get_absolute_url(self):
        return reverse("word-detail", args=[str(self.id)])
