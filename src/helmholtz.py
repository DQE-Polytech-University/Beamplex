from numpy import * 
from random import *
import numpy as np
import math
import cmath

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
        self.matrix_dimension = steps
        self.lyambda0 = lyambda
        self.thickness = thickness
        self.refraction = refr
        self.deltaX = (sum((float(self.thickness[i]) for i in range(0, int(len(self.thickness))))) - 0.001) / float(self.matrix_dimension) 
        self.deltaArb = float(self.deltaX * 2 * math.pi) / float(self.lyambda0)
        self.gridX = [i * self.deltaX for i in range(0, self.matrix_dimension + 1)]
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
        
    def refractionMatrix(self):
        self.Mtr = [[0]*(self.matrix_dimension + 1) for x in range(self.matrix_dimension + 1)]
        for j in range(self.matrix_dimension + 1):
            for k in range(self.matrix_dimension + 1):
                if j == k:
                    self.Mtr[j][k] = (self.gridN[j] ** 2) - 2 / (self.deltaArb) ** 2
                elif j == k - 1 or j == k + 1:
                    self.Mtr[j][k] = 1 / self.deltaArb ** 2
        
    def find_neffective(self):
        neffective = [x for x in range(self.matrix_dimension + 1)]
        self.neffect = [x for x in range(self.matrix_dimension + 1)]
        matric = linalg.eig(self.Mtr)                            #gives the eigenvalues and right eigenvectors of a square array
        neffectiv = matric[0]                                    #returns array of eigenvalues
        for k in range(self.matrix_dimension + 1):                   #gives squared root
            self.neffect[k] = (cmath.sqrt(neffectiv[k])).real            #and returns real part
    
    def find_max(self):
        neff_max = max(self.neffect)                             #gives the maximum element of index refraction matrix
        self.index_max = self.neffect.index(neff_max)
    
    def find_matrix(self):
        self.Matr = [[0]*(self.matrix_dimension + 1) for x in range(self.matrix_dimension + 1)]
        for j in range(self.matrix_dimension + 1):
            for k in range(self.matrix_dimension + 1):
                if j == k:
                    self.Matr[j][k] = self.gridN[j]**2 - self.neffect[self.index_max]**2 - 2/self.deltaArb**2
                elif j == k - 1 or j == k + 1:
                    self.Matr[j][k] = 1 / self.deltaArb ** 2
 
    def coeffs(self, initPoint):
        if isinstance(self.aalp, list) == False:
            raise TypeError("self.aalp should be a list")
        for i in range(len(self.aalp)):
            if isinstance(self.aalp[i], (int, float)) == False:
                raise TypeError("self.aalp elements should be numbers")
        if self.matrix_dimension <= 0:
            raise ValueError("self.matrix_dimension out of range")
        if len(self.aalp) == self.matrix_dimension + 1 is False:
            raise ValueError("self.aalp out of range")
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
    
    def find_Xforward(self):
        if self.init <= 0:
            raise ValueError("self.init out of range")
        if self.matrix_dimension <= 0:
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
            
    def find_Xrev(self):
        if self.init <= 0:
            raise ValueError("self.init out of range")
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
            
    def Field(self):
        self.U = [0 for x in range(self.matrix_dimension + 1)]
        for i in range(self.init + 1):
            self.U[i] = self.Y[i]
        for j in range(self.init + 1 , self.matrix_dimension + 1):
            self.U[j] = self.X[j - self.init]
            
    def Norm(self):
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
