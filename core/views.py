import platform

import django
import iommi
from iommi import Page, html


def index(request):
    class VersionInfo(Page):
        class Meta:
            title = "Versions"
            h_tag__tag = "h3"

        versions = html.ul(
            html.li(f"Python: {platform.python_version()}"),
            html.li(f"Django: {django.__version__}"),
            html.li(f"Iommi: {iommi.__version__}"),
        )

    return VersionInfo()
