from rest_framework import generics, viewsets

from core.models import Content
from core.serializers import ContentSerializer


class ContentListCreateView(generics.ListCreateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer


class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_field = "slug"
