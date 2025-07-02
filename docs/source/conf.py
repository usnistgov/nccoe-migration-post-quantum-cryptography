# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys


# -- Project information -----------------------------------------------------

project = 'Migration to Post-Quantum Cryptography'
copyright = 'NIST'
author = 'NIST'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


exclude_patterns = ['_site', 'Thumbs.db', '.DS_Store']

extensions = [
    "myst_parser",
    "sphinxcontrib.jquery",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_togglebutton",
    "sphinx.ext.autosectionlabel",
    "sphinx_reredirects",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "restructuredtext",
    ".md": "markdown",
}

# The master toctree document.
master_doc = "FAQ/index"

redirects = {
        "index": "FAQ/index.html"
}

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

add_module_names = False

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

on_rtd = os.environ.get("READTHEDOCS") == "True"
html_theme = 'sphinx_book_theme'
html_static_path = ['_static']
html_favicon = 'images/favicon.svg'

html_css_files = [
    "content.css",
    "breadcrumbs.css"
]
html_js_files = [
    "jquery.visible.js",
    "jquery.leaveNotice-nist.js",
    "applyLeaveNotice.js",
    "smoothNavScroll.js",
]

html_theme_options = {
    "repository_branch": "main",
    "use_repository_button": False,
    "home_page_in_toc": True,
    "path_to_docs": "docs/source",
    "home_page_in_toc": True,
    "icon_links": [
        {
            "name": "Main Project Page",
            "url": "https://www.nccoe.nist.gov/crypto-agility-considerations-migrating-post-quantum-cryptographic-algorithms",
            "icon": "_static/MainProjectLogo.jpg",
            "type": "local",
        },
    ],
    "navbar_start": ["header.html"]
}