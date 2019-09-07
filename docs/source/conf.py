# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
from datetime import datetime

import sphinx_rtd_theme
from git import Repo

doc_path = os.path.dirname(os.path.dirname(__file__))
project_path = os.path.dirname(doc_path)
sys.path.insert(0, project_path)

# -- Project information -----------------------------------------------------

repo = Repo(search_parent_directories=True)
commits = list(reversed(list(repo.iter_commits())))
start = datetime.now().year
end = start
if commits:
    start = commits[0].committed_datetime.year
    end = commits[-1].committed_datetime.year
if start == end:
    copyright_date = start
else:
    copyright_date = f'{start}-{end}'

project = 'pol'
copyright = f'{copyright_date}, Trim21'
author = 'Trim21'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx.ext.autodoc',
    'sphinx.ext.githubpages',
    'sphinxcontrib.httpdomain',
    'sphinxcontrib.httpexample',
    'sphinxcontrib.openapi',
    'sphinx_issues',
]

# Github repo
issues_github_path = 'Trim21/personal-website'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'zh-CN'

# html_favicon = '_static/logo144.jpg'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
