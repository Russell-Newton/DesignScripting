# Copyright (C) 2024 Georgia Tech Research Corporation. All rights reserved.

import sys
from datetime import datetime
from typing import cast

import sphinx.ext.autosectionlabel
from docutils import nodes
from sphinx.application import Sphinx
from sphinx.domains.std import StandardDomain
from sphinx.locale import __
from sphinx.util.nodes import clean_astext

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Design Scripting Docs"
copyright = f"{datetime.now().year}, Russell Newton"
author = "Russell Newton"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "linuxdoc.rstFlatTable",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.intersphinx",  # add links to other docs
    "sphinx.ext.todo",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinxcontrib.youtube",
]

templates_path = ["_templates"]
exclude_patterns = [
    "not-indexed/*.rst"
]

todo_emit_warnings = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_title = "Design Scripting"
html_static_path = ["_static"]
html_css_files = [
    "css/colors.css",
    "css/custom.css"
]
html_show_sphinx = False

html_theme_options = {
    "top_of_page_buttons": ["view"],
    "source_repository": "https://github.com/Russell-Newton/DesignScripting/",
    "source_branch": "main",
    "source_directory": "src/",
    "announcement": "<strong>Reminder:</strong> Assignment 4 is due Friday, March 7, 2025!",
    "light_css_variables": {
        "color-announcement-background": "#4f1717dd",
    },
    "dark_css_variables": {
        "color-announcement-background": "#4f1717dd",
    },
}

html_show_sourcelink = (
    False  # Remove "view source code" from top of page (for html, not python)
)

add_module_names = False

# -- Options for Linking  ----------------------------------------------------

version_link = f"{sys.version_info.major}.{sys.version_info.minor}"
intersphinx_mapping = {
    "python": ("https://docs.python.org/3.9", None),
}

# -- Patching ----------------------------------------------------------------

def register_sections_as_label(app: Sphinx, document: nodes.document) -> None:
    from sphinx.ext.autosectionlabel import get_node_depth, logger
    domain = cast(StandardDomain, app.env.get_domain('std'))
    for node in document.findall(nodes.section):
        node = cast(nodes.Element, node)
        if (app.config.autosectionlabel_maxdepth and
                get_node_depth(node) >= app.config.autosectionlabel_maxdepth):
            continue
        labelid = node['ids'][0]
        docname = app.env.docname
        title = cast(nodes.title, node[0])

        # Normally, ref_name is set as in the else block
        # Doing it this way prevents duplicate label warnings on sections that
        #  have duplicate names but also have defined labels
        if node['names']:
            ref_name = node['names'][0]
            if ref_name in domain.labels:
                continue
        else:
            ref_name = getattr(title, 'rawsource', title.astext())

        if app.config.autosectionlabel_prefix_document:
            name = nodes.fully_normalize_name(docname + ':' + ref_name)
        else:
            name = nodes.fully_normalize_name(ref_name)
        sectname = clean_astext(title)

        logger.debug(__('section "%s" gets labeled as "%s"'),
                     ref_name, name,
                     location=node, type='autosectionlabel', subtype=docname)
        if name in domain.labels:
            logger.warning(__('duplicate label %s, other instance in %s'),
                           name, app.env.doc2path(domain.labels[name][0]),
                           location=node, type='autosectionlabel', subtype=docname)

        domain.anonlabels[name] = docname, labelid
        domain.labels[name] = docname, labelid, sectname

sphinx.ext.autosectionlabel.register_sections_as_label = register_sections_as_label
