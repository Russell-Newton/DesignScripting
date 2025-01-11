============
Dictionaries
============

*Dictionaries* are unordered collections that represent mappings from *keys* to *values*.
Dictionaries are indexed by their keys. Indexing a dictionary with a certain key returns
the value stored at that key (or raises an error if that key isn't present in the dictionary).
**Dictionary keys are unique!**

.. important::

    Only *hashable* data can be used as dictionary keys. The specifics are beyond the scope
    of this course, but it basically means that only *immutable* data can be keys.
    For example, a tuple can be a key, but a list cannot. A tuple containing a list
    cannot, because that list itself could be mutated.

    Attempting to use unhashable data as a key will result in an error.

Making a Dictionary
===================

Sets can be constructed with a dictionary literal:

.. code-block:: python

    my_set = {key1: value1, key2: value2, key3: value3}

Note that using empty braces (``{}``) creates an empty dictionary, not an empty set.

The :external+python:py:class:`dict` Constructor
------------------------------------------------

Dictionaries can also be created using the :external+python:py:class:`dict` constructor.
To use this, you can pass either no arguments, another dictionary, or an iterable
collection where each item is an iterable with two items representing ``(key, value)``
pairs. With each of these options, you can also provide additional keyword arguments:

.. code-block:: python

    my_dict1 = dict()
    my_dict2 = dict(key1=value1, key2=value2)
    my_dict3 = dict(my_dict2)
    my_dict4 = dict([(key1, value1), (key2, value2)])

Dictionary Operations
=====================

See `Mapping Types <https://docs.python.org/3.9/library/stdtypes.html#mapping-types-dict>`__.

Iterating Over a Dictionary
===========================

:bdg-warning-line:`Important!!!`

When iterating over a dictionary with a ``for`` loop, the loop variable will always
be a key in the dictionary. The iteration order is determined by the order in which
key-value pairs were inserted into the dictionary.

If you want to iterate over a dictionary's values, you can do:

.. code-block:: python

    for value in dict.values():
        ...

If you want to iterate over the key-value pairs within a dictionary, you can instead do:

.. code-block:: python

    for key, value in dict.items():
        ...

Dictionary Comprehension
========================

Like lists and sets, dictionaries can be constructed using comprehension. Unlike lists
and sets, however, dictionary comprehension looks like:

.. code-block:: python

    my_dict = {key: value for ...}

Usage with ``**kwargs``
=======================

If you want to pass the contents of a dictionary into a function's ``**kwargs``,
you can do the following:

.. code-block:: python

    my_function(**my_dict)

If ``my_dict`` contains key-value pairs ``key1: value1`` and ``key2: value2``, this
is equivalent to:

.. code-block:: python

    my_function(key1=value1, key2=value2)

.. admonition:: Remember!
    :class: note

    Using ``**kwargs`` in the parameter list of a function creates a local
    variable ``kwargs`` that is a dictionary containing all additional positional
    inputs.
