# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import genoray

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "GenVarLoader"
copyright = "2025, David Laub"
author = "David Laub"
release = genoray.__version__
# X.Y.Z verison
version = ".".join(release.split(".")[:3])

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
templates_path = ["_templates"]
exclude_patterns = []

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx_autodoc_typehints",
    "myst_parser",
]

autodoc_typehints = "description"
autodoc_class_signature = "mixed"
autodoc_typehints_format = "short"
autodoc_default_options = {"members": True, "private-members": False}
autodoc_member_order = "groupwise"
autodoc_preserve_defaults = True

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
}

napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_use_param = True
# napoleon_type_aliases = {
#     "Path": ":py:class:`Path <pathlib.Path>`",
#     "Callable": ":class:`Callable <typing.Callable>`",
#     "ArrayLike": ":external+numpy:term:`ArrayLike <array_like>`",
#     "NDArray": ":external+numpy:class:`NDArray <numpy.typing.NDArray>`",
# }
napoleon_preprocess_types = True
napoleon_use_rtype = True

# autodoc typehints
always_use_bar_unions = True
simplify_optional_unions = True
typehints_defaults = "comma"

myst_enable_extensions = ["colon_fence", "deflist", "dollarmath", "amsmath"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"
html_title = f"genoray v{version}"
# html_logo = "_static/gvl_logo.svg"
# html_favicon = "_static/favicon.ico"
html_static_path = ["_static"]
html_theme_options = {
    "repository_url": "https://github.com/d-laub/genoray",
    "repository_branch": "main",
    "path_to_docs": "docs",
    "use_fullscreen_button": True,
    "use_issues_button": True,
    "use_repository_button": True,
    "use_source_button": True,
    "pygments_light_style": "tango",
    "pygments_dark_style": "material",
    "home_page_in_toc": True,
    "collapse_navigation": True,
    "show_toc_level": 3,
}
html_sidebars = {
    "**": [
        "navbar-logo.html",
        "icon-links.html",
        "search-button-field.html",
        "sbt-sidebar-nav.html",
    ]
}
