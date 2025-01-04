=========
Functions
=========

A *function* is an organizational structure that lets you group code into a reusable
package. Not only do functions allow you to reuse the same code (possible with different
inputs) over and over, they can be useful to help organize your code into logically
related fragments, which can make your code easier to develop and understand.

Anatomy of a Function
=====================

A function definition looks like:

.. code-block:: python
    :name: example-function

    def my_function(inputs...):
        ...
        return expression

Let's break it down.

Function Name
-------------

In the :ref:`example above <example-function>`, the function created is called
``my_function``. This has the effect of creating a variable named ``my_function``, who's
value is the function itself. In order to use ``my_function``, you *call* it with the
following syntax:

.. code-block:: python

    my_function(...)

Where ``...`` in this case is the inputs that you pass to your function.

.. note::

    Because a function's name becomes a variable, it is conventional for function
    names to be lowercase, with words separated by underscores. It follows all variable
    name requirements.

    When working with Python in Grasshopper and Rhino 8, it's not uncommon to need to
    work with functions that are PascalCased, where the first letter of each word is
    capitalized (including the first), instead of using underscores. This is a result
    of the Rhino/Grasshopper-specific functions being created by C# instead of Python.

Function Inputs
---------------

The number of inputs a function takes is determined by specifying comma-separated variable
names inside the parentheses immediately following ``def my_function``, ``inputs...``
in the :ref:`example above <example-function>`. A function can accept as many inputs
as you'd like.

When calling the function, you need to pass in one argument for each input declared in
the function definition:

.. code-block:: python

    def function0():
        ...
    # would need to be called like
    return_value = function0()

    def function1(arg1):
        ...
    # would need to be called like
    return_value = function1(True)

    def function2(arg1, arg2):
        ...
    # would need to be called like
    return_value = function2(1, "fizz")

The type of arguments used and the values passed in depend on the function and how it
is being used.

.. dropdown:: Advanced Parameter Shenanigans
    :color: warning
    :name: advanced-parameters

    During this class, you may come across some parameter lists that aren't just
    comma-separated variable names, and you might see some arguments in a function call
    that look like an assignment.

    To understand these, we can look to how Python handles parameters getting passed in.
    When you provide parameters to a function as shown above, they're treated as
    *positional* arguments. That is, the first value you supply when calling the function
    is assigned to the first input parameter, the second to the second, etc. Alternatively,
    you can pass variables *by keyword*, in which you explicitly say which input variable
    to bind to which value. Using the ``function2`` from above:

    .. code-block:: python

        return_value = function2(arg2="fizz", arg1=1)

    .. important::
        All positional arguments must be passed in before all keyword arguments.

        .. code-block:: python

            return_value = function2(arg2="fizz", 1)

        is invalid.

        Furthermore, attempting to pass an argument to a parameter name that doesn't
        exist in the function definition will result in an error.

    Additionally, functions in Python can be *variadic*, which means they can be made to
    accept any number of arguments you supply to them. To do this, create a parameter,
    and have it's name start with an ``*`` (the common choice is ``*args``). When called,
    you can pass in as many comma-separated values as you'd like, and any values in excess
    of the number of positional input parameters in the function definition will fill
    a :external+python:py:class:`list` that gets stored in the ``args`` variable. Keyword arguments can also
    be made to be variadic, starting the variable name with ``**`` (the common choice
    for variable name is ``**kwargs``). Any keyword arguments that do not match an
    explicitly defined input parameter will populate a :external+python:py:class:`dict` that gets stored in
    the ``kwargs`` variable. An example function definition with both variadic positional
    and keyword arguments:

    .. code-block:: python

        def my_function(*args, **kwargs):
            print(args)
            print(kwargs)

        my_function(1, 2, a=3, b=4)
        # Console output:
        # [1, 2]
        # {'a': 3, 'b': 4}

    .. note::
        We will learn about lists and dicts in the next in-person class, during week 3.

    Another trick you can apply to a function definition is to make certain parameters
    either positional-only or keyword-only. Positional-only parameters must be supplied
    positionally (an error will be raised if they are specified by name), and keyword-only
    parameters must be supplied by name.

    By creating a positional-variadic function, any parameters listed after ``*args``
    will be keyword only. If you don't want the function to be positional-variadic but
    still have keyword-only parameters, make a parameter that is simply ``*``. Extra
    positional arguments will raise an error, because there's no variable to save them
    to, but any arguments listed after the ``*`` will be keyword-only. To make
    positional-only arguments, place a ``/`` in the function definition following the
    arguments you want to be positional-only. An example, non-variadic function definition:

    .. code-block:: python

        def my_function(pos_only1, pos_only2, /, either_or1, either_or2, *, kw_only1, kw_only2):
            ...

    Finally, you can supply default values to function parameters. If these parameters
    do not receive a value when the function is called, they are assigned the default
    value provided in the function definition. For example:

    .. code-block:: python

        def my_function(a, b, c=2):
            print(a, b, c)

        my_function(0, 1)
        # Console output:
        # 0 1 2

        my_function(1, 2, 3)
        # Console output:
        # 1 2 3

    .. important::
        All parameters with defaults must be declared at the end of the parameter list.
        This does mean you have to be mindful if you want to have positional-only or
        keyword-only arguments with defaults.

Function Output
---------------

A function in Python will always return some kind of value. This value is determined with
a ``return`` statement. As seen in the :ref:`example above <example-function>`, ``return``
is followed by an expression that sets the output value. Once return is called, the
function is immediately left, and no more code in the function body is executed.

You can have multiple return statements in one function, but only the first one called
will get executed. You can use control statements to make multiple return statements
meaningful:

.. code-block:: python

    def is_odd(number):
        if number % 2 == 0:
            return False
        else:
            return True

.. note::

    The example above is a little contrived, because it can be reduced to:

    .. code-block:: python

        def is_odd(number):
            return number % 2 == 1

    But it gets the point across.

Some special cases for function outputs exist:

* If a ``return`` is *not* followed by an expression, the return value is set to ``None``.
* If a ``return`` statement is never called by the time the end of the function has been
  reached, it will automatically return ``None``.

Useful Functions
================

The following is a collection of helpful functions that you will probably find useful
during this course (copied from the :doc:`dedicated page <../resources/helpful-functions>`).

.. include:: ../resources/helpful-functions.rst
    :start-after: .. start list
    :end-before: .. end list
