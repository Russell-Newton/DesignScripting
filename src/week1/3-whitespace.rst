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

        if (x
            + 1
            == 2:
            ...

#. Statements on the same line can be separated with a semicolon (``;``):

   .. code-block:: python

        x = 1; y = 2

.. note::
    Note how in the first two exceptions, the continuations are indented. This is
    not necessary, but it makes the code easier to read, and is good practice.
