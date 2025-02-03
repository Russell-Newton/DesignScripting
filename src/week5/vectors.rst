=========================
A Crash Course in Vectors
=========================

Vectors are the backbone of computational geometry, computer-aided modeling and design,
and, importantly for this week's lessons, grids. If you've taken a linear algebra class,
you likely either think they're neat or hate them with a passion (if you follow my
educational trajectory, you love them). For this class though, we'll really only need
to know a handful of things about them.

What Makes a Vector a Vector
============================

Most of the time when we work with numbers, we use them as *scalars*. The core idea
of scalars is that they can be added and multiplied, with the following axioms:

* Associativity: :math:`a + (b + c) = (a + b) + c` and :math:`a \cdot (b \cdot c) = (a \cdot b) \cdot c`
* Commutativity: :math:`a + b = b + a` and :math:`a \cdot b = b \cdot a`
* Additive and multiplicative identities: :math:`a + 0 = a` and :math:`a \cdot 1 = a`
* Additive inverses: :math:`a + (-a) = 0`
* Multiplicative inverses: if :math:`a \ne 0`, :math:`a \cdot a^{-1} = 1`
* Distributivity of multiplication over addition: :math:`a \cdot (b + c) = a \cdot b + a \cdot c`

Vectors, on the other hand, can be added together or multiplied to scalars. To distinguish
between vectors and scalars, vectors are often expressed in boldface. Vector addition
and scalar multiplication satisfy the following axioms:

* Associativity of vector addition: :math:`\mathbf{u} + (\mathbf{v} + \mathbf{w}) = (\mathbf{u} + \mathbf{v}) + \mathbf{w}`
* Commutativity of vector addition: :math:`\mathbf{u} + \mathbf{v} = \mathbf{v} + \mathbf{u}`
* Identity of vector addition: :math:`\mathbf{v} + \mathbf{0} = \mathbf{v}`

  * Note that this :math:`\mathbf{0}` is a vector, not the scalar additive identity, :math:`0`.

* Inverses of vector addition: :math:`\mathbf{v} + (-\mathbf{v}) = \mathbf{0}`
* Scalar multiplication "associativity": :math:`a (b \mathbf{v}) = (ab)\mathbf{v}`
* Scalar multiplicative identity: :math:`1\mathbf{v} = \mathbf{v}`
* Distributivity of scalar multiplication with respect to vector addition: :math:`a(\mathbf{u} + \mathbf{v}) = a\mathbf{u} + a\mathbf{v}`
* Distributivity of scalar multiplication with respect to scalar addition: :math:`(a + b)\mathbf{v} = a\mathbf{v} + b\mathbf{v}`

.. note::

    A lot of these rules look similar, and that's no mistake. Technically, real numbers
    can be used as vectors, with real numbers as scalars (which is quite silly). If you
    wanted to go a little crazy though, you can use whatever you want as scalars and
    vectors, assuming you can define your addition and multiplication operations
    appropriately.

.. admonition:: A Vector Space Over a Field
    :class: seealso

    The axioms above technically define what makes a set a *field* (with the additional
    assertion that the set is closed under addition and multiplication) and what makes
    a set a *vector space over a field* (with the assertion that the set is closed
    under vector addition and scalar multiplication). I'll be using this terminology
    in the future.

Vectors in :math:`\mathbb{R}^3`
===============================

The types of vectors we'll be using most in this class are part of the set denoted
:math:`\mathbb{R}^3`. The field you use for scalar multiplication is normally the real
numbers themselves (:math:`\mathbb{R}`), but you could also use the integers (:math:`\mathbb{Q}`)
like we'll do with grids or some other subset of the real numbers.

Vectors in :math:`\mathbb{R}^3` are often represented as an ordered pair of 3 numbers:
:math:`\mathbb{v} = (x, y, z)`. They can also be rewritten as a row vector

.. math::

    \begin{bmatrix}
    x & y & z
    \end{bmatrix}

or as a column vector

.. math::

    \begin{bmatrix}
    x \\
    y \\
    z
    \end{bmatrix}

We won't be doing any matrix multiplication in this class, so it doesn't really matter
which form you use. I like column vectors, but row vectors can be written inline
in text, so I'll switch between both.

Vectors of this form are often used to represent points in 3-D space, where :math:`x`
is the point's position along the X-axis, :math:`y` is the point's position along the
Y-axis, and :math:`z` is the point's position along the Z-axis. These are called the
X component, Y component, and Z component, respectively.

Operations
----------

Given two vectors in :math:`\mathbb{R}^3`, :math:`\mathbf{u} = \begin{bmatrix}u_x & u_y & u_z\end{bmatrix}`
and :math:`\mathbf{v} = \begin{bmatrix}v_x & v_y & v_z\end{bmatrix}`, and a scalar, :math:`a`,
vector addition and scalar-vector multiplication in :math:`\mathbb{R}^3` is defined by:

.. math::

    \mathbf{u} + \mathbf{v} = \begin{bmatrix}
        u_x + v_x \\
        u_y + v_y \\
        u_z + v_z
    \end{bmatrix}

and

.. math::

    a\mathbf{u} = \begin{bmatrix}
        a \cdot u_x \\
        a \cdot u_y \\
        a \cdot u_z
    \end{bmatrix}

Basis Vectors
-------------

In :math:`\mathbb{R}^3`, you can choose any three vectors :math:`\mathbf{u}`,
:math:`\mathbf{v}`, and :math:`\mathbf{w}` (where you can't scale and add 2 of them to get
the other), and by scaling and adding them together, you can make any other vector
in :math:`\mathbb{R}^3`. The 3 vectors you choose are called a *basis* for
:math:`\mathbb{R}^3`. The conventional choice for these 3 vectors to use represent 1
unit of distance along the X, Y, and Z-axes, often called the "elementary" basis vectors,
:math:`\mathbf{e}_1`, :math:`\mathbf{e}_2`, and :math:`\mathbf{e}_3`.

If you choose a different basis, you can still express your vector as
:math:`\mathbf{v} = \begin{bmatrix} a & b & c \end{bmatrix}`, but the assumption is that
:math:`\mathbf{v}' = a\mathbf{u} + b\mathbf{v} + c\mathbf{w}`, and not just
:math:`a\mathbf{e}_1 + b\mathbf{e}_2 + c\mathbf{e}_3`. This will come in handy once we
start working with grids.

Rhino.Geometry.Vector3d
=======================

When working with vectors in Grasshopper, we'll frequently be using the ``Vector3d`` type
provided by RhinoCommon. You can read up on it's entire API
`here <https://developer.rhino3d.com/api/rhinocommon/rhino.geometry.vector3d?version=8.x>`__.

``Vector3d`` objects are constructed with the elementary basis, and as such are analogous to
the ``Point3d`` type provided by RhinoCommon. There are differences in semantics though,
where ``Vector3d`` is used more often to represent a direction or translation, while a ``Point3d``
is used to represent a point geometry. As such, ``Vector3d``\ s tend to be more useful
when doing math. If/when you need a ``Point3d``, you can simply construct a new ``Point3d``
from the ``Vector3d`` (``my_point = Point3d(my_vector)``), or use type coercion with
your input/output type hints on a Python 3 Script component.

There's a bunch of stuff that you can do with ``Vector3d``\ s, but the most useful things
you'll likely want to know is that you can do vector addition (and subtraction) and
scalar multiplication (and division) can all be performed with the corresponding
arithmetic operators (``+``, ``-``, ``*``, and ``/``):

>>> from Rhino.Geometry import Vector3d
>>> u: Vector3d = Vector3d(1, 2, 3)
>>> v: Vector3d = Vector3d(4, 5, 6)
>>> a: float = 10
>>> u + v
Vector3d(5, 7, 9)
>>> u - v
Vector3d(-3, -3, -3)
>>> u * a
Vector3d(10, 20, 30)
>>> u / a
Vector3d(0.1, 0.2, 0.3)

If you want a vector's length, use the ``Length`` property:

>>> u: Vector3d = Vector3d(3, 4, 0)
>>> u.Length
5.0

If you have a vector and want to create a new vector in the same direction with a length
of 1, you can either make one manually or use the ``Unitize()`` method to modify
the vector in-place:

>>> u: Vector3d = Vector3d(6, 0, 8)
>>> u_unit: Vector3d = u / u.Length
>>> u_unit
Vector3d(0.6, 0, 0.8)
>>> u.Unitize()
>>> u
Vector3d(0.6, 0, 0.8)
