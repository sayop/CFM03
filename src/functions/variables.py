import numpy as np

class domainVars:
   x = []
   y = []
   dx = 0.0
   dy = 0.0
   Lref = 0.0

class flowVars:
   Re = 0.0
   Uref = 0.0
   nu = 0.0	# kinematic viscosity
   p = []       # kinematic pressure: used for both dimensional and non-dimensional forms
   u = []       # u velocity: used for both dimensional and non-dimensional forms
   v = []       # v velocity: used for both dimensional and non-dimensional forms

class FDM:
   # solution vector: will store 3 elemetns of primitive variables: p, u, v 
   PHI = [None] * 3
   # convective flux vector in x-direction
   E = [None] * 3
   # convective flux vector in y-direction
   F = [None] * 3
   # diffusive flux vector
   D = [None] * 3
