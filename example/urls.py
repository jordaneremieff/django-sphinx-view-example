from pathlib import Path

from django.contrib import admin
from django.urls import path

from sphinx_view import DocumentationView


urlpatterns = [
    path(
        "docs<path:path>",
        DocumentationView.as_view(
            json_build_dir=Path("docs/build/json"),
            base_template_name="docs_base.html",
        ),
        name="documentation",
    ),
]
