====================
Randomness in Python
====================

In Python, the :external+python:py:mod:`random` module implements random number
generators for sampling a bunch of different distributions. Technically, these are
pseudo-random, meaning the numbers created only seem random, but it will take an astronomically
long time before the generators start repeating themselves.

To start using :external+python:py:mod:`random`, place the following at the top of
your script:

.. code-block:: python

    import random

.. note::

    While some of these can be recreated with Grasshopper nodes, some cannot be, and
    some cannot be recreated without more effort than it would take to create a simple
    script node with a few lines of code.

Using Seeds
===========

It's important to note that these random number generators are deterministic, meaning
if you know the initial configuration, you can predict exactly which numbers will be
produced after ``n`` steps. For us, this is useful because it means we can recreate
the same design if we start with the same *seed*. Setting the seed of the random
number generator completely determines what numbers will be generated. If you play
a lot of Rogue-likes, this is the same concept that you've seen with the seed of a run.

To set the seed used globally in the :external+python:py:mod:`random` module, you can
use the :external+python:py:func:`random.seed` function:

.. autofunction:: random.seed
    :no-index:

Within Grasshopper, it's practical for us to be able to provide a seed to a Python 3
script node via a slider, so that we can have an easy way outside of our script to set
the seed. To do this, add an input type-hinted to *int*, and pass the value to
:external+python:py:func:`random.seed`:

.. code-block:: python

    import random

    seed: int  # provided by an input pin
    random.seed(seed)

.. note::

    If you don't call :external+python:py:func:`random.seed` before using the random
    number generator, the seed will be set as if you passed ``None`` to :external+python:py:func:`random.seed`.

Generating Random Numbers
=========================

The functions provided by the :external+python:py:mod:`random` module are all based
on the :external+python:py:func:`random.random` function. This generates a floating
point number in the range [0.0, 1.0) with a uniform distribution.

.. code-block:: python

    import random

    x = random.random()  # x is now a pseudo-random floating point number in the range [0.0, 1.0)

Before talking about the functions that can make what you want to do easier, let's take
a look at how we can use the output of :external+python:py:func:`random.random` to
create a bunch of different pseudo-random results for us.

Generating a Different Uniform Distribution
-------------------------------------------

If you want to generate numbers in a different range, you'll need to transform the
output of :external+python:py:func:`random.random`, ``x`` with simple arithmetic. To increase
the high end of the range from 1 to any number ``a``, you'll need to multiply ``x``
by ``a``. To shift the start and endpoints of the range with the same number ``b``, you'll
need to add ``b`` to ``x``.

How would you generate an arbitrary uniform distribution, [low, high)?

.. dropdown:: Answer
    :color: secondary

    .. code-block:: python

        import random

        def uniform(low: float, high: float) -> float:
            x = random.random()
            x *= high - low  # stretch the range
            x += low  # shift the range
            return x

This behavior is provided by the :external+python:py:func:`random.uniform` function.

.. autofunction:: random.uniform
    :no-index:

.. note::

    This is something that can be done easily with the Random component in Grasshopper.

Generating Integers
-------------------

The :external+python:py:func:`random.random` function returns floating-point numbers,
but if you want random integers, you'll need to convert a generated floating-point number
to an integer using :external+python:py:class:`int() <int>`. If you do this directly on
the output of :external+python:py:func:`random.random`, you'll always get 0, because converting
a float to an int in Python just floors the floating-point number.

How would you sample an arbitrary integer distribution, [low, low + 1, low + 2, ..., high]?


.. dropdown:: Answer
    :color: secondary

    .. code-block:: python

        import random

        def randint(low: int, high: int) -> int:
            x = random.random()
            x *= high - low + 1  # Add 1 because flooring floats in the range [0, a) yields ints in the range [0, a - 1]
            x += low  # Shift
            x = int(x)  # Floor
            return x

This behavior is provided by the :external+python:py:func:`random.randint` function.

.. autofunction:: random.randint
    :no-index:

.. warning::

    This is not something you can do well with Grasshopper, even though the random
    component can be set to generate integer numbers. This component uses rounding to
    convert to integers, which means you're actually not getting a uniform distribution
    of integers when you use this component.

Generating an Arbitrary Distribution
------------------------------------

Arbitrary real-valued distributions can be sampled if you can convert from the standard
uniform distribution to your target distribution. Transformations of this sort will often
look like a real-valued function :math:`f:\: \mathbb{R} \rightarrow \mathbb{R}`.

Any real-valued distribution can be converted to a discrete integer-valued distribution
using :external+python:py:class:`int() <int>`, but be careful to note that this
conversion floors floating-point numbers, which has implications for the distribution
of integers created.

Random Sequence Operations
==========================

Some operations you might want to perform on sequences can be supplemented with the
:external+python:py:mod:`random` module. Namely, you might want to pick one or
more items from the sequence at random.

Picking a Random Item
---------------------

:bdg-info-line:`Very Useful!`

To take a single random item from a sequence, you effectively want to choose a random
integer index to use to subscript the sequence. The index you'll use will need to be
at least 0 and up to, but not including, the length of the sequence.

How would you pick a random item from a given sequence?

.. dropdown:: Answer
    :color: secondary

    .. code-block:: python

        import random
        from typing import Any, Sequence

        def choice(sequence: Sequence[Any]) -> Any:
            x = random.random()
            x *= len(sequence)  # Scale the range to [0, len(sequence))
            x = int(x)  # Convert to int distribution [0, len(sequence) - 1]
            return sequence[x]

This behavior is provided by the :external+python:py:func:`random.choice` function.

.. autofunction:: random.choice
    :no-index:

.. warning::

    This can be simulated with Grasshopper to create an index and sample a list, but
    again, the default behavior for converting real numbers to integers is by rounding,
    so you won't get a uniform distribution of selected items.

Picking Multiple Items with Replacement
---------------------------------------

To select multiple random items from a sequence with replacement, you basically just
have to repeatedly pick a single random item. Because we're replacing the items that
we take, we don't mind if we take multiple of the same thing.

How would you pick ``n`` items from a given sequence, with replacement?

.. dropdown:: Answer
    :color: secondary

    .. code-block:: python

        import random
        from typing import Any, List, Sequence

        def choices(sequence: Sequence[Any], n: int) -> List[Any}:
            out = []
            # Using _ as the iteration variable is just a way to say we don't really
            #  care about the variable
            for _ in range(n):
                x = random.random()
                x *= len(sequence)
                x = int(x)
                out.append(sequence[x])
            return out

This behavior is provided by the :external+python:py:func:`random.choices` function.

.. autofunction:: random.choices
    :no-index:

Picking Multiple Items Without Replacement
------------------------------------------

Picking multiple items from a sequence without replacement is a bit trickier, because
we need to make sure that we don't have any repeats. A naive approach might be to
create a set of indices that have already been sampled and check that you haven't
already checked the number that you drew at random:

.. code-block:: python

    import random

    def sample(sequence: Sequence[Any], n: int) -> List[Any]
        out = []
        sampled = set()
        while len(out) < n:
            idx = random.randint(len(sequence))
            if idx in sampled:
                continue
            set.add(idx)
            out.append(sequence[idx])
        return out

What's the issue with this approach?

.. dropdown:: Answer
    :color: Secondary

    It's possible you might sample values for ``idx`` that you've already sampled many
    different times in a row, and you may end up looping a lot.

A smarter approach might be to create a companion list of indices that haven't been
sampled yet and remove items from this list as you sample your sequence. How might you
do this?

.. dropdown:: Answer
    :color: secondary

    .. code-block:: python

        import random
        from typing import Any, List, Sequence

        def sample(sequence: Sequence[Any], n: int) -> List[Any}:
            out = []
            indices = list(range(len(sequence)))  # Convert to a list because we need a sequence, not a range
            for _ in range(n):
                idx = random.choice(indices)  # Pick an index
                indices.remove(idx)  # Remove it from the available indices
                out.append(sequence[idx])  # Add the picked item to the output
            return out

This behavior is provided by the :external+python:py:func:`random.sample` function.

.. autofunction:: random.sample
    :no-index:

.. important::

    This function can be used to create a shuffled version of a sequence:

    .. code-block:: python

        import random
        from typing import Any, List, Sequence

        def shuffled(sequence: Sequence[Any]) -> List[Any]
            return random.sample(sequence, len(sequence))

    To shuffle a sequence in place (meaning you change the sequence itself without
    returning anything), you can use the :external+python:py:func:`random.shuffle`
    function.

.. warning::

    To the best of my knowledge, sampling without replacement and shuffling a sequence
    *cannot* be recreated with Grasshopper!
