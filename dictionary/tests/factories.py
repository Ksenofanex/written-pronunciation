import factory

from dictionary.models import Word
from users.tests.factories import UserFactory


class WordFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Word

    english = factory.Faker("word")
    turkish = "Fektri"
    is_approved = True

    # ForeignKeys
    author = factory.SubFactory(UserFactory)
