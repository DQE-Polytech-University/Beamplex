##Mathematical modeling##
**At the stage of mathematical modeling it was developed policy for numerical modeling of electromagnetic wave propagation through the waveguide of the laser nanoheterostructure of separate limitations. 
As noted above, modeling the laser nanoheterostructure the propagation of electromagnetic waves allows to calculate the optical confinement factors of the layers in the active region (quantum well), waveguide, and emitter layers.**

**Preliminary information about optical confinement in the emitter layers is very important when you select a construction laser nanoheterostructure
In accordance with the provisions of the concept of high-power semiconductor laser to reduce internal optical loss it is necessary to expand the waveguide layers of the laser nanoheterostructure of separate limitations.
 However, this leads to the emergence of higher orders of the mode, increase internal optical losses, the drop in differential quantum efficiency and optical power.**

**But if the optical confinement factor of the emitter layer for zero mode less then optical confinement factors for higher-order modes, the internal optical losses for higher order mode in highly doped emitter layers above and their generation is suppressed.**

**Thus, mathematical modeling allows to determine
the performance of the basic requirements for laser nanoheterostructure – the condition of generation on zero mode in the structure.**

![1](https://raw.githubusercontent.com/DQE-Polytech-University/Beamplex/master/doc/eq1.png)

***β=k<SUB>0</SUB>n=2πn/λ*** **-is the effective refractive index of waveguide mode. In this equation the constant of propagation of a plane wave is defined as:**

![1](https://raw.githubusercontent.com/DQE-Polytech-University/Beamplex/master/doc/eq2.png)

![1](https://raw.githubusercontent.com/DQE-Polytech-University/Beamplex/master/doc/eq3.png)

**Equation (1) is solved by numerical finite-difference method, which is applied to the grid of some finite period on the cross section of the waveguide.Then the differential equation (1) converted to the system of finite difference equations, defined at the nodal points.**

**The resulting solution of this system will cross the wave field U(x,y) in the grid nodes. Own value of this system of linear equations is the effective refractive index n of the considered mode.Thus, the transition from direct solution of the differential equation in partial derivatives to the problem in the search of the eigenvalues, which can be solved using linear algebra.**
