=================================
Assignment 1: Snap, Crackle, Pop!
=================================

:bdg-danger-line:`Due: Friday, Jan 24, 2025`

.. note::

    This problem is based on FizzBuzz, a children's game, a drinking game, and a basic
    test for programming competence.

Description
===========

In Grasshopper, create a Python3 script node that has two integer inputs
(``start`` and ``end``) and three integer outputs (``num_snap``, ``num_crackle``,
and ``num_pop``). Connect an integer slider to ``start``, and another to ``end``, and
panels to ``out`` and the three ``num_xxx`` outputs.

Inside the script node, write Python code that will :external+python:py:func:`print`
out each number from ``start`` (inclusive) to ``end`` (exclusive). However:

* For numbers that are multiples of 3, instead print "Snap".
* For numbers that are multiples of 5, instead print "Crackle".
* For numbers that are multiples of 7, instead print "Pop".
* For numbers that are multiples of a combination of 3, 5, or 7, instead print
  "SnapCrackle" (3 and 5), "SnapPop" (3 and 7), "CracklePop" (5 and 7), or
  "SnapCracklePop" (3, 5, and 7).

Additionally, define ``num_snap`` to be the number of times that "Snap" appeared in a
print statement, ``num_crackle`` to be the number of times that "Crackle" appeared, and
``num_pop`` to be the number to times that "Pop" appeared.

.. _assignment1-edge-cases:

Edge Cases
----------

* If ``start`` is greater than or equal to ``end``, nothing should print, and the output
  variables should be set to 0.
* If "Snap", "Crackle", or "Pop" are never printed, their corresponding ``num_xxx``
  outputs should be set to 0.
* ``start`` and ``end`` can be negative numbers.

Examples
--------

Inputs: ``start = 97``, ``end = 122``

``out`` panel:

.. code-block:: none
    :linenos:
    :lineno-start: 0

    97
    Pop
    Snap
    Crackle
    101
    Snap
    103
    104
    SnapCracklePop
    106
    107
    Snap
    109
    Crackle
    Snap
    Pop
    113
    Snap
    Crackle
    116
    Snap
    118
    Pop
    SnapCrackle
    121

Outputs: ``num_snap = 8``, ``num_crackle = 5``, ``num_pop = 4``

.. dropdown:: Example 2
    :color: secondary

    Inputs: ``start = 11``, ``end = 15``

    ``out`` panel:

    .. code-block:: none
        :linenos:
        :lineno-start: 0

        11
        Snap
        13
        Pop

    Outputs: ``num_snap = 1``, ``num_crackle = 0``, ``num_pop = 1``

.. dropdown:: Example 3
    :color: secondary

    Inputs: ``start = -40``, ``end = 6``

    ``out`` panel:

    .. code-block:: none
        :linenos:
        :lineno-start: 0

        Crackle
        Snap
        -38
        -37
        Snap
        CracklePop
        -34
        Snap
        -32
        -31
        SnapCrackle
        -29
        Pop
        Snap
        -26
        Crackle
        Snap
        -23
        -22
        SnapPop
        Crackle
        -19
        Snap
        -17
        -16
        SnapCrackle
        Pop
        -13
        Snap
        -11
        Crackle
        Snap
        -8
        Pop
        Snap
        Crackle
        -4
        Snap
        -2
        -1
        SnapCracklePop
        1
        2
        Snap
        4
        Crackle

    Outputs: ``num_snap = 15``, ``num_crackle = 10``, ``num_pop = 6``

.. dropdown:: Example 4
    :color: secondary

    Inputs: ``start = 10``, ``end = 0``

    ``out`` panel is empty.

    Outputs: ``num_snap = 0``, ``num_crackle = 0``, ``num_pop = 0``

.. dropdown:: Example 5
    :color: secondary

    Inputs: ``start = 20``, ``end = 20``

    ``out`` panel is empty.

    Outputs: ``num_snap = 0``, ``num_crackle = 0``, ``num_pop = 0``

Rubric
======

Your grade for this assignment is determined by adding points for each milestone you
complete:

======= ===========================================================================================================================
Points  Requirements
======= ===========================================================================================================================
25      | Create a Python3 Script node with 2 integer inputs and 3 integer outputs (not including ``out``)
        | -2 points for each input/output not marked as integers (up to -10)
15      ``out`` contains a correct printed output
15      ``num_snap`` contains the number of numbers from ``start`` (inclusive) to ``end`` (exclusive) that are divisible by 3
15      ``num_crackle`` contains the number of numbers from ``start`` (inclusive) to ``end`` (exclusive) that are divisible by 5
15      ``num_pop`` contains the number of numbers from ``start`` (inclusive) to ``end`` (exclusive) that are divisible by 7
15      All edge cases (specified :ref:`above <assignment1-edge-cases>`) are accounted for (-5 points for each one missed)

        .. important::

            Missing an edge case **will not** affect your score for prior rubric items.
======= ===========================================================================================================================

Correctness is **very important** in this assignment because of how straightforward the
problem is. Although there is no correct way to program a solution, there is only one
correct solution output. I will try to be as generous as possible with partial credit,
but there's only so much I can do here.
