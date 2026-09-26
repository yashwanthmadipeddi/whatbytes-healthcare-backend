from django.urls import path

from .views import (
    MappingListCreateView,
    MappingPatientListDeleteView,
)


urlpatterns = [
    path(
        "",
        MappingListCreateView.as_view(),
        name="mapping-list-create",
    ),
    path(
        "<int:pk>/",
        MappingPatientListDeleteView.as_view(),
        name="mapping-patient-list-delete",
    ),
]
