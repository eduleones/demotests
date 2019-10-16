from django.urls import path

from core import views


urlpatterns = [
    path("", views.ContentListCreateView.as_view(), name="contents"),
    path(
        "<slug:slug>/",
        views.ContentViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="contents_viewset",
    ),
]
