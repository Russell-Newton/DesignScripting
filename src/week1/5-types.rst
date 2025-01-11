=============
Types, Part 1
=============

Everything in Python has a *type*. The type of a variable, for instance, lets
your program know how it operates. An ``int`` behaves differently from a ``float``,
which both behave differently from a ``str``.

For right now, we'll cover some useful information about types that you'll likely want
to know for the first week or two. During week 2, we'll go more into detail.

Python is Dynamically-Typed
===========================

Python is a *dynamically-typed* language, which basically means a variable could refer
to an object of any type. The exact type it is is determined at runtime. For example,
a variable ``x`` might start as an integer, but could be a string later in the same
function. This can be very convenient because you don't have to be explicit about what
your variables actually represent (easier to write), but it can get confusing if, for
example, you don't know what types of variables you can provide to a function. To
alleviate some of this, Python supports *type hints*.

Type Hints
==========

Type hints in Python provide type information to a programmer. They can be provided
on variable definitions (including function parameter lists) and on a function to
declare its output type. Because Python is dynamically typed, these are not strict,
and it's up to the programmer to ensure that type hints are respected.

.. tip::
    Most modern development environments will provide warnings if type hints aren't
    respected. Some complicated types may still fall between the cracks though.

A type hint on a variable declaration looks like:

.. code-block:: python

    # The ": int" tells us that x is an integer
    x: int = 10

A type hint on a function declaration looks like:

.. code-block:: python

    # Here, like with a variable, we can specify input parameter types like
    #       identifier: type
    # To specify a function's output type, we do
    #       -> type
    #   following the closing parenthesis, before the colon
    def my_function(text: str) -> int:
        ...

    # Now, our development environment would warn us that the following line
    #   doesn't respect type hints
    x: float = my_function(2)
    # Not only does the type of x not match the return type of my_function, but the
    #   inputted value of 2 isn't a string like expected

.. important::
    During this course, I will try to ensure that any assignments will have explicitly
    typed inputs and outputs, so that you know what to expect.

Basic Types
===========

The following lists are copied from the :doc:`dedicated page on type hints <../resources/type-hints>`.

.. include:: ../resources/type-hints.rst
    :start-after: .. start basic
    :end-before: .. end basic
