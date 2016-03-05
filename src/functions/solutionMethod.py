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
   FDM.D[1] = flowVars.u / flowVars.Re
   FDM.D[2] = flowVars.v / flowVars.Re

