=============
 Problem1 - a
=============

Describe the essential steps of the solution method. Include the discretized equations and implementation of boundary conditions.

In this problem set, we are supposed to solve the Navier-Stokes equations having continuity and momentum conservation equations together. Tensor forms of continuity and momentum equations are given below:

- Continuity (incompressible)

  .. math::

     \frac{\partial u_{i}}{\partial x_{i}} = 0 

- Momentum equation:

  .. math::

     \frac{\partial u_{i}}{\partial t} + \frac{\partial u_{i}u_{j}}{\partial x_{j}} = -\frac{1}{\rho}\frac{\partial p}{\partial x_{i}} + \nu \frac{\partial}{\partial x_{j}}\left ( \frac{\partial u_{i}}{\partial x_{j}} \right )


- Non-dimensionalization of the Navier-Stokes equations

  In some cases, it is beneficial to non-dimensionalize the given transport equation because it eases the analysis of problem of interest, and also may reduce the number of parameters. The non-dimensionalized form of the Navier-Stokes equation can be achieved by first normalizing the primitive variables as followings:

  .. math::

     \tilde{u_{i}} = \frac{u_{i}}{U_{\text{ref}}},\;\;  \tilde{x_{i}} = \frac{x_{i}}{L_{\text{ref}}},\;\; \tilde{\rho}=\frac{\rho}{\rho_{\text{ref}}},\;\;\tilde{P} = \frac{P}{\rho_{\text{ref}}\, U^{2}_{\text{ref}}},\;\; \tilde{t}=\frac{t}{L/U_{\text{ref}}}

  For the final form of non-dimensionalized Navier-Stokes equation, tilda, :math:`\tilde{}`, will be dropped out for brevity and a new non-dimensional physical parameter :math:`Re` that represents the flow intertia against the fluid viscosity is introduced. Now we got:

  .. math::

     \frac{\partial u_{i}}{\partial t} + \frac{\partial u_{i}u_{j}}{\partial x_{j}} = -\frac{1}{\rho}\frac{\partial p}{\partial x_{i}} + \frac{1}{\text{Re}} \frac{\partial}{\partial x_{j}}\left ( \frac{\partial u_{i}}{\partial x_{j}} \right )

  where the Reynolds number is defined as:

  .. math::

     \text{Re} = \frac{U_{\text{ref}}L_{\text{ref}}}{\nu}


- Artificial Compressiblity Method (ACM)

  In the artificial compressibility method (ACM), the continuity equation is modified adding an unsteady term with ariticial compressiblity :math:`\beta`. To have this new form of continuity equation, an artificial equation of state that relates pressure, :math:`P`, to artificial density :math:`\tilde{\rho}` is emploeyd as following form:

  .. math::

     P = \frac{\tilde{\rho}}{\beta}


  Finally, the modified continuity equation can then be recast as:

  .. math::

     \frac{\partial P}{\partial t} + \frac{1}{\beta} \frac{\partial u_{i}}{\partial x_{i}} = 0


- Vector form of transport equations

  Rewriting the previously drived non-dimensionalized continuity and momentum equation in vector form generates a simple format that eases implementation of the numerical method. The above transport equation can be newly formed as shown below:

  .. math::

     \frac{\partial \vec{U}}{\partial t} + \frac{\partial \vec{E}}{\partial x} + \frac{\partial \vec{F}}{\partial y} = \frac{1}{\text{Re}} \left ( \frac{\partial^{2}}{\partial x^{2}} + \frac{\partial^{2}}{\partial y^{2}} \right ) \vec{U}
