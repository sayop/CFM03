import numpy as np
from variables import *

def initFlowVars(inputDict):
   print '# Initializing flow variables...'
   imax = int(inputDict['iDim'])
   jmax = int(inputDict['jDim'])
   flowVars.nu   = float(inputDict['nu'])
   flowVars.Uref = float(inputDict['uUp'])

   pInit = float(inputDict['pInit'])
   flowVars.p    = pInit * np.ones((imax,jmax))
   flowVars.u    = np.zeros((imax,jmax))
   flowVars.v    = np.zeros((imax,jmax))

   # Populate primitive variables in solution vector of PHI
   FDM.PHI[0] = flowVars.p
   FDM.PHI[1] = flowVars.u
   FDM.PHI[2] = flowVars.v


   # Evaluate reference Re number
   flowVars.Re = flowVars.Uref * domainVars.Lref / flowVars.nu
   print "# - Reference Reynolds number: Re = ", flowVars.Re

   updateBC(inputDict,imax,jmax)


def updateBC(inputDict,imax,jmax):
   # update boundary values in dimensionalized form
   # Left boundary
   flowVars.u[0,:] = float(inputDict['uLeft'])
   flowVars.v[0,:] = float(inputDict['vLeft'])
   # Right boundary
   flowVars.u[imax-1,:] = float(inputDict['uRight'])
   flowVars.v[imax-1,:] = float(inputDict['vRight'])
   # Bottom boundary
   flowVars.u[:,0] = float(inputDict['uBottom'])
   flowVars.v[:,0] = float(inputDict['vBottom'])
   # Upper boundary
   flowVars.u[:,jmax-1] = float(inputDict['uUp'])
   flowVars.v[:,jmax-1] = float(inputDict['vUp'])

