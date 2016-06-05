import matplotlib.pyplot as plt

class Laser:

    laserRefraction = []
    laserField = []

    def __init__(self, wavelength, layersNumber, concentration, thickness):

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
