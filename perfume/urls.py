from django.urls import include, path
from .views import (
    PerfumeListApiView,
    DesignerListApiView,
    NoteListApiView,
    AccordListApiView,
)


# Specify URL path for rest_framework
urlpatterns = [
    path("perfume", PerfumeListApiView.as_view(), name="perfume"),
    path("designers", DesignerListApiView.as_view(), name="designer"),
    path("notes", NoteListApiView.as_view(), name="note"),
    path("accords", AccordListApiView.as_view(), name="accord"),
]
