====
Sets
====

*Sets* are unordered collections that do not contain duplicates.

.. warning::

    Sets cannot be indexed!

Making a Set
============

Sets can be constructed with a set literal:

.. code-block:: python

    my_set = {1, 2, 3}

or by using the :external+python:py:class:`set` constructor:

.. code-block:: python

    empty_set = set()
    my_set = set(my_collection)

Note that any duplicates contained in ``my_collection`` or the set literal will be
ignored.

.. important::

    Only *hashable* data can be contained in a set. The specifics are beyond the scope
    of this course, but it basically means that only *immutable* data can be contained
    within a set. For example, a tuple can be added to a set, but a list cannot. A tuple
    containing a list cannot, because that list itself could be mutated.

    Attempting to add unhashable data to a set will result in an error.

``frozenset``
-------------

Sets created with a set literal or with the :external+python:py:class:`set` constructor
are mutable, which means they cannot be used as elements within a set. The
:external+python:py:class:`frozenset` constructor can be used to create an immutable
set, which *can* be contained within another set.

Iterating Over a Set
====================

:bdg-warning-line:`Important!!!`

When iterating over a set, you're not guaranteed anything about iteration order.

Set Comprehension
=================

Like lists, you can construct sets by wrapping a generator expression inside of braces:

.. code-block:: python

    my_set = {some_operation(x) for x in another_collection}

This is equivalent to:

.. code-block:: python

    my_set = set()
    for x in another_collection:
        my_set.add(some_operation(x))

.. include:: ../../resources/helpful-functions.rst
    :start-after: .. start set ops
    :end-before: .. end set ops
