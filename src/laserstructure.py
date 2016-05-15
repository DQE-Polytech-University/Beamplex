import matplotlib.pyplot as plt

class Laser:

    laserRefraction = []
    laserField = []

    def __init__(self, wavelength, layersNumber, concentration, thickness):
        self.laserWavelength = wavelength
        self.laserLayersNumber = layersNumber
        self.laserConcentration = concentration
        self.laserThickness = thickness
    
    def plotRefraction(self):
        coord = [0]
        sum = 0
        refr = [self.laserRefraction[0]]
        for i in range(self.laserLayersNumber):
            sum += self.laserThickness[i]
            coord.append(sum-0.0001)
            coord.append(sum)
            refr.append(self.laserRefraction[i])
            if i < self.laserLayersNumber - 1:
                refr.append(self.laserRefraction[i+1])
            else:
                refr.append(self.laserRefraction[i])
        plt.plot(coord, refr, 'b')
        plt.show()


