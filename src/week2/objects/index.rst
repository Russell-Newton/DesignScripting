=======
Objects
=======

In Python, everything is an *object*. If you're familiar with another programming
language, you might know there is a distinction between primitives and objects, but
in Python even what would normally be a primitive is an object. Even types themselves
are objects.

Methods
=======

A *method* is a function associated with an object. To call a method, you first
type an expression that resolves to the object in question (normally a variable),
a period (``.``), then the method name followed by parentheses and any arguments:

.. code-block:: python

    my_object.my_method(...)

You can think of methods as defining the "behavior" of an object.

.. note::

    Because everything in Python is an object, including types and functions,
    everything has some methods that are defined for it. This can vary by what type
    an object is, but even integers have methods that define their behavior.

Method Chaining
---------------

If one method returns another object, you can immediately call a method on that
returned object in the same line:

.. code-block:: python

    my_object.method1(...).method2(...)

Classes
=======

.. warning::

    We likely won't need to make a whole lot of classes during this course, but it's
    important to know what they are, how they work, and how to make them.

Every object is an *instance* of a *class*. Simply put, a class defines the common behaviors
shared by each instance.

Think, for example, if you have a list of attributes and behaviors that all dogs share.
Obviously, each dog is different, but the shared attributes and behaviors persist.
The description of the attributes and behaviors is like a class, and each dog is like
an instance of that class. Similarly, every instance of a class in Python might be
different, but they will all share common attributes and behaviors.

Anatomy of a Class
------------------

Let's start with an example class definition and then break it down into its components:

.. code-block:: python

    class MyClass:
        def __init__(self, ...):
            local_var = ...
            self.instance_var = ...

        def method(self, ...):
            ...

The ``class`` Statement
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    class MyClass:

Every class definition is started with ``class ClassName``. In Python, it's conventional
to use TitleCasing for class names (every word starts with a capital letter). Anything
indented below this statement is a *member* of the class definition.

.. note::

    If you need an empty class definition for some reason, you can use ``pass``:

    .. code-block:: python

        class EmptyClass:
            pass

``self``
^^^^^^^^

Every method in a class definition accepts one argument at a minimum: ``self``.
This argument is implicit, meaning you don't have to provide it when you call the
method. The only exceptions to this rule are *static methods*
(:ref:`see below <static-methods>`) and *class methods*
(:ref:`even further below <class-methods>`).

``self`` is a variable that evaluates to the instance the method is being called on. So
for example, if you call ``my_instance.some_method()``, then the ``self`` parameter
used when calling ``some_method()`` will be set to ``my_instance``.

.. note::

    Use ``self`` when accessing instance methods and variables.

The ``__init__`` Method
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    def __init__(self, ...):
        local_var = ...
        self.instance_var = ...

The ``__init__`` method defines how an instance of a class gets initialized. It's sometimes
called the *constructor* of the class. It gets called when you create a new instance of
a class:

.. code-block:: python

    my_new_instance = MyClass(...)

This is kind of like calling a function, but you're instead calling the class itself,
which has the effect of creating a new instance. Any parameters passed into this call
will get provided to the ``__init__`` method.

.. note::

    If no ``__init__`` method is defined, the ``__init__`` method of the superclass
    is used instead (see :ref:`inheritance`).

Instance Variables
~~~~~~~~~~~~~~~~~~

Parameters passed to ``__init__`` are often used to initialize *instance variables*,
which are variables associated to an instance of a class. To access them, you use
the same "dot notation" as when accessing a method:

.. code-block:: python

    my_instance.instance_var  # access
    my_instance.instance_var = something_else  # assignment

Instance variables are created in the ``__init__`` method by using the ``self`` parameter
as the instance in the dot notation. Any variables not created on ``self`` are just
local variables of ``__init__`` and cannot be accessed by other pieces of code, including
methods on the same instance.

.. dropdown:: Class Variables
    :color: warning
    :name: class-variables

    Variables can be defined at the class level, instead of the instance level. This creates
    a *class variable*, which is shared by the class itself and all instances of the class.

    .. code-block:: python

        class MyClass:
            class_variable = ...

    Modifying a class variable is a little bit strange:

    #. Modifying it on the class itself, modifies it on all existing instances
    #. Modifying it on an instance only changes it on the instance, and also makes it
       so that modifications made on the class are no longer reflected on that instance

    .. code-block:: python

        MyClass.class_variable = 0
        instance1 = MyClass()
        instance2 = MyClass()

        print(instance1.class_variable, instance2.class_variable)  # 0 0
        MyClass.class_variable = 1
        print(instance1.class_variable, instance2.class_variable)  # 1 1
        instance1.class_variable = 2
        print(instance1.class_variable, instance2.class_variable)  # 2 1
        MyClass.class_variable = 3
        print(instance1.class_variable, instance2.class_variable)  # 2 3
        instance2.class_variable = 4
        print(instance1.class_variable, instance2.class_variable)  # 2 4
        MyClass.class_variable = 5
        print(instance1.class_variable, instance2.class_variable)  # 2 5


Instance Methods
^^^^^^^^^^^^^^^^

To create your own methods, you create them like any other function, indented inside
the class body, including ``self`` as the first parameter.

.. dropdown:: Static Methods
    :color: warning
    :name: static-methods

    Sometimes, you might want a method that doesn't actually need any specific instance
    of a class to run, but it's associated to that class and makes sense to bundle into it.
    Methods of this type are called *static*, don't have the ``self`` parameter, and can
    be called either from the class itself or from any instance:

    .. code-block:: python

        class MyClass:

            @staticmethod
            def my_static_method():
                ...

        # Can be called like:
        MyClass.my_static_method()
        # or
        my_instance.my_static_method()

    The :external+python:py:func:`staticmethod` decorator right before the method
    definition tells Python that the method is a static method and shouldn't be
    provided with the ``self`` parameter.

Inheritance
===========

In Python, classes can *inherit* from one another. Basically any attributes or behavior
created in a *superclass* will also exist for a *subclass*:

.. code-block:: python

    # Superclasses are specified as seen below
    class Subclass(Superclass):
        ...

.. note::

    A class can have multiple superclasses, if you want, but it can make things
    significantly weirder.

Going back to the dog analogy, you might have a class ``Dog`` that defines behavior
for all dogs, and you might make subclasses of ``Dog`` that define breed-specific
attributes and behavior, such as ``ChocolateLab`` or ``LittleCrustyWhiteDog``.

.. important::

    All classes inherit from ``object``. It is implied, and you don't need to manually
    specify it.

.. admonition:: A note on class variables
    :class: note

    Class variables are inherited by a subclass. Similar to the weirdness with instances
    and class variables, subclasses share the same value of the class variable unless
    it gets redefined.

    .. code-block::

        class A:
            var = 1

        class B(A):
            var = 2  # B.var is no longer linked to A.var

        class C(A):
            pass  # C.var is the same as A.var

        B.var = 3  # doesn't change A.var
        A.var = 4  # also affects C.var
        C.var = 5  # C.var no longer tied to A.var
        A.var = 6  # B.var is still 4, C.var is still 5

Inherited Methods
-----------------

All methods in a superclass are inherited by the subclass. That is, you can call
a method on an instance of ``LittleCrustyWhiteDog`` that is defined in ``Dog``, and it will
exhibit the same behavior as an instance of ``Dog``. If you want this behavior to
differ, you can redefine the method to do something different:

.. code-block:: python

    class Dog:
        def speak(self):
            print("Bark!")

    class LittleCrustyWhiteDog(Dog):
        def speak(self):
            print("Yip!")

You can, optionally, call the corresponding method on the superclass using
:external+python:py:func:`super`:

.. code-block:: python

    class GrandmasDog(LittleCrustyWhiteDog):
        def speak(self):
            super().speak()  # Prints "Yip!"
            print("Also pees on the ground for no reason")

.. admonition:: A note on ``__init__``
    :class: note

    When no ``__init__`` method is defined, the superclass's ``__init__`` will get called
    by default, accepting the same parameters. If an ``__init__`` method *is* defined
    on the subclass, the superclass ``__init__`` **MUST** be called with
    ``super().__init__(...)``.

.. admonition:: A note on static methods
    :class: note

    If you want to redefine a static method in a subclass, you'll want to decorate it with
    :external+python:py:func:`staticmethod` in the subclass. Otherwise, Python will think
    you're redefining the method to be an instance method.

.. dropdown:: Class Methods
    :name: class-methods
    :color: warning

    Class methods are methods that are associated to the class itself, not to an instance
    of the class. Instead of accepting the ``self`` parameter, they accept a ``cls``
    implicit parameter, which is defined to be the class the method is called on:

    .. code-block:: python

        class MyClass:

            @classmethod
            def my_class_method(cls, ...):
                ...

    Class methods can be called on an instance on the class as well as the class itself.

    Like static methods, class methods are decorated with :external+python:py:func:`classmethod`.

    Inheritance is where class methods are most useful. Say you have:

    .. code-block:: python

        class A:
            @classmethod
            def do_something(cls):
                print(cls.__name__)

        class B(A):
            @classmethod
            def do_something(cls):
                super().do_something()
                print("Hello!")

    Running ``A.do_something()`` would print "A", and running ``B.do_something()`` would
    print "B" followed by "Hello!". Note how, as with static methods, when redefining
    a class method, you want to use the :external+python:py:func:`classmethod` decorator
    again in the subclass.

Useful Functions and Methods
============================

.. include:: ../../resources/helpful-functions.rst
    :start-after: .. start class-related
    :end-before: .. end class-related

Magic Methods
=============

Sometimes, you might want your class to mimic built-in types or have more control
over the life cycle of a class. This is facilitated with special methods that have
names starting with two underscores and ending with two underscores. These are often
called "magic methods" or "dunder methods" (for double-underscore). ``__init__`` is
one such method.

There's a huge list of all magic methods and their descriptions available on
`Python's documentation <https://docs.python.org/3.9/reference/datamodel.html#special-method-names>`__.

Some useful ones to know:

* `__init__ <https://docs.python.org/3.9/reference/datamodel.html#object.__init__>`__ (initialization)
* `__str__ <https://docs.python.org/3.9/reference/datamodel.html#object.__str__>`__ (conversion to a human-readable string)
* `__bool__ <https://docs.python.org/3.9/reference/datamodel.html#object.__bool__>`__ (conversion to ``True`` or ``False``)
* `__int__ <https://docs.python.org/3.9/reference/datamodel.html#object.__int__>`__ (conversion to an integer)
* `__float__ <https://docs.python.org/3.9/reference/datamodel.html#object.__float__>`__ (conversion to a floating-point number)
* `__len__ <https://docs.python.org/3.9/reference/datamodel.html#object.__len__>`__ (used with :external+python:py:func:`len`)
* `__getitem__ <https://docs.python.org/3.9/reference/datamodel.html#object.__getitem__>`__ (access with indexing)
* `__setitem__ <https://docs.python.org/3.9/reference/datamodel.html#object.__setitem__>`__ (assignment with indexing)
* `__delitem__ <https://docs.python.org/3.9/reference/datamodel.html#object.__delitem__>`__ (deletion with indexing)
* `__contains__ <https://docs.python.org/3.9/reference/datamodel.html#object.__contains__>`__ (used with ``in`` and ``not in``)
* `Rich comparison methods <https://docs.python.org/3.9/reference/datamodel.html#object.__lt__>`__ (``<``, ``<=``, ``==``, ``>=``, ``>``, ``!=``)
* `Numeric operators <https://docs.python.org/3.9/reference/datamodel.html#emulating-numeric-types>`__ (``+``, ``-``, ``*``, ``/``, ``//``, ``%``, ``**``, etc.)
