=================
Helpful Functions
=================

This page contains a collection of functions that you might find useful during this
course.

.. start list

This is a living list that will expand over the course of the semester.

``print``
---------

The :external+python:py:func:`print` function allows you to output text to the console
while a program is running.

In a Grasshopper script node, instead of printing to the console, any printed text
gets sent to the ``out`` pin, which can be viewed with a Panel.

.. autofunction:: builtins::print
    :no-index:

Note how ``print`` is variadic. You can supply as many arguments as you want to it,
and each argument will be converted to a string using that object's ``__str__()``
function. The stringified arguments will then be sent to the output stream, separated
by the ``sep`` argument, which is keyword-only. In the case of a Grasshopper script node,
the default output stream is captured into the ``out`` pin.

.. end list
