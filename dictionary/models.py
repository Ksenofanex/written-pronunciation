from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Word(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    english = models.CharField(max_length=250)
    turkish = models.CharField(max_length=250)

    def __str__(self):
        return self.english # Human readable object name.

    def get_absolute_url(self):
        return reverse('word_detail', args=[str(self.id)])
    # The get_absolute_url() method sets a canonical URL for the model.
    # It is also the correct way to refer to a model in your templates rather than hard-coding them.
