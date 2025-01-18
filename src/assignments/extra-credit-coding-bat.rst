=======================
Extra Credit: CodingBat
=======================

:bdg-danger-line:`Due: Thursday, May 1, 2025`

If you elect to complete all problems in the listed Python categories on CodingBat,
you will receive an additional 2 points on your final grade (i.e.: if you would have
an 88 as your final grade, you will instead receive a 90).

The categories to fully complete to receive extra credit:

* `String-2 <https://codingbat.com/python/String-2>`__ (6 problems)
* `List-1 <https://codingbat.com/python/List-1>`__ (12 problems)
* `List-2 <https://codingbat.com/python/List-2>`__ (6 problems)
* `Logic-1 <https://codingbat.com/python/Logic-1>`__ (9 problems)
* `Logic-2 <https://codingbat.com/python/Logic-2>`__ (7 problems)

.. tip::

    I highly recommend also doing String-1, but it won't be considered for extra credit,
    whether you do it or not.

.. note::

    Some of the problems suggest creating a helper function. This is just another function
    inside of your solution on CodingBat. You have two options for this:

    #. Create a top-level helper function, i.e.:

       .. code-block:: python

           def problem(...):   # This is the function header created by the CodingBat problem
               ...             # Some solution
               helper(...)     # Call your helper
               ...             # Some more solution

           # Create this below the main function, outside of the main function body
           def helper(...):
               ...

    #. Create a nested helper, i.e.:

       .. code-block:: python

           def problem(...):
               def helper(...):
                   ...

               ...
               helper(...)
               ...

    Note the difference in placement and indentation of ``helper``.
