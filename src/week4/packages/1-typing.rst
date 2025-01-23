===============================
``typing``: Advanced Type Hints
===============================

We've learned about basic type-hints for primitives, but when you want to start
type-hinting more complicated data types, the built-in options in Python 3.9 (the
version used in Rhino 8) don't cut it. This is where the :external+python:py:mod:`typing`
package comes in.

It's rarely imported on its own. Instead, individual members are imported from it
to be used in type hints:

.. code-block:: python

    from typing import ...

.. important::

    The following syntax does nothing but instruct the type checker that a variable
    is a specific type:

    .. code-block:: python

        some_variable: SomeType

    I will use this in Grasshopper Python script nodes to match the type checker to
    the type hint specified on the input parameter.

.. warning::

    Type hinting in later versions of Python has changed to support easier syntax
    and to separate many of the type hints provided by :external+python:py:mod:`typing`
    to more relevant packages like :external+python:py:mod:`collections.abc`.

Parameterized Types
===================

Many type hints provided in the :external+python:py:mod:`typing` pacakge can be
*parameterized*. That means you can provide extra information about the data being
typed. For example, if you have a list of integers, you can use ``List[int]`` to
indicate that your list contains integers. This can be incredibly helpful for
autocompletion and intellisense because, for example, the type checker will know
that your iteration variable in a ``for`` loop is an int, which allows it to provide
more specific feedback:

.. code-block:: python

    from typing import List

    my_list: List[int] = [0, 1, 2, 3]
    for n in my_list:
        # The type checker knows that n is of type int
        ...

Useful Imports
==============

The following imports are incredibly useful to know from ``typing``:

.. include:: ../../resources/type-hints.rst
    :start-after: .. start advanced
    :end-before: .. end advanced


