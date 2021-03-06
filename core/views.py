import platform

import django
import iommi
from django.urls import reverse_lazy
from iommi import Page, html


class MyPage(Page):
    class Meta:
        h_tag__tag = "h4"


def hyperlink(link_text, url_name, enclosing_tag=True):
    return html.a(link_text, attrs__href=reverse_lazy(url_name))


class VersionInfo(MyPage):
    class Meta:
        title = "Versions"

    versions = html.ul(
        html.li(f"Python: {platform.python_version()}"),
        html.li(f"Django: {django.__version__}"),
        html.li(f"Iommi: {iommi.__version__}"),
    )


class DatabaseRecords(MyPage):
    class Meta:
        title = "Database Records"

    model_pages = html.ul(
        html.li(hyperlink("Artists", url_name="artists")),
        html.li(hyperlink("Albums", url_name="albums")),
    )


class Cookbook(MyPage):
    class Meta:
        title = "Cookbook"

    recipes = html.ul(
        html.li(html.i("TODO"))
    )


class Pitfalls(MyPage):
    class Meta:
        title = "Pitfalls"

    class PageTitleWrong(MyPage):
        title = "This text is *not* recognised as a page title"

    class PageTitleCorrect(MyPage):
        class Meta:
            title = "This is properly recognised as the page title"

    pitfalls = html.ul(
        html.li(
            html.p(
                "Page title must be set in the `Meta` class. "
                "Can we at least produce a warning if the user tries to set the 'title' attribute directly? "
                "It seems like a common mistake that beginners might make.",
                attrs__style={"font-size": "smaller", "font-style": "italic"}
            ),
            PageTitleWrong(),
            PageTitleCorrect())
    )


def error_example(title, *paragraphs, url_name):
    return html.li(
        hyperlink(title, url_name=url_name),
        *(
            html.div(paragraph_text, attrs__style={"padding-top": "10px", "font-size": "smaller"})
            for paragraph_text in paragraphs
        )
    )


class ImprovableErrorMessages(MyPage):
    class Meta:
        title = "Improvable Error Messages"

    intro_text = html.div(
        "The following examples deliberately produce errors. "
        "They are meant to illustrate examples where the error message could be clearer.",
        attrs__style={"padding-top": "5px", "padding-bottom": "15px", "font-style": "italic"},
    )

    error_pages = html.ul(
        error_example(
            "Page parts must be dict, not list",
            (
                """
                I tried to create a page by passing a list of its parts instead of a dict, like so:
                `Page(parts=[...])`.
                """
            ),
            (
                """
                The current error message is:
                `descriptor 'items' for 'dict' objects doesn't apply to a 'list' object`.
                While this is reasonably clear, it doesn't provide any context why
                this error occurs. It would be nice to add an explanation, possibly
                linking to the docs page "Everything in iommi has a name".
                """
            ),
            url_name="error_page_parts_must_be_dict_not_list",
        ),
    )


def index(request):
    return Page(
        parts=dict(
            version_info=VersionInfo(),
            model_pages=DatabaseRecords(),
            cookbook=Cookbook(),
            pitfalls=Pitfalls(),
            error_pages=ImprovableErrorMessages(),
        )
    )
