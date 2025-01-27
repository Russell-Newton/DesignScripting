=================
Helpful Functions
=================

This page contains a collection of functions that you might find useful during this
course.

Built-in Functions
==================

.. start funcs

This is a living list that will expand over the course of the semester.

``print``
---------

The :external+python:py:func:`print` function allows you to output text to the console
while a program is running.

In a Grasshopper script node, instead of printing to the console, any printed text
gets sent to the ``out`` pin, which can be viewed with a Panel.

.. autofunction:: builtins::print
    :no-index:

Note how ``print`` is variadic. You can supply as many arguments as you want to it,
and each argument will be converted to a string using that object's ``__str__()``
method. The stringified arguments will then be sent to the output stream, separated
by the ``sep`` argument, which is keyword-only. In the case of a Grasshopper script node,
the default output stream is captured into the ``out`` pin.

``len``
-------

The :external+python:py:func:`len` function returns the size of a collection, or any
object that has defined the ``__len__`` method.

.. autofunction:: builtins::len
    :no-index:

``max``
-------

The :external+python:py:func:`max` function accepts items that support
"rich" comparison using ``<``, ``<=``, ``==``, ``>=``, and ``!=``. Multiple versions
can be used:

.. autofunction:: builtins::max
    :no-index:

The second version is variadic and can be provided with as many positional inputs as
you'd like. If, instead, an iterable is provided, all items within that iterable
must be comparable with the rich comparison operators.

The keyword-only parameter ``key`` accepts a function that takes in a single input
and returns a value that is richly comparable. With a ``key``, the output of the function
is instead the item, ``x``, from the input that has the maximum ``key(x)``. This can
be used, for example, to compute an "argmax", the index of the maximal item:

.. code-block:: python

    def collection_at_index(idx):
        return collection[idx]
    argmax = max(range(len(collection)), key=collection_at_index)

Note how ``collection_at_index`` is passed into ``key`` without using parentheses
to call it. This supplies the function itself to ``key`` instead of an output from
the function.

``min``
-------

The :external+python:py:func:`min` function accepts items that support
"rich" comparison using ``<``, ``<=``, ``==``, ``>=``, and ``!=``. Multiple versions
can be used:

.. autofunction:: builtins::min
    :no-index:

The second version is variadic and can be provided with as many positional inputs as
you'd like. If, instead, an iterable is provided, all items within that iterable
must be comparable with the rich comparison operators.

The keyword-only parameter ``key`` accepts a function that takes in a single input
and returns a value that is richly comparable. With a ``key``, the output of the function
is instead the item, ``x``, from the input that has the minimum ``key(x)``. This can
be used, for example, to compute an "argmax", the index of the minimal item:

.. code-block:: python

    def collection_at_index(idx):
        return collection[idx]
    argmax = min(range(len(collection)), key=collection_at_index)

Note how ``collection_at_index`` is passed into ``key`` without using parentheses
to call it. This supplies the function itself to ``key`` instead of an output from
the function.

``sorted``
----------

.. autofunction:: builtins::sorted
    :no-index:

``abs``
-------

.. autofunction:: builtins::abs
    :no-index:

``round``
---------

.. autofunction:: builtins::round
    :no-index:

``reversed``
------------

The :external+python:py:func:`reversed` function can be used to reverse a sequence,
or any object that has defined the ``__reversed__`` method.

.. autofunction:: builtins::reversed
    :no-index:

.. warning::

    :external+python:py:func:`reversed` does not return a sequence. It returns something
    that can be iterated over with a ``for`` loop, but it cannot be indexed. If you need
    a reversed version of your sequence that *can* be indexed, use a slice, as shown in
    the :ref:`slicing-examples`.

``range``
---------

.. autofunction:: builtins::range
    :no-index:

Useful in ``for`` loops.

``zip``
-------

.. function:: zip(*iterables, strict = False) -> zip object
    :no-index:

    >>> list(zip('abcdefg', range(3), range(4)))
    [('a', 0, 0), ('b', 1, 1), ('c', 2, 2)]

    The zip object yields n-length tuples, where n is the number of iterables
    passed as positional arguments to zip().  The i-th element in every tuple
    comes from the i-th iterable argument to zip().  This continues until the
    shortest argument is exhausted.

    If strict is true and one of the arguments is exhausted before the others,
    raise a ValueError.

Useful in ``for`` loops in conjunction with tuple unpacking:

.. code-block:: python

    for item1, item2 in zip(collection1, collection2):
        ...

``enumerate``
-------------

.. autofunction:: builtins::enumerate
    :no-index:

Useful in ``for`` loops in conjunction with tuple unpacking:

.. code-block:: python

    for idx, item in enumerate(collection):
        ...

Type Conversions
----------------

Many built-in types can be converted to one another by passing them to the new type's
constructor. For example, to convert something to a string, use the
:external+python:py:class:`str() <str>`. To convert something to an integer, use the
:external+python:py:class:`int() <int>`. If the conversion fails, an error will be
raised.

.. autoclass:: builtins::str
    :no-index:

.. autoclass:: builtins::int
    :no-index:

.. autoclass:: builtins::float
    :no-index:

.. autoclass:: builtins::bool
    :no-index:

.. end funcs

Doing Math
==========

.. start math

Be sure to check out the :external+python:py:mod:`math` package if you need to do
math beyond simple arithmetic operations! Click on the :external+python:py:mod:`math` to
proceed to the documentation.

.. code-block:: python

    from math import ...
    # Where "..." is a comma-separated list of things you want to import

or

.. code-block:: python

    import math
    # Where what you want can be accessed like "math.whatever"

.. end math
.. start sequence ops

String Operations
=================

See :external+python:ref:`string-methods`.

.. admonition:: Important to Remember
    :class: important

    * ``join``
    * ``lower``
    * ``upper``
    * ``split``
    * ``strip``

Common Sequence Operations
==========================

See `Common Sequence Operations <https://docs.python.org/3.9/library/stdtypes.html#common-sequence-operations>`__.

.. admonition:: Important to Remember
    :class: important

    * Containment tests
    * Concatenation
    * Indexing and slicing

Mutable Sequence Operations
===========================

See `Mutable Sequence Operations <https://docs.python.org/3.9/library/stdtypes.html#mutable-sequence-types>`__.

.. admonition:: Important to Remember
    :class: important

    * ``append``
    * ``insert``
    * ``pop``
    * ``remove``

.. end sequence ops
.. start set ops

Set Operations
==============

See `Set Types <https://docs.python.org/3.9/library/stdtypes.html#set-types-set-frozenset>`__.

.. admonition:: Important to Remember
    :class: important

    * ``add``
    * ``remove``
    * ``union``, ``intersection``, ``difference``, and ``symmetric_difference``
    * ``issubset`` and ``issuperset``

.. end set ops
.. start dict ops

Dictionary Operations
=====================

See `Mapping Types <https://docs.python.org/3.9/library/stdtypes.html#mapping-types-dict>`__.

.. admonition:: Important to Remember
    :class: important

    * ``keys``
    * ``values``
    * ``items``
    * ``get``

.. end dict ops

Class-Related Functions
=======================

.. start class-related

``type(x)`` and ``x.__class__``
-------------------------------

If you want a reference to an object's class, you can either use :external+python:py:class:`type`
or ``x.__class__``:

.. code-block:: python

    class A:
        pass

    instance = A()
    print(type(instance) == A)  # True
    print(type(instance) is A)  # True
    print(instance.__class__ == A)  # True
    print(instance.__class__ is A)  # True

Note how in the example above, class comparisons can be performed with ``==`` and ``is``.

``isinstance``
--------------

Because Python is dynamically typed, you might not know what type of object your variable
represents. Or you might have a function that accepts multiple types of inputs, but should
behave slightly differently for each type of input.

You can use the :external+python:py:func:`isinstance` function to check to see if your
variable is an instance of a given class (or one of multiple classes). An instance
of a subclass is also considered to be an instance of the superclass.

.. code-block:: python

    class A:
        pass
    class B(A):
        pass

    var1 = A()
    var2 = B()

    print(isinstance(var1, A))  # True
    print(isinstance(var2, A))  # True
    print(isinstance(var1, B))  # False
    print(isinstance(var2, B))  # True
    print(isinstance(var1, (int, A)))  # True because var1 is an instance of either int or A

.. note::

    ``isinstance(x, object)`` is always true, regardless of what ``x`` is.

.. autofunction:: builtins::isinstance
    :no-index:

``issubclass``
--------------

If you want to see if a class inherits from another, you can use
:external+python:py:func:`issubclass`.

.. code-block:: python

    class A:
        pass
    class B(A):
        pass

    var = B()

    print(issubclass(B, A))  # True
    print(issubclass(type(var), A))  # True

.. autofunction:: builtins::issubclass
    :no-index:

.. note::

    A class is considered to be a subclass of itself.

.. end class-related
