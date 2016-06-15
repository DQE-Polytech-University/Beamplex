import unittest
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from src.helmholtz import *

class TestHelmholtzInput(unittest.TestCase):

    def correctSolver(self, function):
        solver = HelmholtzSolver(100, 0.85, [0.1, 0.1, 0.1, 0.1, 0.1], [3, 3, 3, 3, 3])
        if function == "init" or function == "refractionMatrix":
            pass
        elif function == "find_neffective":
            solver.refractionMatrix()
        elif function == "find_matrix":
            solver.refractionMatrix()
            solver.find_neffective()
        elif function == "coeffs":
            solver.refractionMatrix()
            solver.find_neffective()
            solver.find_matrix()
        elif function == "find_Xforward":
            solver.refractionMatrix()
            solver.find_neffective()
            solver.find_matrix()
            solver.coeffs(95)
        elif function == "find_Xrev":
            solver.refractionMatrix()
            solver.find_neffective()
            solver.find_matrix()
            solver.coeffs(95)
            solver.find_Xforward()
        elif function == "Field":
            solver.refractionMatrix()
            solver.find_neffective()
            solver.find_matrix()
            solver.coeffs(95)
            solver.find_Xforward()
            solver.find_Xrev()
        elif function == "Norm":
            solver.refractionMatrix()
            solver.find_neffective()
            solver.find_matrix()
            solver.coeffs(95)
            solver.find_Xforward()
            solver.find_Xrev()
            solver.Field()
        return solver

    def testInitCorrect(self):
        try:
            self.solver = self.correctSolver("init")
        except Exception, error:
            self.fail(error)

    def testInitSteps(self):
        self.assertRaises(TypeError, HelmholtzSolver, '100', 0.85, [0.1, 0.1, 0.1, 0.1, 0.1], [3, 3, 3, 3, 3])
        self.assertRaises(TypeError, HelmholtzSolver, None, 0.85, [0.1, 0.1, 0.1, 0.1, 0.1], [3, 3, 3, 3, 3])
        self.assertRaises(ValueError, HelmholtzSolver, -100, 0.85, [0.1, 0.1, 0.1, 0.1, 0.1], [3, 3, 3, 3, 3])
    
    def testInitLambda(self):
        self.assertRaises(TypeError, HelmholtzSolver, 100, '0.85', [0.1, 0.1, 0.1, 0.1, 0.1], [3, 3, 3, 3, 3])
        self.assertRaises(TypeError, HelmholtzSolver, 100, None, [0.1, 0.1, 0.1, 0.1, 0.1], [3, 3, 3, 3, 3])
        self.assertRaises(ValueError, HelmholtzSolver, 100, 0.5, [0.1, 0.1, 0.1, 0.1, 0.1], [3, 3, 3, 3, 3])
        self.assertRaises(ValueError, HelmholtzSolver, 100, 2, [0.1, 0.1, 0.1, 0.1, 0.1], [3, 3, 3, 3, 3])
    
    def testInitThickness(self):
        self.assertRaises(TypeError, HelmholtzSolver, 100, 0.85, '[0.1, 0.1, 0.1, 0.1, 0.1]', [3, 3, 3, 3, 3])
        self.assertRaises(TypeError, HelmholtzSolver, 100, 0.85, None, [3, 3, 3, 3, 3])
        self.assertRaises(TypeError, HelmholtzSolver, 100, 0.85, [0.1, '0.1', 0.1, 0.1, 0.1], [3, 3, 3, 3, 3])
        self.assertRaises(ValueError, HelmholtzSolver, 100, 0.85, [-0.1, 0.1, 0.1, 0.1, 0.1], [3, 3, 3, 3, 3])

    def testInitRefraction(self):
        self.assertRaises(TypeError, HelmholtzSolver, 100, 0.85, [0.1, 0.1, 0.1, 0.1, 0.1], '[3, 3, 3, 3, 3]')
        self.assertRaises(TypeError, HelmholtzSolver, 100, 0.85, [0.1, 0.1, 0.1, 0.1, 0.1], None)
        self.assertRaises(TypeError, HelmholtzSolver, 100, 0.85, [0.1, 0.1, 0.1, 0.1, 0.1], ['3', 3, 3, 3, 3])
        self.assertRaises(ValueError, HelmholtzSolver, 100, 0.85, [0.1, 0.1, 0.1, 0.1, 0.1], [-3, 3, 3, 3, 3])

    def testRefractionMatrix(self):
        self.solver1 = self.correctSolver("refractionMatrix")
        self.solver1.gridN = "123"
        self.assertRaises(TypeError, self.solver1.refractionMatrix)

        self.solver2 = self.correctSolver("refractionMatrix")
        self.solver2.matrix_dimension = "999"
        self.assertRaises(TypeError, self.solver2.refractionMatrix)

        self.solver3 = self.correctSolver("refractionMatrix")
        self.solver3.deltaArb = "999"
        self.assertRaises(TypeError, self.solver3.refractionMatrix)

        self.solver4 = self.correctSolver("refractionMatrix")
        self.solver4.matrix_dimension = 10
        self.assertRaises(ValueError, self.solver4.refractionMatrix)

        self.solver5 = self.correctSolver("refractionMatrix")
        self.solver5.matrix_dimension = 10
        self.assertRaises(ValueError, self.solver5.refractionMatrix)

        self.solver6 = self.correctSolver("refractionMatrix")
        self.solver6.deltaArb = 0
        self.assertRaises(ValueError, self.solver6.refractionMatrix)

        self.solver7 = self.correctSolver("refractionMatrix")
        self.solver7.matrix_dimension = 1000
        self.assertRaises(IndexError, self.solver7.refractionMatrix)

        self.solver8 = self.correctSolver("refractionMatrix")
        self.solver8.gridN[5] = "123"
        self.assertRaises(TypeError, self.solver8.refractionMatrix)

        self.solver9 = self.correctSolver("refractionMatrix")
        self.solver9.gridN[5] = 0.5
        self.assertRaises(ValueError, self.solver9.refractionMatrix)

    def testFindNeffective(self):
        self.solver1 = self.correctSolver("init")
        self.solver1.matrix_dimension = "999"
        self.assertRaises(TypeError, self.solver1.find_neffective)

        self.solver2 = self.correctSolver("find_neffective")
        self.solver2.Mtr = "999"
        self.assertRaises(TypeError, self.solver2.find_neffective)

        self.solver3 = self.correctSolver("find_neffective")
        self.solver3.matrix_dimension = 10
        self.assertRaises(ValueError, self.solver3.find_neffective)

        self.solver4 = self.correctSolver("find_neffective")
        self.solver4.matrix_dimension = 1000
        self.assertRaises(IndexError, self.solver4.find_neffective)

        self.solver5 = self.correctSolver("find_neffective")
        self.solver5.Mtr[0] = "[1, 2, 3]"
        self.assertRaises(TypeError, self.solver5.find_neffective)

        self.solver6 = self.correctSolver("find_neffective")
        self.solver6.Mtr[0] = [1, 2, 3]
        self.assertRaises(IndexError, self.solver6.find_neffective)

        self.solver7 = self.correctSolver("find_neffective")
        self.solver7.Mtr[0][0] = "1"
        self.assertRaises(TypeError, self.solver7.find_neffective)

    def testFindMatrix(self):
        self.solver1 = self.correctSolver("find_matrix")
        self.solver1.matrix_dimension = "999"
        self.assertRaises(TypeError, self.solver1.find_matrix)

        self.solver2 = self.correctSolver("find_matrix")
        self.solver2.gridN = "123"
        self.assertRaises(TypeError, self.solver2.find_matrix)

        self.solver3 = self.correctSolver("find_matrix")
        self.solver3.neffect[self.solver3.index_max] = "999"
        self.assertRaises(TypeError, self.solver3.find_matrix)

        self.solver4 = self.correctSolver("find_matrix")
        self.solver4.deltaArb = "999"
        self.assertRaises(TypeError, self.solver4.find_matrix)

        self.solver5 = self.correctSolver("find_matrix")
        self.solver5.matrix_dimension = 10
        self.assertRaises(ValueError, self.solver5.find_matrix)
        
        self.solver5 = self.correctSolver("find_matrix")
        self.solver5.gridN[5] = "123"
        self.assertRaises(TypeError, self.solver5.find_matrix)

        self.solver6 = self.correctSolver("find_matrix")
        self.solver6.gridN[5] = 0.5
        self.assertRaises(ValueError, self.solver6.find_matrix)

        self.solver7 = self.correctSolver("find_matrix")
        self.solver7.neffect[self.solver7.index_max] = 0.5
        self.assertRaises(ValueError, self.solver7.find_matrix)

        self.solver8 = self.correctSolver("find_matrix")
        self.solver8.deltaArb = 0
        self.assertRaises(ValueError, self.solver8.find_matrix)
        
    def testCoeffs(self):
        self.solver1 = self.correctSolver("coeffs")
        self.solver1.matrix_dimension = "999"
        self.assertRaises(TypeError, self.solver1.coeffs, 95)

        self.solver2 = self.correctSolver("coeffs")
        self.solver2.matrix_dimension = 10
        self.assertRaises(ValueError, self.solver2.coeffs, 95)

        self.solver3 = self.correctSolver("coeffs")
        self.assertRaises(TypeError, self.solver3.coeffs, "95")

        self.solver4 = self.correctSolver("coeffs")
        self.assertRaises(ValueError, self.solver4.coeffs, -1)

        self.solver5 = self.correctSolver("coeffs")
        self.solver5.matrix_dimension = 1000
        self.assertRaises(IndexError, self.solver5.coeffs, 95)

        self.solver6 = self.correctSolver("coeffs")
        self.solver6.Matr[0] = "[1, 2, 3]"
        self.assertRaises(TypeError, self.solver6.coeffs, 95)

        self.solver7 = self.correctSolver("coeffs")
        self.solver7.Matr[0] = [1, 2, 3]
        self.assertRaises(IndexError, self.solver7.coeffs, 95)

        self.solver8 = self.correctSolver("coeffs")
        self.solver8.Matr[0][0] = "1"
        self.assertRaises(TypeError, self.solver8.coeffs, 95)

    def testFindXForward(self):
        self.solver1 = self.correctSolver("find_Xforward")
        self.solver1.matrix_dimension = "999"
        self.assertRaises(TypeError, self.solver1.find_Xforward)

        self.solver2 = self.correctSolver("find_Xforward")
        self.solver2.matrix_dimension = 10
        self.assertRaises(ValueError, self.solver2.find_Xforward)

        self.solver3 = self.correctSolver("find_Xforward")
        self.solver3.init = "95"
        self.assertRaises(TypeError, self.solver3.find_Xforward)

        self.solver4 = self.correctSolver("find_Xforward")
        self.solver4.init = -1
        self.assertRaises(ValueError, self.solver4.find_Xforward)

        self.solver5 = self.correctSolver("find_Xforward")
        self.solver5.matrix_dimension = 1000
        self.assertRaises(IndexError, self.solver5.find_Xforward)

        self.solver6 = self.correctSolver("find_Xforward")
        self.solver6.Matr[0] = "[1, 2, 3]"
        self.assertRaises(TypeError, self.solver6.find_Xforward)

        self.solver7 = self.correctSolver("find_Xforward")
        self.solver7.Matr[0] = [1, 2, 3]
        self.assertRaises(IndexError, self.solver7.find_Xforward)

        self.solver8 = self.correctSolver("find_Xforward")
        self.solver8.Matr[0][0] = "1"
        self.assertRaises(TypeError, self.solver8.find_Xforward)

    def testFindXRev(self):
        self.solver1 = self.correctSolver("find_Xrev")
        self.solver1.matrix_dimension = "999"
        self.assertRaises(TypeError, self.solver1.find_Xrev)

        self.solver2 = self.correctSolver("find_Xrev")
        self.solver2.matrix_dimension = 10
        self.assertRaises(ValueError, self.solver2.find_Xrev)

        self.solver3 = self.correctSolver("find_Xrev")
        self.solver3.init = "95"
        self.assertRaises(TypeError, self.solver3.find_Xrev)

        self.solver4 = self.correctSolver("find_Xrev")
        self.solver4.init = -1
        self.assertRaises(ValueError, self.solver4.find_Xrev)

        self.solver5 = self.correctSolver("find_Xrev")
        self.solver5.matrix_dimension = 1000
        self.assertRaises(IndexError, self.solver5.find_Xrev)

        self.solver6 = self.correctSolver("find_Xrev")
        self.solver6.Matr[0] = "[1, 2, 3]"
        self.assertRaises(TypeError, self.solver6.find_Xrev)

        self.solver7 = self.correctSolver("find_Xrev")
        self.solver7.Matr[0] = [1, 2, 3]
        self.assertRaises(IndexError, self.solver7.find_Xrev)

        self.solver8 = self.correctSolver("find_Xrev")
        self.solver8.Matr[0][0] = "1"
        self.assertRaises(TypeError, self.solver8.find_Xrev)

    def testField(self):
        self.solver1 = self.correctSolver("Field")
        self.solver1.matrix_dimension = "999"
        self.assertRaises(TypeError, self.solver1.Field)

        self.solver2 = self.correctSolver("Field")
        self.solver2.X = "999"
        self.assertRaises(TypeError, self.solver2.Field)

        self.solver3 = self.correctSolver("Field")
        self.solver3.Y = "999"
        self.assertRaises(TypeError, self.solver3.Field)

        self.solver4 = self.correctSolver("Field")
        self.solver4.matrix_dimension = 10
        self.assertRaises(ValueError, self.solver4.Field)

        self.solver5 = self.correctSolver("Field")
        self.solver5.X = []
        self.assertRaises(IndexError, self.solver5.Field)

        self.solver6 = self.correctSolver("Field")
        self.solver6.Y = []
        self.assertRaises(IndexError, self.solver6.Field)

        self.solver7 = self.correctSolver("Field")
        self.solver7.X[0] = "1"
        self.assertRaises(TypeError, self.solver7.Field)

        self.solver8 = self.correctSolver("Field")
        self.solver8.Y[0] = "1"
        self.assertRaises(TypeError, self.solver8.Field)

    def testNorm(self):
        self.solver1 = self.correctSolver("Norm")
        self.solver1.matrix_dimension = "999"
        self.assertRaises(TypeError, self.solver1.Norm)

        self.solver2 = self.correctSolver("Norm")
        self.solver2.U = "999"
        self.assertRaises(TypeError, self.solver2.Norm)

        self.solver3 = self.correctSolver("Norm")
        self.solver3.deltaX = "999"
        self.assertRaises(TypeError, self.solver3.Norm)

        self.solver4 = self.correctSolver("Norm")
        self.solver4.deltaX = 0
        self.assertRaises(ValueError, self.solver4.Norm)

        self.solver5 = self.correctSolver("Norm")
        self.solver5.U = []
        self.assertRaises(IndexError, self.solver5.Norm)

        self.solver5 = self.correctSolver("Norm")
        self.solver5.U[0] = "1"
        self.assertRaises(TypeError, self.solver5.Norm)
              
if __name__ == '__main__':
    unittest.main()
