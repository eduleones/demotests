import pytest

from django.urls import reverse as r

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Content

from .factories import ContentFactory


@pytest.mark.django_db
class TestContentViews:
    def setup(self):
        self.client = APIClient()

    def test__get_contents(self):

        ContentFactory(name="Promoção Nike de Natal")

        url = r("content:contents")

        response = self.client.get(url, format="json")
        assert response.status_code == status.HTTP_200_OK

        data = response.json()["results"]
        assert data[0]["name"] == "Promoção Nike de Natal"
        assert data[0]["slug"] == "promocao-nike-de-natal"
        assert len(data) == 1

    def test__get_contents_with_pagination(self):

        for i in range(0, 60):
            ContentFactory(name=str(i))

        url = r("content:contents")

        response = self.client.get(url, format="json")
        assert response.status_code == status.HTTP_200_OK
        assert response.json()["count"] == 60

        data = response.json()["results"]
        assert isinstance(data, list)
        assert len(data) == 30

    def test__create_content(self, content_payload):

        url = r("content:contents")

        payload = content_payload

        response = self.client.post(url, data=payload, format="json")
        assert response.status_code == status.HTTP_201_CREATED

        data = response.json()
        assert payload["name"] == data["name"]
        assert data["gender_name"] == "Male"

    def test__create_content_with_invalid_payload(self, content__invalid_payload):

        url = r("content:contents")

        payload = content__invalid_payload

        response = self.client.post(url, data=payload, format="json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test__get_content_with_slug(self):

        content = ContentFactory(name="Campanha Natal 2019")

        for i in range(0, 60):
            ContentFactory(name=str(i))

        url = r("content:contents_viewset", args=[content.slug])

        response = self.client.get(url, format="json")

        assert response.status_code == status.HTTP_200_OK
        data = response.json()

        assert data["name"] == content.name
        assert data["slug"] == content.slug

    def test__get_content_not_found(self):

        url = r("content:contents_viewset", args=[10])

        response = self.client.get(url, format="json")

        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test__put_content(self, content_payload):

        content = ContentFactory(name="Campanha Natal 2019")

        url = r("content:contents_viewset", args=[content.slug])

        payload = content_payload

        response = self.client.put(url, data=payload, format="json")
        assert response.status_code == status.HTTP_200_OK

        data = response.json()
        assert payload["name"] == data["name"]

    def test__put_content_with_partial_payload(self, content_payload_partial):

        content = ContentFactory(name="Campanha Natal 2019")

        url = r("content:contents_viewset", args=[content.slug])

        payload = content_payload_partial

        response = self.client.put(url, data=payload, format="json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test__put_content_not_found(self):

        url = r("content:contents_viewset", args=["test-slug-invalid"])

        response = self.client.put(url, format="json")

        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test__patch_content(self, content_payload_partial):

        content = ContentFactory(name="Dias das mães")

        url = r("content:contents_viewset", args=[content.slug])

        payload = content_payload_partial

        response = self.client.patch(url, data=payload, format="json")
        assert response.status_code == status.HTTP_200_OK

        data = response.json()
        assert data["name"] == "Partial Name"
        assert data["slug"] == "partial-name"

    def test__patch_content_not_found(self):

        url = r("content:contents_viewset", args=[370])
        response = self.client.patch(url, format="json")

        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test__delete_content(self):

        content = ContentFactory(name="Dias das mães")

        assert Content.objects.filter(pk=content.pk).count() == 1

        url = r("content:contents_viewset", args=[content.slug])
        response = self.client.delete(url, format="json")

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Content.objects.filter(pk=content.pk).count() == 0

    def test__delete_content_not_found(self):

        url = r("content:contents_viewset", args=[370])
        response = self.client.delete(url, format="json")

        assert response.status_code == status.HTTP_404_NOT_FOUND