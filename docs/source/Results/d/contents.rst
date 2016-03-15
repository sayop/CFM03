=============
 Problem1 - d
=============

Examine the method stability with different grids. Determine the maximum time step that leads to a stable solution and compare it to the stability criteria.


------------------
 Grid spacing test
------------------

Here, the stabilith test is performed with different set of grid spacing. To rule out other effect of numerical setup, *Courant* number and :math:`\beta` remain constant whereas only grid spacing changes. Following table shows the stability check. *O* denotes the *stable* condition and *X* represents the *unstable* condition.

  +---------+-----------+
  |  NxN    | stability |
  +=========+===========+
  |  10x10  |  *X*      |
  +---------+-----------+
  |  15x15  |  *X*      |
  +---------+-----------+
  |  16x16  |  *X*      |
  +---------+-----------+
  |  17x17  |  *O*      |
  +---------+-----------+
  |  18x18  |  *O*      |
  +---------+-----------+
  |  20x20  |  *O*      |
  +---------+-----------+


------------------
 Maximum time step
------------------

In this code, the variable time step method is used to maintain stable numerically. Therefore, the code does not run with constant time step. The maximum time step test is performed with different set of *Courant* number condition. The grid spacing is fixed with 20x20 to have fast running of simulation.

  .. figure:: ./images/stabilityCr.png
     :scale: 80%

  +-----------+----------------------+
  | Courant # | dt at last iteration |
  +===========+======================+
  |  0.5      | 0.007470             |
  +-----------+----------------------+
  |  0.51     | 0.007620             |
  +-----------+----------------------+
  |  0.55     | 0.008218             |
  +-----------+----------------------+
  |  0.6      | 0.008653             |
  +-----------+----------------------+
  |  0.8      | 0.007761             |
  +-----------+----------------------+
