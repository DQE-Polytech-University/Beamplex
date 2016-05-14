from numpy import * 
from random import *

class HelmholtzSolver:
    matrix_dimension = 0
    lyambda0 = 0
    Mtr = []
    neffect = []
    thickness = []
    refr = []
    index_max = 0

    def __init__(self, steps, lyambda, thickness, refr):
        self.matrix_dimension = steps
        self.lyambda0 = lyambda
        self.thickness = thickness
        self.refraction = refr
        
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


