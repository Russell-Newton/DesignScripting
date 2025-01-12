=========
Sequences
=========

*Sequences* are collections that contain data in a specific order. This means that for
a sequence, it makes sense to talk about the "nth" item. Iterating over sequences
occurs in order from the first element to the last.

Indexing Sequences
==================

Sequences are index with integers. Importantly, sequence indices start at 0, where
``sequence[0]`` gets the first item in the sequence. This can be a bit confusing at
first, but it could help to think of the index as how many places *after* the first
item you want to grab from. So to get the fourth item, you would do ``sequence[3]``
because the fourth item is 3 places after the first.

.. important::

    | If the length of a sequence is ``n``, trying to get ``sequence[n]`` will result
      in an error.
    | The last item in the sequence is ``sequence[n - 1]``.

Negative Indices
----------------

Sequences support negative indices, where ``sequence[-1]`` is the last item,
``sequence[-2]`` is the second to last item, and so on.

Reversing a Sequence
--------------------

Sequences can be reversed with the :external+python:py:func:`reversed` function.

.. warning::

    :external+python:py:func:`reversed` does not return a sequence. It returns something
    that can be iterated over with a ``for`` loop, but it cannot be indexed. If you need
    a reversed version of your sequence that *can* be indexed, use a slice, as shown in
    the :ref:`slicing-examples`.

Slicing
-------

Slicing is an important concept for sequences. A *slice* is a special data type that
can be used as the index of a sequence. Instead of getting a single element using an
integer index, using a *slice* as the index will retrieve a subsequence of the original
sequence.

.. important::

    The subsequence created with a slice index will always be the same type as the
    original sequence

To construct a slice, you can use the following syntax within the square brackets when
indexing a sequence:

.. code-block:: python

    my_subsequence = my_sequence[start_inclusive:end_exclusive:step]

Some notes:

* The returned subsequence is basically defined as:

  .. code-block:: python

      i = 0
      while start_inclusive + i < end_exclusive:
          my_sequence[start_inclusive + i]  # added to subsequence

          i += step

* All three parameters in the slice can be any int-valued expression you want.
* All three parameters can be negative. If ``step`` is negative, the returned subsequence
  is defined differently:

  .. code-block:: python

      i = 0
      while start_inclusive - i > end_exclusive:
          my_sequence[start_inclusive - i]  # added to subsequence

          i -= step

  Note that here, if ``start_inclusive < end_exclusive``, the returned subsequence
  will be empty.

The slice sequence can be simplified in the following ways:

* If ``start_inclusive = 0``, it can be dropped:

  .. code-block:: python

      my_subsequence = my_sequence[:end_exclusive:step]

  This gives you the subsequence from the start of the sequence to ``end_exclusive``,
  using ``step``. If ``step`` is negative, dropping ``start_inclusive`` has the effect
  of setting ``start_inclusive = len(my_sequence) - 1``.

* If ``end_exclusive = len(my_sequence)``, it can be dropped:

  .. code-block:: python

      my_subsequence = my_sequence[start_inclusive::step]

  This gives you the subsequence from ``start_inclusive`` to the end of the sequence,
  using ``step``. If ``step`` is negative, dropping ``end_exclusive`` has the effect
  of setting ``end_inclusive = 0``. Note here that the end is inclusive because setting
  ``end_exclusive = -1`` sets ``end_exclusive = len(my_sequence) - 1``.

* If ``step = 1``, ``:step`` can be dropped all together:

  .. code-block:: python

      my_subsequence = my_sequence[start_inclusive:end_exclusive]

  This gives you the subsequence from ``start_inclusive`` to ``end_exclusive``.

.. dropdown:: Slicing Examples
    :color: warning
    :name: slicing-examples

    To get every other item in the sequence, starting from the first:

    .. code-block:: python

        my_sequence[::2]

    To reverse the sequence with a slice:

    .. code-block:: python

        my_sequence[::-1]

    To get the subsequence from index ``a`` to ``b``:

    .. code-block:: python

        my_sequence[a:b]

    To get the subsequence up to ``b``:

    .. code-block:: python

        my_sequence[:b]

    To get the subsequence starting at ``a``:

    .. code-block:: python

        my_sequence[a:]

Types of Sequences
==================

Strings
-------

Strings are *immutable* sequences of characters. Indexing a string returns a
single-character string, and slicing a string returns a substring. A full specification
of methods usable on strings can be found in Python's documentation
:external+python:ref:`here <string-methods>`. Generally, if you want to do
something with a string in Python, Google, StackOverflow, and ChatGPT will probably
have the answers for you.

Tuples
------

Tuples are *immutable* sequences of any data you'd like. Tuples can be constructed
with a tuple literal:

.. code-block:: python

    my_tuple = (1, 2, 3)

or by converting another collection to a tuple with the :external+python:py:class:`tuple`
constructor:

.. code-block:: python

    my_tuple = tuple(my_collection)
    # The order in which the elements are placed in the tuple is the same as how
    # my_collection would get iterated upon in a ``for`` loop.

.. note::

    The parenthesis in a tuple literal can be avoided when used in the RHS of an assignment
    statement or as the return value in a return statement:

    .. code-block:: python

        my_tuple = 1, 2, 3

.. important::

    If you want to create a 1-tuple, you must include a comma following the single
    item.

    .. code-block:: python

        my_tuple = (1,)  # This is a tuple
        my_int = 1  # This is an int

    If you want to create a 0-tuple, you must use the tuple constructor:

    .. code-block:: python

        empty_tuple = tuple()

Lists
-----

Lists are *mutable* sequences of any data you'd like. Lists can be constructed with
a list literal:

.. code-block:: python

    empty_list = []
    my_list = [1, 2, 3]

or by converting another collection to a list with the :external+python:py:class:`list`
constructor:

.. code-block:: python

    my_list = list(my_collection)
    # Like with tuples, the order of elements is the same as how my_collection would
    # get iterated upon in a ``for`` loop.

List Comprehension
^^^^^^^^^^^^^^^^^^

Lists can also be constructed by putting a *generator expression* between two brackets:

.. code-block:: python

    my_list = [some_operation(x) for x in another_collection]

This is equivalent to:

.. code-block:: python

    my_list = []
    for x in another_collection:
        my_list.append(some_operation(x))

but using the list comprehension is faster to write and can be easier to read. You can
even nest list comprehensions:

.. code-block:: python

    my_list = [some_operation(x) for x in [other_operation(y) for y in another_collection]]

.. note::

    There's no such thing as tuple comprehension. If you wanted to do something similar,
    you can write the generator expression inside of the call to the
    :external+python:py:class:`tuple` constructor:

    .. code-block:: python

        my_tuple = tuple(some_operation(x) for x in another_collection)

Ranges
------

Ranges are *immutable* sequences of integers, ranging from some start value (inclusive) to an end
value (exclusive), using an optional step value to set the common difference within the sequence.
Ranges are constructed with the :external+python:py:class:`range` constructor, and are
most often used within a ``for`` loop:

.. code-block:: python

    for i in range(start_inclusive, end_exclusive, step):
        ...

The constructor can take either 1, 2, or 3 inputs. If one input is given, it is
interpreted as ``end_exclusive``, and ``start_inclusive = 0`` and ``step = 1``. If
two inputs are given, the first is interpreted as ``start_inclusive``, the second is
``end_exclusive``, and ``step = 1``. With all 3, the third becomes the value used for
``step``.

.. include:: ../../resources/helpful-functions.rst
    :start-after: .. start sequence ops
    :end-before: .. end sequence ops
