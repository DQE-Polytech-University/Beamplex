import matplotlib.pyplot as plt

class Laser:

    refraction = []
    field = []
    gridX = []
    gridN = []
    field = []

    def __init__(self, (wavelength, layersNumber, concentration, thickness)):

        if isinstance(wavelength, (int, float)) == False:
            raise TypeError("wavelength should be a number")
        if isinstance(layersNumber, (int, float)) == False:
            raise TypeError("layersNumber should be a number")
        if isinstance(concentration, list) == False:
            raise TypeError("concentration should be a list")
        if isinstance( thickness, (list)) == False:
            raise TypeError("thickness should be a list")
        for i in range(layersNumber):
            if isinstance(concentration[i], (int, float)) == False or isinstance( thickness[i], (int, float)) == False:
                raise TypeError("concentration and thickness elements should be numbers")

        if wavelength is None:
            raise ValueError("wavelength is undefined")
        if layersNumber is None:
            raise ValueError("layersNumber is undefined")
        if concentration is None:
            raise ValueError("concentration is undefined")
        if thickness is None:
            raise ValueError("thickness is undefined")
        
        if wavelength < 0.85 or wavelength > 1.5:
            raise ValueError("wavelength out of range")
        
        self.wavelength = wavelength
        self.layersNumber = layersNumber
        self.concentration = concentration
        self.thickness = thickness


    def plotRefraction(self):
        
        plt.plot(self.gridX, self.gridN)
        plt.xlabel('position, micrometers')
        plt.ylabel('refraction index, arb. units')
        plt.title('Refraction Index Profile')
        plt.savefig('refraction.png', format='png', dpi=100)
        plt.clf()

        refractionFile = open("refraction.txt", "w")
        for i in range(len(self.gridN)):
            refractionFile.write(str(self.gridX[i]) + ": " + str(self.gridN[i]) + "\n")
        refractionFile.close()
        
    def plotField(self):
        
        for i in range(len(self.field)):
            self.field[i] = self.field[i] ** 2
        plt.plot(self.gridX, self.field)
        plt.xlabel('position, micrometers')
        plt.ylabel('electric field, arb. units')
        plt.title('Electric field in laser structure')
        plt.savefig('field.png', format='png', dpi=100)
        plt.clf()

        fieldFile = open("field.txt", "w")
        for i in range(len(self.gridN)):
            fieldFile.write(str(self.gridX[i]) + ": " + str(self.field[i]) + "\n")
        fieldFile.close()
