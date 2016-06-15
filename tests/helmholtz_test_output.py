import unittest
import sys
from os import path
from matplotlib import pyplot as plt
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from src.helmholtz import *

class TestHelmholtzInput(unittest.TestCase):

    def testHelmholtz(self):
        
        try:
            solver = HelmholtzSolver(999, 0.85, [1, 1.05, 0.007, 0.75, 1], [3.331564442988186, 3.393487851264978, 3.6, 3.393487851264978, 3.331564442988186])
            solver.refractionMatrix()
            solver.find_neffective()
            solver.find_matrix()
            solver.coeffs(int(999 * 0.9))
            solver.find_Xforward()
            solver.find_Xrev()
            solver.Field()
            solver.Norm()
        except Exception, error:
            self.fail(error)

        error = []
        f = open("test_field_output.txt", "r")
        for x in range(1000):
            n = float(f.readline())
            solver.UTOTAL[x] = solver.UTOTAL[x] ** 2
            error.append(solver.UTOTAL[x] - n)
            error[x] = abs(error[x])
        plt.plot(solver.gridX, error)
        plt.xlabel('position, micrometers')
        plt.ylabel('error, arb. units')
        plt.savefig('error.png', format='png', dpi=100)
        plt.clf()
              
if __name__ == '__main__':
    unittest.main()
