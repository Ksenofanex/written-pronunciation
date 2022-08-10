import factory

from dictionary.models import Word
from users.tests.factories import UserFactory


class WordFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Word
        django_get_or_create = ("english",)  # To prevent unique constraint
        # error.

    english = factory.Faker("word")
    turkish = "Fektri"
    is_approved = True

    # ForeignKeys
    author = factory.SubFactory(UserFactory)
