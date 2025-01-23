=================================================
``rhinoscriptsyntax``: Helper functions for Rhino
=================================================

This is a big module made by McNeel to make a lot of the geometry nonsense you might
want to do with Rhino objects easier. While I won't cover everything there is to see
in the module here, I'll include some links to things you might find useful.

.. warning::

    Not every function provided in ``rhinoscriptsyntax`` is available for use within
    Grasshopper. If you try to use one of the invalid functions, you'll be met with an
    error.

The full list of functions available can be found `here <https://developer.rhino3d.com/api/RhinoScriptSyntax/>`__

.. note::

    This package is often import like:

    .. code-block:: python

        import rhinoscriptsyntax as rs

    Because ``rs`` is easier to type than ``rhinoscriptsyntax``.

Could be Worth Looking Into
===========================

* `Curve functions <https://developer.rhino3d.com/api/RhinoScriptSyntax/#curve>`__
* `AddPoint <https://developer.rhino3d.com/api/RhinoScriptSyntax/#geometry-AddPoint>`__
  and `IsPoint <https://developer.rhino3d.com/api/RhinoScriptSyntax/#geometry-IsPoint>`__
* `Surface functions <https://developer.rhino3d.com/api/RhinoScriptSyntax/#surface>`__

Additional Notes
================

Basically everything that can be done with ``rhinoscriptsyntax`` can be done with
Grasshopper nodes, but you might find it useful to have these functions available.

Furthermore, ``rhinoscriptsyntax`` accepts and returns GUIDs. You'll want to make sure
your type hints work with this, if applicable. Geometry you create with these functions
can be coerced to their corresponding type, but no preview will be shown in the viewport
unless you output the GUID to a variable (regardless of type hinting):

.. code-block:: python
    :caption: With an output pin ``out_line`` set to type Line

    import rhinoscriptsyntax as rs

    out_line = rs.AddLine((0, 0, 0), (20, 20, 20))
    # Even though out_line is a GUID, it will get coerced into a line
