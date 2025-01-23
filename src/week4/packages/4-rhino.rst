============================================
``Rhino``: Python bindings of Rhino's C# API
============================================

Sometimes, a Grasshopper node or ``rhinoscriptsyntax`` function doesn't do exactly
what you want it to do. It should be possible, but the behavior isn't quite right.
In cases like these, you might have to resort to using the
`RhinoCommon API <https://developer.rhino3d.com/api/rhinocommon/?version=8.x>`__.

Although it's all written in C#, you can access it through Python. For example, if you
wanted to make use of Rhino's Vector3d struct, you could do:

.. code-block:: python

    from Rhino.Geometry import Vector3d

For the most part in this class, we won't be using this library for anything other
than type hints, which lets you have access to the attributes and functions associated
to your variables.
