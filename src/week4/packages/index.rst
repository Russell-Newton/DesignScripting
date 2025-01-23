==========================
Using Modules and Packages
==========================

Only a handful of identifiers are available in the global scope of your program. These
include the built-in functions and classes discussed during weeks 1 and 2. There are
a lot more tools at your disposal when using Python, however. These tools are organized
into *modules* and *packages*. A module is basically any Python file that contains
definitions that can be used within another file. A package is a collection of modules
and subpackages. Oftentimes, a top-level pacakge or module is referred to as a *library*.

.. note::

    We won't be making any modules or packages in this class, but if you're interested
    in how to do it, you can find more information in the `Python docs <https://docs.python.org/3.9/tutorial/modules.html>`__.

Importing a Module
==================

To gain access to the definitions in a module, use an *import* statement:

.. code-block:: python

    import my_module

To use one of the definitions in a module, use "dot notation" as if you're accessing
a member of a class:

.. code-block:: python

    my_module.some_function()
    # or
    my_module.some_variable

If your module is contained within a package, use "dot notation" in the import statement:

.. code-block:: python

    import my_package.my_module
    # Note that "my_package" could be nested in another package, which would require
    #  additional dot notation:
    # import package1.package2.my_module

One downside of importing a module from a package like this is that you need to include
the package identifier when accessing module contents:

.. code-block:: python

    my_package.my_module.some_function()
    # or
    my_package.my_module.some_variable

You have two options to make a shorthand for this:

.. code-block:: python

    import my_package.my_module as my_module
    # or
    from my_package import my_module

The first option, using ``as`` after an import statement, allows you to rename whatever
you're importing. Where it would normally be ``my_package.my_module``, it is instead just
``my_module``. The second option, using ``from`` before an import statement, allows you
to specify the package or module you want to peek into when importing, so you don't have
to specify it again.

.. important::

    Using a ``from`` import allows you to import a module from a package without needing
    the dot notation to access the module, but you can also do this to access members
    from a module too:

    .. code-block:: python

        from my_package.my_module import some_function

.. important::

    You can rename any imported name using ``as``:

    .. code-block:: python

        from my_package.my_module import some_function as something_else

Importing Multiple Things
-------------------------

You can import multiple modules from one pacakge or multiple members from one module
by separating what you're importing with commas:

.. code-block:: python

    from my_package.my_module import some_function, some_variable

You can also throw in an ``as``, if you'd like.

If you want to import all members of a module, you can instead import ``*``:

.. code-block:: python

    from my_package.my_module import *

    some_function()  # can be called
    some_variable  # can be accessed

.. warning::

    In general, it's frowned upon to use this because it floods the namespace in your
    current file, but it can be very helpful when working with Rhino-related packages
    and modules so you don't have to write a bunch of import statements.

Important Libraries
===================

The following pages discuss some important packages that you should be at least loosely
familiar with during this course. There are many more packages than this built into Python,
and you can add more packages from online sources, but these are the most important ones
we'll start seeing all over.

.. toctree::
    :titlesonly:
    :glob:

    *
