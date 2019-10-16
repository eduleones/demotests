import factory
from core.models import Content


class ContentFactory(factory.django.DjangoModelFactory):

    is_active = True

    class Meta:
        model = Content
