#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#
import os
import sys
# sys.path.insert(0, os.path.abspath('.'))

import inspect
import logging
from pathlib import Path
from datetime import datetime
from typing import Optional

from sphinx.application import Sphinx
from sphinx.ext import autosummary

from jinja2.defaults import DEFAULT_FILTERS

import matplotlib  # noqa
# Don’t use tkinter agg when importing scanpy → … → matplotlib
matplotlib.use('agg')

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
# import episcanpy  # noqa

logger = logging.getLogger(__name__)


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
#needs_sphinx = '1.0'
needs_sphinx = '1.7'  # autosummary bugfix

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
	'sphinx.ext.doctest',
    'sphinx.ext.coverage',
    'sphinx.ext.autosummary',
    'sphinx.ext.githubpages',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx_autodoc_typehints',
    'sphinx.ext.intersphinx',
    #'scanpydoc',
]

# Generate the API documentation when building
autosummary_generate = True
# both of the following two lines don't work
# see falexwolf's issue for numpydoc
autodoc_member_order = 'bysource'
# autodoc_default_flags = ['members']
napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_use_rtype = False
napoleon_use_param = True
napoleon_custom_sections = [('Params', 'Parameters')]

intersphinx_mapping = dict(
    anndata=('https://anndata.readthedocs.io/en/latest/', None),
    bbknn=('https://bbknn.readthedocs.io/en/latest/', None),
    leidenalg=('https://leidenalg.readthedocs.io/en/latest/', None),
    louvain=('https://louvain-igraph.readthedocs.io/en/latest/', None),
    matplotlib=('https://matplotlib.org/', None),
    numpy=('https://docs.scipy.org/doc/numpy/', None),
    pandas=('http://pandas.pydata.org/pandas-docs/stable/', None),
    python=('https://docs.python.org/3', None),
    scipy=('https://docs.scipy.org/doc/scipy/reference/', None),
    sklearn=('https://scikit-learn.org/stable/', None),
)

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'episcanpy'
author = 'Anna Danese, Maria Richter'
copyright = '2019, Anna Danese' #f'{datetime.now():%Y}, {author}'


# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.0.1'
# The full version, including alpha/beta/rc tags.
release = '0.0.1'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'#'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}
html_theme_options = dict(
    navigation_depth=4, # it used to be navigation_depth=2,
)

html_context = dict(
    display_github=True,      # Integrate GitHub
    github_user='AnnaDanese',   # Username
    github_repo='episcanpy',     # Repo name
    github_version='master',  # Version
    conf_py_path='/docs/',    # Path in the checkout to the docs root
)

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

def setup(app):
    app.add_stylesheet('css/custom.css')

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': [
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
    ]
}


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'episcanpydoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'episcanpy.tex', 'episcanpy Documentation',
     'Anna Danese', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'episcanpy', 'episcanpy Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'episcanpy', 'episcanpy Documentation',
     author, 'episcanpy', 'One line description of project.',
     'Miscellaneous'),
]


# -- Images for plot functions -------------------------------------------------


def api_image(qualname: str) -> str:
    # I’d like to make this a contextfilter, but the jinja context doesn’t contain the path,
    # so no chance to not hardcode “api/” here.
    path = Path(__file__).parent / 'api' / f'{qualname}.png'
    print(path, path.is_file())
    return f'.. image:: {path.name}\n   :width: 200\n   :align: right' if path.is_file() else ''


# html_context doesn’t apply to autosummary templates ☹
# and there’s no way to insert filters into those templates
# so we have to modify the default filters
DEFAULT_FILTERS['api_image'] = api_image

