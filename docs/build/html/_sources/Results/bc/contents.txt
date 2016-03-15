================
 Problem1 - b, c
================

Consider the case when :math:`H=W` (a square cavity). Here, the Reynolds number, :math:`Re=UW/\nu`, characterizes the flow patters. Compute the steady state solutions for both :math:`Re=100` and :math:`Re=500`. Plot the flow streamlines and centerline profiles (:math:`u` vs. :math:`y` and :math:`v` vs. :math:`x` through the center of the domain). For :math:`Re=100`, valdiate your method by comparing your results to data from given literature.


---------
 Re = 100
---------

- NxN = 20x20

  .. figure:: ./images/Re100/strm_20x20.png
     :scale: 80%

  - u-velocity

    .. figure:: ./images/Re100/uVel_20x20.png
       :scale: 60%

  - v-velocity

    .. figure:: ./images/Re100/vVel_20x20.png
       :scale: 60%


  - **Observation**

    - Streamlines roughly forms and recirculation zone in the bottom right can be found.
    - This course grid case shows bad estimation of u and v-velocity as compared to the Ghia's data

|
  
- NxN = 40x40

  .. figure:: ./images/Re100/strm_40x40.png
     :scale: 80%

  - u-velocity

    .. figure:: ./images/Re100/uVel_40x40.png
       :scale: 60%

  - v-velocity

    .. figure:: ./images/Re100/vVel_40x40.png
       :scale: 60%


  - **Observation**

    - The predicted u- and v-velocity approached closer to the Ghia's data



 
|

- NxN = 80x80

  .. figure:: ./images/Re100/strm_80x80.png
     :scale: 80%

  - u-velocity

    .. figure:: ./images/Re100/uVel_80x80.png
       :scale: 60%

  - v-velocity

    .. figure:: ./images/Re100/vVel_80x80.png
       :scale: 60%

  - **Observation**
   
    - The currently predicted data seems to be almost identical with the Ghia's solution.
    - Recirculation zone in the bottom left and right seems more clear than the coarser grid cases.


|

---------
 Re = 500
---------


- NxN = 20x20

  .. figure:: ./images/Re500/strm_20x20.png
     :scale: 80%

|


- NxN = 80x80

  .. figure:: ./images/Re500/strm_80x80.png
     :scale: 80%

