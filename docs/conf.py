# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
# import sphinx_rtd_theme
sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'UPPMAX intro course — part 1'
copyright = 'UPPMAX'
author = 'UPPMAX'

# The full version, including alpha/beta/rc tags
release = '0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ["sphinx_lesson",
    "sphinx.ext.githubpages",
    "sphinx_rtd_theme_ext_color_contrast",
    'sphinx-prompt',
    'sphinx.ext.autodoc',
    'sphinxcontrib.plantuml',
    'sphinx.ext.graphviz',
    "sphinxcontrib.mermaid",
    'sphinx-prompt',
    'sphinx_copybutton',
]

source_suffix = ['.rst', '.md']

master_doc = 'index'

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_admonition",
    "html_image",
    "replacements",
    "smartquotes",
    "substitution",
    "tasklist",
]
copybutton_exclude = '.linenos, .gp, .go'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']
#html_static_path = ['_static']
html_logo = "img/c_242915-l_3-k_svg-uu-logo.svg"
#html_theme_options = {
#    'logo_only': False,
#    'display_version': True,
#}
mermaid_output_format = "png"
