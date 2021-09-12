# django-sphinx-view-example

An example Django project demonstrating a potential configuration and structure for [django-sphinx-view](https://github.com/carltongibson/django-sphinx-view).

## Setting up the project

1. Install [Poetry](https://python-poetry.org/docs/#installation) for dependency management.
2. Run `poetry shell && poetry install` to install the dependencies.

## Writing and building the docs

1. Save [reStructuredText (reST)](https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html) files containing the documentation content to the `docs/source/` directory.
2. From the `docs/` directory, run the `make json` command to build the documentation to be served from the `docs/build` directory.

## Viewing the docs

Run `./manage.py runserver` and navigate to http://localhost:8000/docs/ in your browser.
