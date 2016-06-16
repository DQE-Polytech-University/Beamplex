#Mathematical modeling##
At the stage of mathematical modeling it was developed policy for numerical modeling of electromagnetic wave propagation through the waveguide of the laser nanoheterostructure of separate limitations. 
As noted above, modeling the laser nanoheterostructure the propagation of electromagnetic waves allows to calculate the optical confinement factors of the layers in the active region (quantum well), waveguide, and emitter layers.

Preliminary information about optical confinement in the emitter layers is very important when you select a construction laser nanoheterostructure
In accordance with the provisions of the concept of high-power semiconductor laser to reduce internal optical loss it is necessary to expand the waveguide layers of the laser nanoheterostructure of separate limitations.
 However, this leads to the emergence of higher orders of the mode, increase internal optical losses, the drop in differential quantum efficiency and optical power.

But if the optical confinement factor of the emitter layer for zero mode less then optical confinement factors for higher-order modes, the internal optical losses for higher order mode in highly doped emitter layers above and their generation is suppressed.

Thus, mathematical modeling allows to determine
the performance of the basic requirements for laser nanoheterostructure – the condition of generation on zero mode in the structure.

![1](https://raw.githubusercontent.com/DQE-Polytech-University/Beamplex/master/doc/eq1.png)

***β=k<SUB>0</SUB>n=2πn/λ*** -is the effective refractive index of waveguide mode. In this equation the constant of propagation of a plane wave is defined as:

![1](https://raw.githubusercontent.com/DQE-Polytech-University/Beamplex/master/doc/2.png)

![1](https://raw.githubusercontent.com/DQE-Polytech-University/Beamplex/master/doc/3.png)

Equation (1) is solved by numerical finite-difference method, which is applied to the grid of some finite period on the cross section of the waveguide.Then the differential equation (1) converted to the system of finite difference equations, defined at the nodal points.

The resulting solution of this system will cross the wave field U(x,y) in the grid nodes. Own value of this system of linear equations is the effective refractive index n of the considered mode.Thus, the transition from direct solution of the differential equation in partial derivatives to the problem in the search of the eigenvalues, which can be solved using linear algebra.


##The procedure of the sweep method:
1)The selection of the design region. On the border of the region field is equal to zero. Set
the optimum size of the computational domain to achieve more accurate result.

2) Discretization of the computational domain. Let the grid be uniform. The coordinates (x,
y) of the grid nodes using the node number (i, j) and the grid spacing in the x (Δx) and y direction (Δy):

__x=iΔx , i = 0, 1, 2, …, I + 1__

__y=jΔy , j = 0, 1, 2, …, J + 1__

Write the Hamilton operator in Cartesian coordinates and make the brackets
wave number k<SUB>0</SUB> from the second term in equation (1), in the parentheses
will the difference of the squares of the refractive index profile n(x, y) and
the effective modal refractive index n . Equation (1) will
the following:
![1](https://raw.githubusercontent.com/DQE-Polytech-University/Beamplex/master/doc/4.png)

Resort to finite difference approximations of partial derivatives. For
this decompose the function U in the neighboring nodal point in a Taylor series of the second
order:
![1](https://raw.githubusercontent.com/DQE-Polytech-University/Beamplex/master/doc/5.png)

From this system of equations we can to express the second derivative:
![1](https://raw.githubusercontent.com/DQE-Polytech-University/Beamplex/master/doc/6.png)

After discretization the computational domain, we only need the values
of the function U at the nodes. So it's nessesary to spend the next replacement:
![1](https://raw.githubusercontent.com/DQE-Polytech-University/Beamplex/master/doc/7.png)

Then, 

![1](https://raw.githubusercontent.com/DQE-Polytech-University/Beamplex/master/doc/8.png)

Now the scalar wave equation can be rewritten in discrete form:

![1](https://raw.githubusercontent.com/DQE-Polytech-University/Beamplex/master/doc/9.png)

For ease of calculation, divide both sides by k<SUP>2</SUP><SUB>0</SUB> and enter
dimensionless quantities:

__ΔX<SUP>2</SUP>=k<SUP>2</SUP><SUB>0</SUB>Δx<SUP>2</SUP>__

__ΔY<SUP>2</SUP>=k<SUP>2</SUP><SUB>0</SUB>Δy<SUP>2</SUP>__

Now rewrite the equation in the form of the characteristic equation of the matrix for i from i = 0 to i + 1 and j from j = 0 to j + 1:

![1](https://raw.githubusercontent.com/DQE-Polytech-University/Beamplex/master/doc/10.png)

where U<SUP>i</SUP><SUB>j</SUB> and n<SUP>i</SUP><SUB>j</SUB> are
normalized electric field and the refractive index in
nodal point (i, j); ΔX=k<SUB>0</SUB>Δx,
ΔY=k<SUB>0</SUB>Δy - normalized steps between the nodal
points.


Condition: at the boundaries of computational domain the field must be equal to zero:U<SUP>0</SUP><SUB>j</SUB>=U<SUP>I+1</SUP><SUB>j</SUB>=U<SUP>i</SUP><SUB>0</SUB>=U<SUP>i</SUP><SUB>J+1</SUB>=0. Thus, it is necessary to solve all equations of
region i x j .
Convert the equation to the form:

![1](https://raw.githubusercontent.com/DQE-Polytech-University/Beamplex/master/doc/11.png)

Rewrite the function U in the form of vector-column for a given x (i):


![1](https://raw.githubusercontent.com/DQE-Polytech-University/Beamplex/master/doc/12.png)

There are J of equations for the i, so it can be
wrote the matrix differential equation along x:

![1](https://raw.githubusercontent.com/DQE-Polytech-University/Beamplex/master/doc/13.png)

![1](https://raw.githubusercontent.com/DQE-Polytech-University/Beamplex/master/doc/14.png)

where I is the identity matrix of dimension J x J .
Now we can write equations (a total of I equations) in matrix form:

![1](https://raw.githubusercontent.com/DQE-Polytech-University/Beamplex/master/doc/15.png)

There A is a matrix of I x I , the elements of which are matrix J x J , and U is a vector of length I whose components are the vectors
each length of J. Then each element of the matrix A to be deployed in block J x J , 
so A becomes A matrix (IJ) x (IJ), whose elements are scalar values.
We proceed similarly with the components of the vector U.
The solution for TE mode, when an electric field E is polarized along y,
is reduced to the solution of the equations for one-dimensional case:

![1](https://raw.githubusercontent.com/DQE-Polytech-University/Beamplex/master/doc/16.png)


Thus, the refractive index does not change along y:n<SUB>i</SUB>=n<SUB>j</SUB><SUP>j</SUP> and U<SUB>i</SUB>=U<SUB>j</SUB><SUP>j</SUP>, because of j
accepts a single value.
The solution of the finite difference matrix equations are one of the
matrix methods we can find  own
number  (effective refractive index squared) n<SUP>2</SUP>, and a vector U
(profile mode).

Consequently, mathematical modeling allows to determine
the implementation of the main requirements to the laser heterostructure as a condition of
generation zero mode with extended
waveguide.

