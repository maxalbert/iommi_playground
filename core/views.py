import platform

import django
import iommi
from django.urls import reverse_lazy
from iommi import Page, html


class MyPage(Page):
    class Meta:
        h_tag__tag = "h3"


def hyperlink(link_text, url_name):
    return html.li(html.a(link_text, attrs__href=reverse_lazy(url_name)))


class VersionInfo(MyPage):
    class Meta:
        title = "Versions"

    versions = html.ul(
        html.li(f"Python: {platform.python_version()}"),
        html.li(f"Django: {django.__version__}"),
        html.li(f"Iommi: {iommi.__version__}"),
    )


class ModelPages(MyPage):
    class Meta:
        title = "Pages"

    model_pages = html.ul(
        hyperlink("Artists", url_name="artists"),
    )


class ErrorPages(MyPage):
    class Meta:
        title = "Errors"

    error_pages = html.ul(
        hyperlink("Page parts must be dict, not list", url_name="error_page_parts_must_be_dict_not_list")
    )


def index(request):
    return Page(
        parts=dict(
            version_info=VersionInfo(),
            model_pages=ModelPages(),
            error_pages=ErrorPages(),
        )
    )
