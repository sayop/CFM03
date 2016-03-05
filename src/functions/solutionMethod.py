from variables import flowVars, domainVars, FDM
import numpy as np

def nondimensionalize(inputDict, idomain, iflow):
   # idomain: nondimensionlize only domain variables
   if idomain == 1:
      Lref = domainVars.Lref
      domainVars.x = domainVars.x / Lref
      domainVars.y = domainVars.y / Lref
   # iflow: nondimensionalize only flow variables
   if iflow == 1:
      Uref = flowVars.Uref
      flowVars.u = flowVars.u / Uref
      flowVars.v = flowVars.v / Uref
      flowVars.p = flowVars.p / Uref ** 2

def populateFluxVectors(inputDict):
   beta = float(inputDict['Beta'])
   imax = int(inputDict['iDim'])
   jmax = int(inputDict['jDim'])

   # Populate E vector
   FDM.E[0] = flowVars.u / beta
   FDM.E[1] = flowVars.u ** 2 + flowVars.p
   FDM.E[2] = flowVars.u * flowVars.v
   
   # Populate F vector
   FDM.F[0] = flowVars.v / beta
   FDM.F[1] = flowVars.u * flowVars.v
   FDM.F[2] = flowVars.v ** 2 + flowVars.p

   # Populate D vector
   FDM.D[0] = np.zeros((imax,jmax))
   FDM.D[1] = flowVars.u
   FDM.D[2] = flowVars.v


def updateQvector(inputDict, dt):
   imax = int(inputDict['iDim'])
   jmax = int(inputDict['jDim'])

   for n in range(3):
      # clean Q vector to store new values
      FDM.Q[n] = np.zeros((imax,jmax))
      # Add convective flux in x-direction with E vector
      FDM.Q[n] += centralFiniteDifference(-FDM.E[n],'x',1)
      # Add convective flux in y-direction with F vector
      FDM.Q[n] += centralFiniteDifference(-FDM.F[n],'y',1)
      # Add diffusive flux in x- and y-directions with D vector
      FDM.Q[n] += centralFiniteDifference(FDM.D[n],'x',2) / flowVars.Re
      FDM.Q[n] += centralFiniteDifference(FDM.D[n],'y',2) / flowVars.Re

def centralFiniteDifference(phi, direction, nOrder):
   imax = len(phi[:,0])
   jmax = len(phi[0,:])
   dx = domainVars.dx
   dy = domainVars.dy
   f = np.zeros((imax,jmax))
   # first order spatial derivative in central difference
   if nOrder == 1:
      # x-derivative
      if direction == 'x':
         for j in range(jmax-1):
            if j == 0: continue
            for i in range(imax-1):
               if i == 0: continue
               f[i,j] = 0.5 * (phi[i+1,j] - phi[i-1,j]) / dx
      # y-derivative
      if direction == 'y':
         for i in range(imax-1):
            if i == 0: continue
            for j in range(jmax-1):
               if j == 0: continue
               f[i,j] = 0.5 * (phi[i,j+1] - phi[i,j-1]) / dy
         
   # second order spatial derivative in central difference
   if nOrder == 2:
      # x-derivative
      if direction == 'x':
         for j in range(jmax-1):
            if j == 0: continue
            for i in range(imax-1):
               if i == 0: continue
               f[i,j] = (phi[i+1,j] - 2.0*phi[i,j] + phi[i-1,j]) / dx ** 2
      # y-derivative
      if direction == 'y':
         for i in range(imax-1):
            if i == 0: continue
            for j in range(jmax-1):
               if j == 0: continue
               f[i,j] = (phi[i,j+1] - 2.0*phi[i,j] + phi[i,j-1]) / dy ** 2

   return f
