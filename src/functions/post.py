import numpy as np
import matplotlib.pyplot as plt
import csv

def plotContour(x,y,phi,phiMin,phiMax,pltFile):
   from matplotlib import mlab, cm
   cmap = cm.PRGn
   
   xi, yi = np.meshgrid(x, y)
   zi = np.swapaxes(phi,1,0)

   nLevels = 20
   dPhi = (phiMax - phiMin) / nLevels
   levels = np.arange(phiMin, phiMax*1.001, dPhi)

   plt.contour(xi,yi,zi,levels)
   #plt.imshow(zi, vmin=phiMin, vmax=phiMax, extent=[x.min(), x.max(), y.min(), y.max()])
   plt.colorbar()

   plt.xscale('linear')
   plt.yscale('linear')
   plt.xlabel('x', fontsize=18)
   plt.ylabel('y', fontsize=18)
   #plt.grid(True)
   ax = plt.gca()
   xlabels = plt.getp(ax, 'xticklabels')
   ylabels = plt.getp(ax, 'yticklabels')
   plt.setp(xlabels, fontsize=15)
   plt.setp(ylabels, fontsize=15)

   fig = plt.gcf()
   fig.set_size_inches(6,5)
   plt.tight_layout()
   plt.savefig(pltFile, format='png')
   plt.close()

   print "%s DONE!!" % (pltFile)
   plt.show()
