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
      
      # find dt with stability condition
      dt = 0.001
      t += dt
      print "|- nIter = ", nIter, " dt = ", dt

      # update Q vector for explicit time integration
      updateQvector(inputDict, dt)

      # update primative vector U
      for n in range(3):
         for j in range(jmax-1):
            if j == 0: continue
            for i in range(imax-1):
               if i == 0: continue
               FDM.PHI[n][i,j] += dt * FDM.Q[n][i,j]

      #print FDM.PHI[1]
      print flowVars.u

      if (nIter >= maxIter): break

