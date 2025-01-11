=================
Helpful Functions
=================

This page contains a collection of functions that you might find useful during this
course.

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
function. The stringified arguments will then be sent to the output stream, separated
by the ``sep`` argument, which is keyword-only. In the case of a Grasshopper script node,
the default output stream is captured into the ``out`` pin.

``len``
-------

The :external+python:py:func:`len` function returns the size of a collection, or any
object that has defined the ``__len__`` method.

.. autofunction:: builtins::len
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

.. autoclass:: builtins::range
    :no-index:

.. end funcs

Common Sequence Operations
--------------------------

See `Common Sequence Operations <https://docs.python.org/3.9/library/stdtypes.html#common-sequence-operations>`__.

Mutable Sequence Operations
---------------------------

See `Mutable Sequence Operations <https://docs.python.org/3.9/library/stdtypes.html#mutable-sequence-types>`__.

String Operations
-----------------

See :external+python:ref:`string-methods`.

Set Operations
--------------

See `Set Types <https://docs.python.org/3.9/library/stdtypes.html#set-types-set-frozenset>`__.

Dictionary Operations
---------------------

See `Mapping Types <https://docs.python.org/3.9/library/stdtypes.html#mapping-types-dict>`__.
