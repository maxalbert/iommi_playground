import platform
import textwrap

import django
import iommi
from django.http import HttpResponse
from django.template import Template, RequestContext


def index(request):
    context = RequestContext(request)
    context["python_version"] = platform.python_version()
    context["django_version"] = django.__version__
    context["iommi_version"] = iommi.__version__
    template = Template(textwrap.dedent("""
    <h3>Versions</h3>
        <ul>
            <li>Python: {{ python_version }}</li>
            <li>Django: {{ django_version }}</li>
            <li>Iommi: {{ iommi_version }}</li>
        </ul>
        """))
    return HttpResponse(template.render(context))
