==========
Whitespace
==========

In Python, whitespace matters a lot. Line breaks are used to separate statements,
and indentation is used to indicate which code belongs to which control statement.

Conventionally, lines of code under a control statement will be indented either by
2 or 4 spaces. Most code editors will insert spaces instead of a tab character when you
press your TAB key. This includes the script editor in Rhino 8.

.. warning::
    DO NOT try to mix and match indentations. Within an indented block, all statements
    should be indented by the same amount.

    Additionally, if your program uses spaces to indent in one place and tabs in another,
    it will not execute.

There are three exceptions to the rule that line breaks separate statements:

#. If a line ends with a backslash (``\``), the next line continues the statement. All
   of the following are equivalent:

   .. code-block:: python

        x = 1 + 2
        x = 1 + \
            2
        x = 1 \
            + 2

#. An expression contained within parentheses can be extended with line breaks. The
   following are all equivalent:

   .. code-block:: python

        if x + 1 == 2:
            ...

        if (x
            + 1) == 2:
            ...

        if (
            x
            + 1
            == 2
        ):
            ...

#. Statements on the same line can be separated with a semicolon (``;``):

   .. code-block:: python

        x = 1; y = 2

.. note::
    Note how in the first two exceptions, the continuations are indented. This is
    not necessary, but it makes the code easier to read, and is good practice.

Variable Scope
==============

*Variable scope* defines where a variable can be used. A variable's scope is determined
when it gets defined for the first time. Within that scope, the variable can be used
and redefined as many times as you'd like. A variable can either be scoped at a global
or at a function level.

.. topic:: A note about control statements

    Control statements like ``if``, ``while``, and ``for`` do not create a new scope.
    Any variable created inside the statement body can be used after exiting the body.
    The one limitation is that if the variable is never defined because the body never
    runs, it cannot be used. Attempting to use a variable that hasn't been defined
    will result in a :external+python:py:class:`NameError` being raised.

Global Variables
----------------

Global variables are defined outside of any function or class body. These tend to be at
no indentation and can include file-level constants, functions, imports, and class
definitions. Any identifiers created inside of a top-level control statement is also
a global variable, assuming the statement body was run.

Local Variables
---------------

Local variables are defined inside of a function or class body. They can only be used
within that function or class. Global variables *can* be used within a function, but
some care has to be taken if you wish to redefine a global variable within a function:

``global``
^^^^^^^^^^

When a function needs to be able to redefine a global variable, it must be told that
that variable is the global one, and not a new local variable to be defined. For example:

.. code-block:: python

    x = 10
    def my_function():
        x = 3  # This creates a new local variable called x within my_function
        print(x)
    my_function()
    print(x)

    # Console Output:
    # 3
    # 10

In order to indicate that you want to redefine a global variable instead of creating
a local variable, use ``global variable_name`` before redefining the variable:

.. code-block:: python

    x = 10
    def my_function():
        global x
        x = 3
        print(x)
    my_function()
    print(x)

    # Console Output:
    # 3
    # 3

``nonlocal``
^^^^^^^^^^^^

Functions can be nested inside other functions, which means that similar to global
variables, a nested function could need to redefine a variable within the outer
function. In order to specify that you want to redefine an outer-scope local variable
instead of defining a new local variable, use ``nonlocal variable_name``:

.. code-block:: python

    def my_function():
        x = 10
        def inner_function():
            nonlocal x
            x = 3
            print(x)
        inner_function()
        print(x)
    my_function()

    # Console Output:
    # 3
    # 3

Without the use of ``nonlocal``, the second ``print`` call in the output above would
print ``10`` to the console.

.. important::

    The use of ``global`` and ``nonlocal`` as in the examples above is needed, but it
    highlights one common source of bugs: variable name clashes. If at all possible,
    it's a good idea to avoid reusing variable names within the same scope.
