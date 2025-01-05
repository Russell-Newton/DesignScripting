===========
Expressions
===========

*Expressions* are pieces of code that return some sort of value. These are often single
values like :ref:`literals` or :ref:`variables`\ , but can also be made by combining
expressions with operations.

Literals
========

In Python, *literals* allow you to specify a value by writing it out directly. Basically,
what you see is what you'll get. A handful of different types of literals are available
in Python:

Numeric Literals
----------------

Numbers can take the form of integers and floating point numbers.

An integer is any number that does not contain any fractional/decimal component. Some
example integer literals:

.. code-block:: python

    1
    30
    -20
    1000000

Floating point numbers, on the other hand, are numbers that do contain a fractional part.
Basically any real number. Floating point literals are created either by using a decimal
point or by using "`E notation <https://en.wikipedia.org/wiki/Scientific_notation#E_notation>`__"
(e.g.: :math:`3 \times 10^2` can be rewritten as ``3e2`` in code). Some example floating
point literals:

.. code-block:: python

    20.25
    13.  # Placing the decimal point converts it to a floating point number
    3e2
    1.9e-4

String Literals
---------------

Strings represent text in Python. Strings can be written by putting whatever text you'd like
within quotation marks (single ``'`` or double ``"``, as long as you're consistent).
There are a couple of exceptions:

#. String literals cannot contain a line break (i.e.: the literal must be wholly contained
   in one line).
#. The backslash character, ``\``, is used to precede an :ref:`escape sequence <escape-sequence-summary>`. More on these
   later.

Some example string literals:

.. code-block:: python

    "Hello, World!"
    'apple'

.. _escape-sequence-summary:

.. note::
    In this class, we'll be working less with strings and more with data representing
    numbers, vectors, and geometry. Strings can be convenient during debugging though,
    and learning to work with strings is a good way to learn to work with more complex
    data structures.

Escape Sequences
^^^^^^^^^^^^^^^^

Escape sequences are made with a backslash (``\``), followed by a character(s). Some common
escape sequences that you might want are shown in the table:

=============== ========================================
Escape Sequence Meaning
=============== ========================================
``\n``          Line break
``\t``          Horizontal tab
``\uxxxx``      Unicode character with hex value *xxxx*
``\\``          Backslash
``\'``          Single quote (``'``)
``\"``          Double quote (``"``)
=============== ========================================

Multiline Strings
^^^^^^^^^^^^^^^^^

Multiline strings can be created by wrapping your text in three quotation marks (single or double)
on either side. Line breaks are preserved in multiline strings. You can also use unescaped
single and double quotes inside multiline strings because they're terminated with a set of
three. An example multiline string literal:

.. code-block:: python

    """This is my multiline string.
    It preserves line breaks like the one above and the two below.

    I can use "quotation" marks without any problem. I end the string by using three:"""

It's worth noting that any leading or trailing line breaks are preserved, which is why
the ``"""`` are on the first and last lines of the text.

.. dropdown:: Advanced: Formatted Strings
    :color: warning
    :name: f-strings

    Creating strings in Python with concatenation can become somewhat tedious if you want
    to include the results of multiple expressions in them. Using formatted strings
    can make this a lot easier.

    The easiest way to create a formatted string is with an *f-string* literal. To do
    this, precede the first quotation mark with an ``f``, with no space in between. Now,
    whenever you'd like to include an expression, put it directly into the string,
    surrounded by braces (``{...}``). For example:

    .. code-block:: python

        print("1e6 becomes the number " + 1e6)
        # Console Output:
        # 1e6 becomes the number 1000000.0
        print(f"1e6 becomes the number {1e6}")

    In an f-string, if you want to have a brace, you need to escape it, similar to a
    backslash. To escape a brace, repeat it twice (``{{`` becomes ``{`` in the string
    content, and ``}}`` becomes ``}``).

    There are a lot more modifiers you can apply to format the expression results. You
    can learn more `here <https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals>`__.
    Later on that page, you can also learn more about other approaches to creating
    formatted strings.

Boolean Literals
----------------

When programming, you'll often want some way to identify something as being true or not.
If you want an expression that will always be true or false, you can use a Boolean literal.

In Python, the Boolean literals are ``True`` and ``False``.

Booleans have their own special operations: NOT, AND, and OR. NOT flips the truth value
of a Boolean expression (NOT ``True`` becomes ``False`` and vice versa). AND yields
``True`` if and only if all compared expressions are ``True``. OR yields ``True`` if
and only if at least one of the compared expressions is ``True``.

None
----

``None`` is a special keyword in Python that signifies the absense of something. It's not
the same as ``False``\ ; it is instead it's own thing. We'll come back to it's usages
later.

Operations
==========

Operations allow you to combine and modify the results of one or two expressions.
An operator is called *unary* if it only operates on a single expression, and *binary*
if it operates on two.

Unary Operators
---------------

========= =================
Operation Description
========= =================
``-x``    Negative of ``x``
``not x`` Boolean NOT
========= =================

Binary Operators
----------------

============== =============================================================
Operation      Description
============== =============================================================
``a + b``      Sum of ``a`` and ``b``
``a - b``      Difference of ``a`` and ``b``
``a * b``      Product of ``a`` and ``b``
``a / b``      Quotient of ``a`` and ``b`` (floating point)
``a // b``     Quotient of ``a`` and ``b`` (floored to an integer)
``a % b``      ``a`` mod ``b`` (remainder of ``a / b``)
``a ** b``     ``a`` raised to the power of ``b``
``a and b``    Boolean AND
``a or b``     Boolean OR
``a < b``      Yields ``True`` if ``a`` is less than ``b``
``a <= b``     Yields ``True`` if ``a`` is at most ``b``
``a == b``     Yields ``True`` if ``a`` is equal to ``b``
``a >= b``     Yields ``True`` if ``a`` is at least ``b``
``a > b``      Yields ``True`` if ``a``1 is greater than ``b``
``a != b``     Yields ``True`` if ``a`` is not equal to ``b``
============== =============================================================

Some operators may be defined on some types of data while not on others. For example,
subtracting two strings is not supported in Python, but adding two strings concatenates
them. Further, different types of data may be used for both ``a`` and ``b``. Adding a number
to a string concatenates that number to the string, and multiplying a string by an integer
repeats the string that many times. Comparing strings with ``<``, for example, shows if the
first string would come before the second in alphabetical order.

For this class, we won't be using operator behavior that isn't too self explanatory.

Operator Precedence
-------------------

Like PEMDAS, operator order matters. Operators are applied in the following order:

#. Parentheses (``(expressions...)``)
#. Exponentiation (``**``)
#. Negative (``-x``)
#. Multiplication, division, floor division, remainder (``*``, ``/``, ``//``, ``%``)
#. Addition and subtraction (``+``, ``-``)
#. Comparisons (``<``, ``<=``, ``==``, ``>=``, ``>``, ``!=``)
#. Boolean NOT (``not x``)
#. Boolean AND (``a and b``)
#. Boolean OR (``a or b``)

Variables
=========

*Variables* are named identifiers that correspond to some data in memory. The value of
a variable can be set to the value of any expression, including other variables, the results
of operations, and literals. Variables serve multiple purposes:

* Use a named constant instead of repeating a literal (e.g.: ``PI = 3.14159``)
* Refer to the result of an operation so that you don't have to repeat it in your code
* Refer to some value that could be changing (e.g.: ``x = x + 1``)
* Have named inputs and outputs to your script (incredibly important within Grasshopper)

The value of a variable is set using an :ref:`assignment statement <assignment>`.

Variable Names
--------------

Variable names can be *almost* anything you want. Some requirements and guidelines are
listed below:

* Variable names can only contain numbers, letters, and underscores. No spaces or symbols allowed.
* Variable names CANNOT be reserved words (like ``True``, ``if``, ``None``, etc.).
* Variable names CANNOT start with a number.
* Variable names are case-sensitive (``myVar`` is not the same as ``MyVar``).
* Conventionally, variable names in Python are lowercase, with words separated by underscores.

  * Other programming languages have different conventions.
  * Constants may sometimes be all uppercase, with words separated by underscores.

.. note::

    When working with Python in Grasshopper and Rhino 8, it's not uncommon to need to
    work with variables that are camelCased, where the first letter of each word is
    capitalized (excluding the first), instead of using underscores. This is a result
    of the Rhino/Grasshopper-specific variables being created by C# instead of Python.
