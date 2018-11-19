#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import guzzle_sphinx_theme

html_theme_path = guzzle_sphinx_theme.html_theme_path()
html_theme = 'guzzle_sphinx_theme'

html_title = "QuantumFlow Documentation"
html_short_title = "QuantumFlow"


# Custom sidebar templates, maps document names to template names.
html_sidebars = {
    '**': ['logo-text.html', 'searchbox.html', 'globaltoc.html', ]
}

def setup(app):
    app.add_stylesheet("qf.css") # also can be a full URL

# -- General configuration ------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.githubpages',
    'sphinx.ext.napoleon',
    'sphinx.ext.doctest',
  #  'sphinx_autodoc_typehints',
    'sphinx.ext.inheritance_diagram',
    ]

extensions.append("guzzle_sphinx_theme")


napoleon_use_ivar = True
napoleon_use_rtype = False


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
project = 'QuantumFlow'
copyright = """2016-2018, Rigetti Computing<br>
QuantumFlow: A Quantum Algorithms Development Toolikit, 
Gavin E. Crooks (2018)<br>"""
author = 'Gavin E. Crooks'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
from quantumflow import __version__
# version = '0.0.0'
# The full version, including alpha/beta/rc tags.
release = __version__  # '0.0.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

# Guzzle theme options (see theme.conf for more information)
html_theme_options = {
    "project_nav_name": "QuantumFlow",
}

html_static_path = ['_static']



# Custom post sphinx substitutions
import atexit
import glob
import os
import re


def do_edits():

    pats = [
            # Hacks to shorten type descriptors
            (r'quantumflow\.qubits', r'qf'),
            (r'quantumflow\.ops', r'qf'),
            (r'quantumflow\.gates', r'qf'),

            (r'quantumflow\.stdgates', r'qf'),
            (r'quantumflow\.states', r'qf'),
            (r'quantumflow\.circuits', r'qf'),
            (r'qf\.programs\.instructions\.', r'qf.'),
            (r'^/quantumflow\.', r'qf.'),
            # (r'qf\.readthedocs\.io', r'quantumflow.readthedocs.io'),


            # Hacks to fixup types
            (r'sympy\.core\.symbol\.Symbol', r'Parameter'),
            (r'Sequence\[collections\.abc\.Hashable\]', 'Qubits'),
            (r'collections\.abc\.Hashable', 'Qubit'),

            (r'tensor: Any', r'tensor: TensorLike'),
            (r'&#x2192; Any', r'&#x2192; BKTensor'),

            ]

    files = glob.glob('*build/html/*.html')
    for filename in files:
        with open(filename, 'r+') as f:
            text = f.read()
            for pattern, replacement in pats:
                text = re.sub(pattern, replacement, text)
            f.seek(0)
            f.truncate()
            f.write(text)

    print('Note: post sphinx text substitutions performed (conf.py)')


atexit.register(do_edits)
