============================
Applying Randomness to Grids
============================

Here, we'll see a couple of different applications of randomness to grids. Of course,
you can apply randomness in other ways, but grids facilitate a handful of examples
pretty well.

Randomized Height Maps
======================

Height maps are an easy way to create "2.5D" surfaces. The idea is that you have a
grid of heights, and a point is placed above the grid at each height. You can then
connect these points with a surface.

Height maps can, of course, be created with curated data, as is the case with topographies,
but being able to take advantage of randomness can be interesting.

A Simple Random Height Map
--------------------------

To make a simple random height map, you can use the Square component to create a grid
of points. Pass these into a Python 3 Script component with the following properties:

**Inputs:**

* ``in_point``, type-hinted as Point3d, set to Item Access

**Outputs:**

* ``out_point``, type-hinted as Point3d

**Source Code:**

.. code-block::

    import random

    in_point.Z = random.randrange(-1, 1)  # These numbers can be whatever you want
    out_point = in_point  # Explicitly set the out_point to the in_point

Take the output of ``a``, and pass it into a Surface From Points component.
**Make sure that the Points input is flattened!!** To set the U Count input on this
surface component, make it 1 higher than the Extent X used to create the Square grid.

.. note::

    This is a very simple way to apply randomness to a height map, but it can be used
    on an existing height map to apply some small variation.

A Height Map With Choices
-------------------------

This is a contrived example that shows how you can provide a list of possible heights
to the randomizer. The rest of the Grasshopper definition is the same as the previous
example, but we'll have a new Python 3 Script component:

**Inputs:**

* ``in_point``, type-hinted as Point3d, set to Item Access
* ``height_choices``, type-hinted as float, set to List Access

**Outputs:**

* ``out_point``, type-hinted as Point3d

**Source Code:**

.. code-block:: python

    import random

    in_point.Z = random.choice(height_choices)
    out_point = in_point


A Height Map With Random Peaks
------------------------------

As a more interesting exercise, we can create height maps with randomly defined peaks.
To do this, we can randomly create some peaks, and use those randomly created peaks
to set the heights in our height map.

To do this, we'll first need a script component to create the peaks:

**Inputs:**

* ``peak_count``, type-hinted as int, set to Item Access
* ``max_x``, type-hinted as float, set to Item Access
* ``max_y``, type-hinted as float, set to Item Access
* ``min_height``, type-hinted as float, set to Item Access
* ``max_height``, type-hinted as float, set to Item Access

**Outputs:**

* ``peaks``, type-hinted as Point3d

**Source Code:**

.. code-block:: python

    import random

    from Rhino.Geometry import Point3d

    peaks = []
    for _ in range(peak_count):
        x = random.uniform(0, max_x)
        y = random.uniform(0, max_y)
        z = random.uniform(min_height, max_height)
        peaks.append(Point3d(x, y, z))

You'll then need to pipe ``peaks`` into a second script component:

**Inputs:**

* ``in_point``, type-hinted as Point3d, set to Item Access
* ``peaks``, type-hinted as float, set to List Access

**Outputs:**

* ``out_point``, type-hinted as Point3d

**Source Code:**

.. code-block:: python

    import random
    from Rhino.Geometry import Point3d

    in_point: Point3d
    out_point = in_point

    # You can tweak this to be whatever you want
    def influence_function(peak: Point3d) -> float:
        d = in_point.DistanceToSquared(Point3d(peak.X, peak.Y, 0))
        return peak.Z / (1 + d / 10)

    for peak in peaks:
        out_point.Z += influence_function(peak)

Random Crawls
=============

Pick a point at random. Draw a line from it to a random neighboring point, and repeat
from the neighboring point until you can no longer pick any neighbors that hasn't been
connected to. This makes a "crawl" across the entire grid.

A Polyline Crawl
----------------

Create a Square grid, and pipe the Points output into a Python 3 Script component:

**Inputs:**

* ``points``: type-hinted as Point3d, set to Tree Access
* ``seed``: type-hinted as int, set to Item Access

**Outputs:**

* ``crawl``: type-hinted as Polyline

**Source Code:**

.. code-block:: python

    import random

    import ghpythonlib.treehelpers as th
    import rhinoscriptsyntax as rs
    from Rhino.Geometry import Vector3d

    random.seed(seed)

    # Set up the input
    points = th.tree_to_list(points)[0]  # Need to get the first sublist because
                                         #   the Square component outputs {0;0;A}(B)
                                         #   not {0;A}(B)
    extent_x = len(points)
    extent_y = len(points[0])

    # Set up the output
    crawl = []

    # Set up the code to find neighbors that can be visited
    visited = set()
    def can_visit(point):
        x, y = point
        if x < 0 or x >= extent_x:
            return False
        if y < 0 or y >= extent_y:
            return False
        return point not in visited

    # Set up the code to find the neighbors of a point
    def neighbors_of(point):
        x, y = point
        return list(filter(can_visit, [
            (x + 1, y),
            (x, y + 1),
            (x - 1, y),
            (x, y - 1),
            # (x + 1, y + 1),
            # (x + 1, y - 1),
            # (x - 1, y + 1),
            # (x - 1, y - 1),
        ]))
        # You can uncomment the last 4 to get the diagonal neighbors

    # Randomly pick a start point
    start_x = random.randint(0, extent_x - 1)
    start_y = random.randint(0, extent_y - 1)
    start = (start_x, start_y)

    # Add the start point to the crawl
    visited.add(start)
    crawl.append(start)

    # Get the neighbors of the start point
    neighbors = neighbors_of(start)
    # Loop until there's no more neighbors
    while len(neighbors) > 0:
        # Choose a neighbor at random
        chosen = random.choice(neighbors)

        # Add the chosen neighbor to the crawl
        visited.add(chosen)
        crawl.append(chosen)

        # Get the next set of neighbors
        neighbors = neighbors_of(chosen)

    # Convert the crawl into a polyline
    crawl = rs.AddPolyline([
        points[x][y]
        for x, y in crawl
        # The crawl is saved as (x, y) points, get the Point3d
        #   grid points corresponding to (x, y)
    ])

Using a Crawl
-------------

The crawls created by the previous example aren't necessarily interesting for design, but
by tweaking the neighbor selection or by introducing more information, you can
curate the crawls to have interesting properties.

Additionally, you could change how the crawl is realized in the output. In the example,
the crawls create polylines, but you could do a lot more with a crawl. I've created a
file demonstrating some things you can do once you have a simple crawl. You can download
it here: :download:`simple-crawl.gh <../_static/grasshopper-files/simple-crawl.gh>`.

The examples in the file are not exhaustive. There's plenty you can do, such as modifying
grid cells the crawl touches, placing geometry at turns, and applying an attractor force
to points near the crawl.

Modifications of crawls, like those that can branch, can also be very interesting.
We'll see branching crawls in Assignment 3.
