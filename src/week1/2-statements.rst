==========
Statements
==========

*Statements* are the actions for your code to perform. Instead of an expression that
yields a value, statements do not yield any value. Instead, they have some sort of side
effect such as setting the value of a variable, or controlling the flow of the program.

Assignment
==========

To set the value of a variable, you use an assignment statement. This can take one
of a handful of forms:

==================== =============================================================
Assignment           Meaning
==================== =============================================================
``x = expression``   Set the value of ``x`` to the value yielded by ``expression``
``x += expression``  Shorthand for ``x = x + (expression)``
``x -= expression``  Shorthand for ``x = x - (expression)``
``x *= expression``  Shorthand for ``x = x * (expression)``
``x /= expression``  Shorthand for ``x = x / (expression)``
``x //= expression`` Shorthand for ``x = x // (expression)``
``x %= expression``  Shorthand for ``x = x % (expression)``
``x **= expression`` Shorthand for ``x = x ** (expression)``
==================== =============================================================

Control Statements
==================

By default, a Python script gets executed from top to bottom, with each statement getting
executed in order. More often than not, though, you'll want to write code that can choose
between multiple different actions or repeat actions until some condition is met. This
is where control statements come in.

Branching
---------

*Branching* is when a program has to choose to take an action or not, based on some
condition. In Python, this is facilitated with an ``if`` statement. The basic syntax
is:

.. code-block:: python

    if expression:
        ...

Where ``expression`` is some expression that evaluates to ``True`` or ``False``, and
``...`` is the statement *body*: code that the program should execute if ``expression``
evaluates to ``True``. Using variables in ``expression`` can make this behavior dynamic,
making for more complicated programs.

This syntax can be augmented with an ``else`` block:

.. code-block:: python

    if expression:
        ...
    else:
        ...

Here, the code under the ``if`` statement will run only if ``expression`` is ``True``,
and the code under the ``else`` statement will run only if ``expression`` is ``False``.

``if`` statements can be nested together:

.. code-block:: python

    if expression1:
        if expression2:
            ...  # This runs if both expression1 and expression2 are True
        else:
            ...  # This runs if expression1 is True but expression2 is False
    else:
        ...  # This runs if expression1 is False (regardless of expression2's value)

Nesting in an ``else`` block can be avoided with an ``elif`` statement:

.. code-block:: python

    if expression1:
        ...  # This runs if expression1 is True
    elif expression2:
        ...  # This runs if expression1 is False and expression2 is True
    else:
        ...  # This runs if expression1 and expression2 are both False

Looping
-------

Sometimes, you want to repeat a section of code until a condition is met. The easiest
way to do this is with a ``while`` loop:

.. code-block:: python

    while condition:
        ...

As long as ``condition`` evaluates to ``True``, the code in ``...`` will be executed
repeatedly in a loop. ``condition`` is reevaluated before running any of ``...``, so if
the condition isn't met to begin with, it won't run, and if the condition isn't met
when another iteration is about to start, it won't proceed with that iteration and will
instead move on to the code following the ``while`` loop.

Normally, you'd want the code in ``...`` to modify the evaluation
of ``condition`` to make sure the loop doesn't go on forever. For example:

.. code-block:: python

    x = 0
    while x < 10:
        x += 1

will run 10 times. Each iteration of the loop increments ``x`` by one, and after the
10th iteration, when ``x`` is 10, the loop stops because ``x < 10`` is no longer true.

.. note::
    There is another way to loop in Python: the ``for`` loop. We will learn about this
    in the next in-person class, during week 3.

``break``
^^^^^^^^^

Sometimes, you may want to leave a loop early, before the condition is broken. This can
be done with a ``break`` statement:

.. code-block:: python

    x = 0
    while x < 10:
        if x == 5:
            break
        x += 1

In this case, the loop will end once ``x`` is 5, even though ``x < 10`` is still true.
All remaining code in the loop body after ``break`` is called will not be executed.

``continue``
^^^^^^^^^^^^

Other times, you may want to skip the remaining portion of the loop body while still staying
in the loop. This can be done with a ``continue`` statement:

.. code-block:: python

    x = 0
    while x < 10:
        if x == 5:
            x += 2
            continue
        x += 1

Here, without ``continue``, the ``x += 1`` statement would still get executed even
after the ``x += 2`` is executed. By using ``continue``, the remaining content of the loop
body is skipped, and the loop body is execute again from the very start. This code has the
effect of looping until ``x`` is 10, but it will never be the case that ``x`` is 6.

``pass``
^^^^^^^^

Control statements always need at least one line of code in their body. If,
for one reason or another, you don't have any code to put under the control statement,
but you still need it there (for example if you plan on writing the body of an ``if``
statement later), you can use a ``pass`` statement:

.. code-block:: python

    if expression:
        pass
