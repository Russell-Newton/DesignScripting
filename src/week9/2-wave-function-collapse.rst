======================
Wave Function Collapse
======================

Wave function collapse is one of my favorite procedural generation algorithms. I just
think it's really neat. The idea for WFC is that you have a grid of cells that each
could take a variety of possible options, and you have adjacency rules that restrict which
types of cells can neighbor which types.

For example, if you're generating elements in a top-down grid, you might have cells be
able to be rivers, plains, farmland and trees, and you could restrict where the tiles
could go such that farmland can only be adjacent to farmland, rivers, and plains; and
trees can only be adjacent to trees and plains.

.. note::
    Outside of the realm of procedural generation, wave function collapse can be used in
    a Sudoku solver, which is kind of neat.

We won't be going over too many details on the algorithm on this page, partially because
I think this could be an interesting avenue for a final project, and partially because
an explanation is much better motivated by a visual aide, as in the first demo
mentioned in the next section.

Hands-On Demos
==============

There's a bunch of fantastic demos and explanations for wave function collapse online.
One of my favorites was created by `Martin Donald on itch.io <https://bolddunkley.itch.io/wfc-mixed>`__.
It also comes along with a fantastic video on how WFC works. This demo is cool because
it will let you see how choosing one option can update other cell's possible
options.

He also made another demo which shows how the adjacency rules can be inferred by an
prototype model, `found here <https://bolddunkley.itch.io/wave-function-collapse>`__.
This one is interesting because sometimes the results can be very good and other times
they can be not so good. Wave function collapse on its own is very powerful, but this
demo goes to show that introducing some intelligent design can greatly improve outcomes,
as can be seen in the first demo.

Townscaper
----------

:bdg-link-info:`Web Demo <https://oskarstalberg.com/Townscaper/>`

.. raw:: html

    <div class="sd-d-flex-row">

.. figure:: https://images.squarespace-cdn.com/content/v1/6075aa09936ef4121583faed/54e0295d-d53f-4380-807f-d33d3249bc1e/NewScreenshots_04.png
    :figwidth: 49%

.. figure:: https://images.squarespace-cdn.com/content/v1/6075aa09936ef4121583faed/e6591b39-0a29-45b3-b188-b1e39d4b453a/NewScreenshots_08.png
    :figwidth: 49%

.. raw:: html

    </div>

.. rst-class:: centered

*Source:* |townscapergame.com|_

Townscaper is a game about building island towns by placing blocks onto an irregular
grid. Using WFC, Townscaper turns these blocks into houses, arches, stairways, towers,
and more.

Tiny Glade
----------

:bdg-link-info:`Steam Store Page <https://store.steampowered.com/app/2198150/Tiny_Glade/>`

.. figure:: https://shared.cloudflare.steamstatic.com/store_item_assets/steam/apps/2198150/ss_533b0699cd1d6692cfa332f234ce03a36c547480.jpg
    :figwidth: 100%

    *Source:* |tg-steam|_

Tiny Glade is a sandbox diorama builder with a medieval theme. You can build little
castles, cottages, ruins, and so on. It's a very cute game that also uses WCF when
placing details.

.. note::
    As an aside, both Tiny Glade and Townscaper are great examples of incredible
    sound design.

.. |link-external-icon| replace:: :octicon:`link-external`
.. |townscapergame.com| replace:: *https://townscapergame.com*
.. _townscapergame.com: https://townscapergame.com
.. |tg-steam| replace:: *https://store.steampowered.com/app/2198150/Tiny_Glade/*
.. _tg-steam: https://store.steampowered.com/app/2198150/Tiny_Glade/
