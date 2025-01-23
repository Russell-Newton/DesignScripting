====================
Type Hints Reference
====================

This page serves as a reference to various type hints you might see during the course.

This is a living list that will expand over the course of the semester.

Basic Types
===========

.. start basic

=================================== =================================
Type Hint                           Description
=================================== =================================
:external+python:py:class:`int`     An integer
:external+python:py:class:`float`   A floating-point (real) number
:external+python:py:class:`str`     A string
:external+python:py:class:`bool`    A Boolean (``True`` or ``False``)
:external+python:py:obj:`None`      ``None`` (useful on return types)
=================================== =================================

.. end basic

Advanced Types
==============

These type hints all come from the :external+python:py:mod:`typing` package and can be imported with:

.. code-block:: python

    from typing import ...

.. warning::

    Type hinting in later versions of Python has changed to support easier syntax
    and to separate many of the type hints provided by :external+python:py:mod:`typing`
    to more relevant packages like :external+python:py:mod:`collections.abc`.

.. start advanced

Special Typing Primitives and Forms
-----------------------------------

* :external+python:py:obj:`typing.Any`: compatible with every type
* :external+python:py:obj:`typing.Union`: one of multiple types

  * Parameterized as ``Union[Type1, Type2, etc.]```

* :external+python:py:obj:`typing.Optional`: either the specified type or ``None``

  * ``Optional[X]`` is equivalent to ``Union[X, None]``

* :external+python:py:obj:`typing.Literal`: value will be one of provided values

  * ``Literal[1, 2, "hello"]`` means the value will either be ``1``, ``2``, or ``"hello"``.
    This is most useful on function parameters or outputs.
  * I don't know if we'll use this in this class

Collections Type Hints
----------------------

.. note::

    Technically, :external+python:py:class:`tuple`, :external+python:py:class:`list`,
    :external+python:py:class:`set`, :external+python:py:class:`frozenset`, and
    :external+python:py:class:`dict` can all be parameterized directly instead of
    having to use their :external+python:py:mod:`typing` counterpart shown below.

* :external+python:py:obj:`typing.List`, parameterized as ``List[ItemType]``
* :external+python:py:obj:`typing.Set`, parameterized as ``Set[ItemType]``
* :external+python:py:obj:`typing.FrozenSet`, parameterized as ``FrozenSet[ItemType]``
* :external+python:py:obj:`typing.Dict`, parameterized as ``Dict[KeyType, ValueType]``
* :external+python:py:obj:`typing.Tuple`, parameterized as ``Tuple[Item1Type, Item2Type, etc.]``

  * Because a tuple has a fixed size, you need to explicitly state the types of each item.
  * To specify an unknown-length tuple of homogeneous type, you can do ``Tuple[ItemType, ...]``
    with the ellipses after the ``ItemType``.
  * To specify an empty tuple, use ``Tuple[()]``

* :external+python:py:obj:`typing.Collection`, parameterized as ``Collection[ItemType]``

  * Supports :external+python:func:`len`

* :external+python:py:obj:`typing.Container`, parameterized as ``Container[ItemType]``

  * Supports containment checks with ``in`` and ``not in``

* :external+python:py:obj:`typing.Iterable`, parameterized as ``Iterable[ItemType]``

  * Supports iteration with a ``for`` loop

* :external+python:py:obj:`typing.Sequence`, parameterized as ``Sequence[ItemType]``

  * Supports subscripting with integers and :external+python:func:`reversed`

.. end advanced
