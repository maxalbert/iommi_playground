from django.urls import path
from iommi import Table, Page, html

from . import views
from .models import Artist, Album


def error_page_parts_must_be_dict_not_list(request):
    return Page(parts=[html.div("Error")])


urlpatterns = [
    path("", views.index, name="index"),
    path("artists/", Table(auto__model=Artist).as_view(), name="artists"),
    path("albums/", Table(auto__model=Album).as_view(), name="albums"),
    path(
        "errors/page_parts_must_be_dict_not_list",
        error_page_parts_must_be_dict_not_list,
        name="error_page_parts_must_be_dict_not_list",
    ),
]
