from numpy import * 
from random import *
import numpy as np
import math
import cmath

#computes electric field in the specified number of points for certain wavelength and laser structure configuration
class HelmholtzSolver:
    matrix_dimension = 0
    lyambda0 = 0
    Mtr = []
    neffect = []
    thickness = []
    refr = []
    index_max = 0
    Matr = []
    deltaX = 0
    gridX = []
    gridN = []
    X = []
    init = 0
    aalp = []
    Y = []
    U = []
    U1 = []
    UtotalNorm1 = []
    elemk = []
    UTOTAL = []
    
    def __init__(self, steps, lyambda, thickness, refr):
        if isinstance(steps, (int, float)) == False or isinstance(lyambda, (int, float)) == False or isinstance(thickness, list) == False or isinstance(refr, list) == False:
            raise TypeError("type mismatch")
        if steps < 20:
            raise ValueError("wrong grid nodes number")
        if lyambda < 0.85 or lyambda > 1.5:
            raise ValueError("wavelength out of range")
        for i in range(5):
            if isinstance(thickness[i], (int, float)) == False or isinstance(refr[i], (int, float)) == False:
                raise TypeError("type mismatch")
            if thickness[i] <= 0 or refr[i] <= 1:
                raise ValueError("thickness out of range")
                
        self.matrix_dimension = steps
        self.lyambda0 = lyambda
        self.thickness = thickness
        self.refraction = refr
        self.deltaX = (sum((float(self.thickness[i]) for i in range(0, int(len(self.thickness))))) - 0.001) / float(self.matrix_dimension) 
        self.deltaArb = float(self.deltaX * 2 * math.pi) / float(self.lyambda0)
        self.gridX = [i * self.deltaX for i in range(0, self.matrix_dimension + 1)]
        self.gridN = []
        for i in self.gridX:
            if 0 <= i and i < self.thickness[0]:
                self.gridN.append(self.refraction[0])
            if self.thickness[0] <= i and i < self.thickness[0] + self.thickness[1]:
                self.gridN.append(self.refraction[1])
            if self.thickness[0] + self.thickness[1] <= i and i < self.thickness[0] + self.thickness[1] + self.thickness[2]:
                self.gridN.append(self.refraction[2])
            if self.thickness[0] + self.thickness[1] + self.thickness[2] <= i and i < self.thickness[0] + self.thickness[1] + self.thickness[2] + self.thickness[3]:
                self.gridN.append(self.refraction[3])
            if self.thickness[0] + self.thickness[1] + self.thickness[2] + self.thickness[3] <= i and i < self.thickness[0] + self.thickness[1] + self.thickness[2] + self.thickness[3] + self.thickness[4]:
                self.gridN.append(self.refraction[4])

    #composes a matrix for computation of maximal effective refractive index     
    def refractionMatrix(self):
        if isinstance(self.gridN, list) == False or isinstance(self.matrix_dimension, int) == False or isinstance(self.deltaArb, (int, float)) == False:
            raise TypeError("type mismatch")
        if self.matrix_dimension < 20:
            raise ValueError("wrong grid nodes number")
        if self.deltaArb <= 0:
            raise ValueError("wrong deltaArb value")
        if len(self.gridN) != self.matrix_dimension + 1:
            raise IndexError("wrong nodes number in the refractive index grid")
        for i in range(self.matrix_dimension + 1):
            if isinstance(self.gridN[i], (int, float)) == False:
                raise TypeError("type mismatch")
            if self.gridN[i] <= 1:
                raise ValueError("wrong refractive index value")
                
        self.Mtr = [[0]*(self.matrix_dimension + 1) for x in range(self.matrix_dimension + 1)]
        for j in range(self.matrix_dimension + 1):
            for k in range(self.matrix_dimension + 1):
                if j == k:
                    self.Mtr[j][k] = (self.gridN[j] ** 2) - 2 / (self.deltaArb) ** 2
                elif j == k - 1 or j == k + 1:
                    self.Mtr[j][k] = 1 / self.deltaArb ** 2

    #finds maximal effective refractive index as a maximal real eigenvalue of Mtr matrix     
    def find_neffective(self):
        if isinstance(self.matrix_dimension, int) == False or isinstance(self.Mtr, list) == False:
            raise TypeError("type mismatch")
        if self.matrix_dimension < 20:
            raise ValueError("wrong grid nodes number")
        if len(self.Mtr) != self.matrix_dimension + 1:
            raise IndexError("wrong dimension of the refractive index matrix")
        for i in range(self.matrix_dimension + 1):
            if isinstance(self.Mtr[i], list) == False:
                raise TypeError("type mismatch")
            if len(self.Mtr[i]) != self.matrix_dimension + 1:
                raise IndexError("wrong dimension of the refractive index matrix")
            for k in range(self.matrix_dimension + 1):
                if isinstance(self.Mtr[i][k], (int, float)) == False:
                    raise TypeError("type mismatch")
                    
        neffective = [x for x in range(self.matrix_dimension + 1)]
        self.neffect = [x for x in range(self.matrix_dimension + 1)]
        matric = linalg.eig(self.Mtr)                            
        neffectiv = matric[0]                                    
        for k in range(self.matrix_dimension + 1):                   
            self.neffect[k] = (cmath.sqrt(neffectiv[k])).real            
    
        neff_max = max(self.neffect)                             
        self.index_max = self.neffect.index(neff_max)

    #composes a matrix for tridiagonal matrix algorithm
    def find_matrix(self):
        if isinstance(self.matrix_dimension, int) == False or isinstance(self.gridN, list) == False:
            raise TypeError("type mismatch")
        if isinstance(self.neffect[self.index_max], (int, float)) == False or isinstance(self.deltaArb, (int, float)) == False:
            raise TypeError("type mismatch")
        if self.matrix_dimension < 20:
            raise ValueError("wrong grid nodes number")
        for i in range(self.matrix_dimension + 1):
            if isinstance(self.gridN[i], (int, float)) == False:
                raise TypeError("type mismatch")
            if self.gridN[i] <= 1:
                raise ValueError("wrong refractive index value")
        if self.neffect[self.index_max] <= 1:
            raise ValueError("wrong refractive index value")
        if self.deltaArb <= 0:
            raise ValueError("wrong deltaArb value")
            
        self.Matr = [[0]*(self.matrix_dimension + 1) for x in range(self.matrix_dimension + 1)]
        for j in range(self.matrix_dimension + 1):
            for k in range(self.matrix_dimension + 1):
                if j == k:
                    self.Matr[j][k] = self.gridN[j]**2 - self.neffect[self.index_max]**2 - 2/self.deltaArb**2
                elif j == k - 1 or j == k + 1:
                    self.Matr[j][k] = 1 / self.deltaArb ** 2

    #finds coefficients for tridiagonal matrix algorithm
    def coeffs(self, initPoint):
        if isinstance(self.matrix_dimension, int) == False or isinstance(initPoint, int) == False:
            raise TypeError("type mismatch")
        if initPoint <= 0 or initPoint >= self.matrix_dimension:
            raise ValueError("wrong initial point")
        if self.matrix_dimension <= 20:
            raise ValueError("self.matrix_dimension out of range")
        for j in range(self.matrix_dimension + 1):
            for k in range(self.matrix_dimension + 1):
                if isinstance(self.Matr[j][k], (int, float)) == False:
                    raise TypeError("self.Matr[j][k] should be a number")
        if self.init is None:
            raise ValueError("self.init is undefined")
        if self.matrix_dimension is None:
            raise ValueError("self.matrix_dimension is undefined")
        if self.aalp is None:
            raise ValueError("self.aalp is undefined")
        
        self.init = initPoint
        self.Matr[self.init][self.init] = 1
        self.aalp = [0 for x in range(self.matrix_dimension + 1)]
        self.aalp[self.matrix_dimension] = float(-self.Matr[self.matrix_dimension][self.matrix_dimension - 1]) / float(self.Matr[self.matrix_dimension][self.matrix_dimension])
        for i in range(self.matrix_dimension - 1, self.init, -1):
            self.aalp[i] = float(-self.Matr[i][i-1]) / float(self.Matr[i][i] + self.Matr[i][i+1] * self.aalp[i+1])
            
    #forward sweep of tridiagonal matrix algorithm
    def find_Xforward(self):
        if isinstance(self.init, int) == False:
            raise TypeError("type mismatch")
        if self.init <= 0 or self.init >= self.matrix_dimension:
            raise ValueError("self.init out of range")
        if self.matrix_dimension <= 20:
            raise ValueError("self.matrix_dimension out of range")
        if isinstance(self.Matr, list) == False:
            raise TypeError("self.Y should be a list")
        for j in range(self.matrix_dimension + 1):
            for k in range(self.matrix_dimension + 1):
                if isinstance(self.Matr[j][k], (int, float)) == False:
                    raise TypeError("self.Matr[j][k] should be a number")
        if self.init is None:
            raise ValueError("self.init is undefined")
        if self.matrix_dimension is None:
            raise ValueError("self.matrix_dimension is undefined")

        self.X = [0 for x in range(self.matrix_dimension - self.init + 1)]
        self.X[0] = self.aalp[self.init+1] * self.Matr[self.init][self.init]
        for j in range(1,self.matrix_dimension-self.init +1):
            self.X[j] = self.aalp[j+self.init]* self.X[j-1]

    #reverse sweep of tridiagonal matrix algorithm        
    def find_Xrev(self):
        if isinstance(self.init, int) == False:
            raise TypeError("type mismatch")
        if self.init <= 0 or self.init >= self.matrix_dimension:
            raise ValueError("self.init out of range")
        if self.matrix_dimension <= 20:
            raise ValueError("self.matrix_dimension out of range")
        if isinstance(self.Matr, list) == False:
            raise TypeError("self.Y should be a list")
        for j in range(self.matrix_dimension + 1):
            for k in range(self.matrix_dimension + 1):
                if isinstance(self.Matr[j][k], (int, float)) == False:
                    raise TypeError("self.Matr[j][k] should be a number")
        if self.init is None:
            raise ValueError("self.init is undefined")
        
        self.Y = [0 for x in range(self.init + 2)]
        self.Y[self.init ] =  self.X[0]
        self.Y[self.init + 1] = self.X[1]
        for j in range(self.init - 1,-1,-1):
            self.Y[j] = float((-1/self.Matr[j+1][j])) * float((self.Matr[j+1][j+1] * self.Y[j+1] + self.Matr[j+1][j+2] * self.Y[j+2]))

    #composes final solution        
    def Field(self):
        if isinstance(self.matrix_dimension, int) == False or isinstance(self.X, list) == False or isinstance(self.Y, list) == False:
            raise TypeError("type mismatch")
        if self.matrix_dimension < 20:
            raise ValueError("wrong grid nodes number")
        if len(self.X) != self.matrix_dimension - self.init + 1:
            raise IndexError("wrong dimension")
        if len(self.Y) != self.init + 2:
            raise IndexError("wrong dimension")
        for i in range(self.matrix_dimension - self.init + 1):
            if isinstance(self.X[i], (int, float)) == False:
                raise TypeError("type mismatch")
        for i in range(self.init + 2):
            if isinstance(self.Y[i], (int, float)) == False:
                raise TypeError("type mismatch")
        self.U = [0 for x in range(self.matrix_dimension + 1)]
        for i in range(self.init + 1):
            self.U[i] = self.Y[i]
        for j in range(self.init + 1 , self.matrix_dimension + 1):
            self.U[j] = self.X[j - self.init]

    #normalizes the solution        
    def Norm(self):
        if isinstance(self.matrix_dimension, int) == False or isinstance(self.U, list) == False or isinstance(self.deltaX, (int, float)) == False:
            raise TypeError("type mismatch")
        if self.deltaX <= 0:
            raise ValueError("wrong deltaX")
        if len(self.U) != self.matrix_dimension + 1:
            raise IndexError("wrong dimension")
        for i in range(self.matrix_dimension + 1):
            if isinstance(self.U[i], (int, float)) == False:
                raise TypeError("type mismatch")
                
        for i in range(self.matrix_dimension + 1):
            self.U1.append(math.fabs(self.U[i]))
            Umax = - max(self.U1)            
        for j in range(self.matrix_dimension + 1):
            q = self.U[j] / Umax
            self.UtotalNorm1.append(q)
        for k in range(self.matrix_dimension + 1):
            elem = float((self.UtotalNorm1[k])**2) * self.deltaX
            self.elemk.append(elem) 
            IntU = np.sum(self.elemk)
        for n in range(self.matrix_dimension + 1):
            w = float(self.UtotalNorm1[n]) / float(math.sqrt(IntU))
            self.UTOTAL.append(w)
