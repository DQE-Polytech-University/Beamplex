h = 4.1356 * 10 ** (-15)
cl = 2.998 * 10 ** 14

class RefractionCalc:
    concentration = []
    refraction = []
    wavelength = 0
    
    def __init__(self, lyambda, layersNumber, concentration):
        self.concentration = concentration
        self.wavelength = lyambda
        self.layersNumber = layersNumber
        
        
    def refraction_AlGaAs(self, concentration):	#index of refraction Al_x Ga_1-x As calculation:
        A0 = 6.3 + 19 * concentration
        B0 = 9.4 - 10.2 * concentration
        E0 = 1.425 + 1.155 * concentration + 0.37 * concentration ** 2
        delta0 = 0.34 - 0.04 * concentration
        chi = h * cl / (self.wavelength * E0)
        chiSO = h * cl / (self.wavelength * (E0 + delta0))
        fSO =  (2 - (1 + chiSO) ** 0.5 - (1 - chiSO) ** 0.5)/ chiSO ** 2
        f = (2 - (1 + chi) ** 0.5 -(1 - chi) ** 0.5)/ chi ** 2
        n = (A0 * (f + fSO/2 * (E0 / (E0 + delta0)) ** 1.5) + B0) ** 0.5
        return n
    
    def refraction_InGaAs(self, concentration):	#index of refraction In_x Ga_1-x As calculation:
        A = 8.95
        B = 2.054
        C = 0.6245
        Eggaas = 1.424
        E00 = 1.424 - 1.56 * concentration + 0.494 * concentration ** 2
        n = (A + B/ (1 - (C * Eggaas / (self.wavelength * E00)) ** 2)) ** 0.5
        return n

    def computeRefraction(self):
        for i in range(self.layersNumber):
            if i == (self.layersNumber / 2):
                self.refraction.append(self.refraction_InGaAs(self.concentration[i]))
            else:
                self.refraction.append(self.refraction_AlGaAs(self.concentration[i]))


