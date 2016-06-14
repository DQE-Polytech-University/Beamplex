from jsonloader import *
from refraction import *
from helmholtz import *
from laserstructure import *
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filePath', type = str, nargs = '?')
parser.add_argument('steps', type = int, nargs = '?')
namespace = parser.parse_args(sys.argv[1:])
filePath = namespace.filePath
steps = namespace.steps

loader1 = JSONLoader(filePath)
loader1.loadJSON()
laser1 = Laser(loader1.parseJSONData())

calc1 = RefractionCalc(laser1.wavelength, laser1.concentration)
calc1.computeRefraction()

solver1 = HelmholtzSolver(steps, laser1.wavelength, laser1.thickness, calc1.refraction)
solver1.refractionMatrix()
solver1.find_neffective()
solver1.find_matrix()
solver1.coeffs(int(steps * 0.9))
solver1.find_Xforward()
solver1.find_Xrev()
solver1.Field()
solver1.Norm()

laser1.gridX = solver1.gridX
laser1.gridN = solver1.gridN
laser1.field = solver1.UTOTAL
laser1.plotRefraction()
laser1.plotField()
