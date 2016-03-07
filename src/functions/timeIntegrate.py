import numpy as np
from solutionMethod import *
from post import *
import time

def timeIntegrate(inputDict):
   tStart  = 0.0
   Cr      = float(inputDict['Courant'])
   imax    = int(inputDict['iDim'])
   jmax    = int(inputDict['jDim'])
   maxIter = int(inputDict['maxIter'])
   beta    = float(inputDict['Beta'])
   residualMin = float(inputDict['residualMin'])
   nIterWrite  = int(inputDict['nIterWrite'])

   # initialize residual variables for p, u, and v
   residualInit = np.zeros(3)
   residual     = np.zeros(3)

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
      dt = updateTimeStep(inputDict)

      # update Q vector for explicit time integration
      updateQvector(inputDict, dt)

      # update primative vector U
      for j in range(jmax):
         for i in range(imax):
            flowVars.p[i,j] += dt * FDM.Q[0][i,j]
            flowVars.u[i,j] += dt * FDM.Q[1][i,j]
            flowVars.v[i,j] += dt * FDM.Q[2][i,j]

      # compute residual value to verify convergence
      residual = computeResidual(imax, jmax, dt, FDM.Q)
      if nIter == 1:
         residualInit = residual
      # only track residual for u-velocity
      resNorm = residual[1] / residualInit[1]

      t += dt
      MachX, MachY = computeMaximumMach(imax, jmax, beta)
      print "|- nIter = %s" % nIter, ", dt = %.4f" % dt, ", Maximum Mach_x = %.4f" % MachX, ", Maximum Mach_y = %.4f" % MachY, ", u-residual = %.4f" % resNorm

      if (nIter % nIterWrite == 0):
         plotStreamLine(domainVars.x, domainVars.y, flowVars.u, flowVars.v, nIter)

      if (nIter >= maxIter or resNorm <= residualMin): break

   # Dimensionalize flow and domain variables
   dimensionalize(inputDict, 1, 1)

   # plot contour of artificial pressure
   #pltFile = 'p_contour.png'
   #phi = flowVars.p
   #phiMin = phi.min()
   #phiMax = phi.max()
   #plotContour(domainVars.x, domainVars.y, phi, phiMin, phiMax, pltFile)

   # plot contour of velocity magnitude
   pltFile = 'Umag_contour.png'
   flowVars.Umag = np.sqrt(flowVars.u ** 2 + flowVars.v ** 2)
   phi = flowVars.Umag
   phiMin = phi.min()
   phiMax = phi.max()
   plotContour(domainVars.x, domainVars.y, phi, phiMin, phiMax, pltFile)

   # plot streamline of velocity
   plotStreamLine(domainVars.x, domainVars.y, flowVars.u, flowVars.v, nIter)
