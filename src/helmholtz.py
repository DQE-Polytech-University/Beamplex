from numpy import * 
from random import *
import numpy as np
import math

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

    def __init__(self, steps, lyambda, thickness, refr):
        self.matrix_dimension = steps
        self.lyambda0 = lyambda
        self.thickness = thickness
        self.refraction = refr
        self.deltaX = (sum((int(self.thickness[i]) for i in range(0, int(len(self.thickness)))))) / float(steps)
        self.deltaArb = self.deltaX * 2 * math.pi / self.lyambda0
        self.gridX = [i * self.deltaX for i in range(steps)]
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
        self.Mtr = np.zeros((self.matrix_dimension + 1, self.matrix_dimension + 1))
        flat = self.Mtr.ravel()
        flat[self.matrix_dimension + 1 :: self.matrix_dimension + 2] = (1/self.deltaArb) ** 2
        flat[1 :: self.matrix_dimension + 2] = (1/self.deltaArb) ** 2
        for i in range(self.matrix_dimension + 1):
            flat[0 :: self.matrix_dimension + 2] = (self.gridN[i]**2) - 2 / (self.deltaArb) ** 2
        
    def find_neffective(self):
        neffective = [x for x in range(self.matrix_dimension)]
        self.neffect = [x for x in range(self.matrix_dimension)]
        matric = linalg.eig(self.Mtr)                            #gives the eigenvalues and right eigenvectors of a square array
        neffectiv = matric[0]                                    #returns array of eigenvalues
        for k in range(self.matrix_dimension):                   #gives squared root
            self.neffect[k] = sqrt(neffectiv[k]).real            #and returns real part
    
    def find_max(self):
        neff_max = max(self.neffect)                             #gives the maximum element of index refraction matrix
        self.index_max = self.neffect.index(neff_max)
    
    def find_matrix(self):
        self.Matr = [[0]*self.matrix_dimension for x in range(self.matrix_dimension)]
        for j in range(self.matrix_dimension):
            for k in range(self.matrix_dimension):
                if j == k:
                    self.Matr[j][k] = self.gridN[j]**2 - self.neffect[self.index_max]**2 - 2/self.deltaArb**2
                elif j == k - 1 or j == k + 1:
                    self.Matr[j][k] = 1 / self.deltaArb ** 2
                else:
                    self.Matr[j][k] == 0
    
    def find_Xforward(self):
        self.X = [0 for x in range(self.matrix_dimension)]
        X[0] = aalp[self.init+1] * self.Matr[self.init][self.init]
        for j in range(1,self.matrix_dimension-self.init,1):
            X[j] = aalp[j+self.init]* X[j-1]
