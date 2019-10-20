import uuid
import pytest

from django.db.utils import DataError, IntegrityError

from core.models import Content

from .factories import ContentFactory


@pytest.mark.django_db
class TestContentModels:
    def test_create_content_model(self):
        content = ContentFactory(name="Content_01")
        assert content.name == "Content_01"
        assert Content.objects.all().count() == 1

    def test_invalid_choices_in_content_models(self):
        with pytest.raises(DataError):
            ContentFactory(name="Content_01", gender=100)

    def test_unique_name_in_content_model(self):
        content = ContentFactory(name="Content_01")
        assert content.name == "Content_01"
        assert Content.objects.all().count() == 1

        with pytest.raises(IntegrityError):
            ContentFactory(name="Content_01")

    def test_slug_content_manager(self):
        public_name = "Conteudo para Dias dos Pais 2019"

        content = ContentFactory(name=public_name)
        assert content.name == public_name
        assert content.slug == "conteudo-para-dias-dos-pais-2019"
