===========
Collections
===========

A *collection* is a container datatype that holds multiple pieces of data. We'll learn
about a couple of different types of collections in this course and how you might use
each of them. But first, we'll learn about some common features of all of the containers
that we'll use.

Literals
========

All of the collections we'll learn about here can be written with literals.

The ``in`` operator
===================

Every collection we'll use supports the ``in`` operator. This lets you check if a piece
of data is present within the collection. Specifically:

.. code-block:: python

    x in my_collection

will yield ``True`` if the value of ``x`` is contained within ``my_collection``.

If, instead, you wanted to check if a piece of data **isn't** present within the collection,
you can use ``not in``:

.. code-block:: python

    x not in my_collection

which yields ``True`` if the value of ``x`` **is not** present in the collection. This
is equivalent to:

.. code-block:: python

    not (x in my_collection)

But it's generally better to just use ``not in`` because it's easier to read, and the
code can execute faster in some cases.

For each collection covered, we'll have to explain exactly what the truth value of the
``in`` operator actually means.

Indexing
========

Unless otherwise stated, all collections we'll see can be *indexed*. This means you can
get the item at a specific location. For each collection covered, we'll have to
explain what types of indices are supported.

In order to index a collection, you follow the literal or variable with ``[index]``,
where ``index`` is the index to use when accessing the collection.

.. code-block:: python

    my_item = my_collection[some_index]

Mutability
----------

Some collections are *mutable*, while others are *immutable*. If a collection is mutable,
then the values it contains can be changed at any time. To change a value at a specific
index, you can use an assignment statement with the indexed collection on the LHS:

.. code-block:: python

    my_collection[some_index] = new_value

If a collection is immutable, attempting to modify it after it gets created will result
in an error.

Iteration
=========

:bdg-warning-line:`Important!!!`

All of the collections we'll use can be iterated upon. This means you can execute some
sort of code for every piece of data contained in the collection. Any sort of
specifics will be covered on the respective page.

In order to iterate over a collection, you'll want to use a ``for`` loop:

.. code-block:: python

    for item in my_collection:
        ...  # do something with item

Each iteration of a ``for`` loop sets the loop variable (``item`` in the example above``)
to the next value in the collection. Like a ``while`` loop, a ``for`` loop supports the
use of ``break``, ``continue``, and ``pass``.

Unpacking
---------

Collections can be *unpacked* so that you can name each item in the collection, if
you know how many items are in said collection. If, for example, you have a collection
that, when iterated upon, provides three values, you can save those three values as
follows:

.. code-block:: python

    value1, value2, value3 = my_collection

This is particularly useful when using data structures that contain nested collections,
so that you can unpack the inner collections during iteration. If, for example, you
have a collection of 3-value collections, you could iterate over it like:

.. code-block:: python

    for value1, value2, value3 in my_collection:
        ...

.. important::

    You can nest unpacking, if one of the items in your collection is always a collection
    of constant size:

    .. code-block:: python

        # Here, collection contains 2-tuples
        # The enumerate function creates a new collection of 2-tuples, where the first
        #  item is the integer index of the second item. Because the second item is a
        #  2-tuple, it can be further unpacked.
        for idx, (item1, item2) in enumerate(collection):
            ...

If you only want some of the values, you can use a ``*_`` to capture all remaining
items in the collection. So if your collection contains 5 items but you only want the
first two, you can do:

.. code-block:: python

    value1, value2, *_ = my_collection.

.. note::

    Technically, this creates a variable named ``_``, which points to a list
    containing all of the remaining values. Using an underscore as the name of the
    variable is just a common practice to let a reader know you're ignoring that value.

Usage with ``*args``
--------------------

If you want to pass the contents of a collection into a function's ``*args`` instead
of passing the collection itself into ``*args``, you can do the following:

.. code-block:: python

    my_function(*my_collection)

If, for example, iteration over ``my_collection`` provides the values ``1``, ``2``, and
``3``, this is equivalent to

.. code-block:: python

    my_function(1, 2, 3)

.. admonition:: Remember!
    :class: note

    Using ``*args`` in the parameter list of a function creates a local
    variable ``args`` that is a list containing all additional positional inputs.

Types of Collections
====================

Now, we'll cover the different types of collections that we'll see in this course.

.. toctree::
    :titlesonly:
    :glob:

    *
