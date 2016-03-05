import numpy as np
from solutionMethod import *
import time

def timeIntegrate(inputDict):
   tStart  = 0.0
   Cr      = float(inputDict['Courant'])
   imax    = int(inputDict['iDim'])
   jmax    = int(inputDict['jDim'])
   maxIter = int(inputDict['maxIter'])

   # start to count time for calculting computation performance
   start = time.clock()

   # Non-dimensionalize flow and domain variables
   nondimensionalize(inputDict, 1, 1)

   #
   # Time Marching:
   #
   print '=============================================='
   print '# Time integration starts at t = %s' % tStart
   print '=============================================='
   t = tStart
   nIter = 0
   while True:
      nIter += 1
      # populate flux vectors' elements with updated u, v, p
      populateFluxVectors(inputDict)


      if (nIter >= maxIter): break

