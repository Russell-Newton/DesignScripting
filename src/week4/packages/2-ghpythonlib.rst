=========================================================
``ghpythonlib.treehelpers``: Using lists instead of trees
=========================================================

This is a really small module that contains two things we'll use:

``tree_to_list``
================

If you have Tree Access set on your input variable, you can use ``tree_to_list`` to
convert it to a nested list.

.. code-block:: python
    :caption: With an input parameter ``x`` set to Tree Access

    import ghpythonlib.treehelpers as th

    x = th.tree_to_list(x)

Note that by default, this actually converts the tree rooted at ``{0}`` to a nested
list, meaning a path ``{0;A;B}`` will be equivalent to ``x[A][B]``. If your tree has
multiple roots, pass ``None`` as the second parameter:

.. code-block:: python

    import ghpythonlib.treehelpers as th

    x = th.tree_to_list(x, None)
    # {0;A;B} now at x[0][A][B]
    # {1;C;D} now at x[1][C][D]
    # etc.

``list_to_tree``
================

Converts a nested list into a data tree, rooted at ``{0}``.

.. code-block:: python
    :caption: With an output parameter ``out_tree``

    import ghpythonlib.treehelpers as th

    out_tree = th.tree_to_list([
        [0, 1],
        [2, 3],
        [4, 5, 6]
    ])

The above example creates a data tree that, when displayed in a panel, will look like:

.. code-block:: none
    :caption: {0;0}
    :linenos:
    :lineno-start: 0
    :class: gh-panel

    0
    1

.. code-block:: none
    :caption: {0;1}
    :linenos:
    :lineno-start: 0
    :class: gh-panel

    2
    3

.. code-block:: none
    :caption: {0;2}
    :linenos:
    :lineno-start: 0
    :class: gh-panel

    4
    5
    6
