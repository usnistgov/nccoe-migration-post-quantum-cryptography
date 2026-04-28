# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

sys.path.append(os.path.abspath("_themes"))

# -- Project information -----------------------------------------------------

project = 'Migration to Post-Quantum Cryptography'
copyright = 'NIST'
author = 'NIST'



# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# The master toctree document.
master_doc = "FAQ/index"

redirects = {
        "index": "FAQ/index.html"
}


extensions = [
    'sphinxcontrib.rsvgconverter',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx_design',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'nccoe_rtd_theme',
    "sphinxcontrib.mermaid",
    "sphinx_datatables",
    "sphinx_reredirects",
]

# Optionally include the spelling extension only if it's installed
try:
    import sphinxcontrib.spelling
except Exception:
    pass
else:
    extensions.append("sphinxcontrib.spelling")

templates_path = ['_templates']
source_suffix = '.rst'
gettext_compact = False
exclude_patterns = ['build', 'Thumbs.db', '.DS_Store', '.git']

suppress_warnings = ['image.nonlocal_uri']
pygments_style = 'default'




html_logo = "_static/img/nccoe-logo.svg"
html_show_sourcelink = False
html_favicon = "_static/img/favicon.ico"

html_theme = "nccoe_rtd_theme"
html_theme_path = [os.path.abspath("_themes")]
html_static_path = ['_static']
html_theme_options = {
    'logo_only': False,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': True,
    'vcs_pageview_mode': '',
    'style_nav_header_background': 'white',
    'flyout_display': 'hidden',
    'version_selector': False,
    'language_selector': False,
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False,
    'project_page': 'https://www.nccoe.nist.gov/applied-cryptography/migration-to-pqc'
}
html_css_files = [
    "custom.css"
]

html_js_files = [
    "main.js"
]

numfig = True

redirects = {
     "<source>": "<target>"
}

rst_epilog = """
.. |repo_base| replace:: https://gitlab.nist.gov/<group>/<repo>/-/blob/main
.. |config_base| replace:: config
"""

spelling_word_list_filename = ["_themes/nccoe_rtd_theme/dictionaries/spelling_wordlist.txt"] # you can add more wordlist files here
