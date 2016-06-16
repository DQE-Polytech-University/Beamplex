#Program algorithm

###Description of input and output data for each of the component parts

Laserstructure input data for the program is a text file `laserstructure.Json`, describing the values of the wavelength, thickness and concentration of each of the five layers).

The output are:
displayed graphic and text information(results of calculations)

###Description the program's structure and it's main parts

The program consists of 4 modules:

• ***The load module of input data (jsonloader)***

• ***The calculation module of the refractive index  (refraction)***

• ***The module of solutions of the Helmholtz equation (helmhotz)***

• ***Module plotting the dependence of the field amplitude and refractive index on the coordinate from the surface of the heterostructure (laserSrtusture)***

###The load module of input data (jsonloader)

Loading data into the buffer. Diagnostics of the system and reports any errors that occurred

     def loadJSON( self ):
	        try:
	            with open(self.fileName) as jsonFile:
	                self.data = json.load(jsonFile)
	        except IOError:
	            raise IOError(": file not found")
	        except ValueError:
	            raise ValueError(": syntax error")
	        print(self.fileName + " successfully loaded")
    
Extracting and reading information from the input file, identify the errors in the file (no input incorrect data: number of layers,the boundary values)

    def parseJSONData(self):      
	        try:
	            self.concentration = []
	            self.thickness = []
	            self.wavelength = self.data["wavelength"]
	            for i in range(5):
	                self.concentration.append( self.data["layers"][i]["concentration"])
	                self.thickness.append( self.data["layers"][i]["thickness"])
	        except KeyError:
	            raise KeyError(".json: data not found")
	        except IndexError:
	            raise IndexError(".json: actual number of layers does not match with layersNumber value")
	
	        if isinstance( self.wavelength, (int, float)) == False

    or isinstance( self.thickness, (list)) == False 
    or isinstance( self.concentration, (list)) == False:
	            raise TypeError(".json: type mismatch")
	        for i in range(5):
	            if isinstance(self.concentration[i], (int, float)) == False 


    or isinstance( self.thickness[i], (int, float)) == False:
	                raise TypeError(".json: type mismatch")
	            if self.concentration[i] <= 0 or self.concentration[i] >= 1
    or self.thickness[i] <= 0:
	                raise ValueError(".json: data out of range")
	
	        if self.wavelength < 0.85 or self.wavelength > 1.5:
	            raise ValueError(".json: data out of range")
	        
	        if self.concentration is None:
	            raise ValueError("self.concentration is undefined")
	        if self.thickness is None:
	            raise ValueError("self.thickness is undefined")
	        if self.wavelength is None:
	            raise ValueError("self.wavelength is undefined")
	
	        print(".json file successfully parsed")
	        return(( self.wavelength, self.concentration, self.thickness))


  

###The calculation module of the refractive index  (refraction)
Validation of necessary input data for the further calculation of the index of refraction for InGaAs и AlGaAs

    def refraction_AlGaAs(self, concentration):	
	        
	        if isinstance(self.wavelength, (int, float)) == False:
	            raise TypeError("self.wavelength should be a number")
	        if isinstance(concentration, (int, float)) == False:
	            raise TypeError("self.concentration should be a number")
	        if self.wavelength is None:
	            raise ValueError("self.wavelength is undefined")
	        if self.concentration is None:
	            raise ValueError("self.concentration is undefined")
	        if self.wavelength < 0.8 or self.wavelength > 1.5:
	            raise ValueError("self.wavelength out of range")
	        if concentration <= 0 or concentration >= 1:
	            raise ValueError("concentration out of range")
	            
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

    def refraction_InGaAs(self, concentration):	
	        
	        if isinstance(self.wavelength, (int, float)) == False:
	            raise TypeError("self.wavelength should be a number")
	        if isinstance(concentration, (int, float)) == False:
	            raise TypeError("self.concentration should be a number")
	        if self.wavelength is None:
	            raise ValueError("self.wavelength is undefined")
	        if self.concentration is None:
	            raise ValueError("self.concentration is undefined")
	        if self.wavelength < 0.8 or self.wavelength > 1.5:
	            raise ValueError("self.wavelength out of range")
	        if concentration <= 0 or concentration >= 1:
	            raise ValueError("concentration out of range")
	        
	        A = 8.95
	        B = 2.054
	        C = 0.6245
	        Eggaas = 1.424
	        E00 = 1.424 - 1.56 * concentration + 0.494 * concentration ** 2
	        n = (A + B/ (1 - (C * Eggaas / (self.wavelength * E00)) ** 2)) ** 0.5
	        return n

   

###The module of solutions of the Helmholtz equation (helmhotz)***


The advent of the grid functions for the discretization of the index profile in the coordinate
   
    self.matrix_dimension = steps
	        self.lyambda0 = lyambda
	        self.thickness = thickness
	        self.refraction = refr
	        self.deltaX = (sum((float(self.thickness[i])
    for i in range(0, int(len(self.thickness))))) - 0.001) / 

    float(self.matrix_dimension) 
	        self.deltaArb = float(self.deltaX * 2 * math.pi) / float(self.lyambda0)
	        self.gridX = [i * self.deltaX for i in range(0, self.matrix_dimension + 1)]

	        self.gridN = []
	        for i in self.gridX:
	            if 0 <= i and i < self.thickness[0]:
	                self.gridN.append(self.refraction[0])
	            if self.thickness[0] <= i and i < self.thickness[0] + self.thickness[1]:
	                self.gridN.append(self.refraction[1])
	            if self.thickness[0] + self.thickness[1] <= i and i < self.thickness[0] + 
    self.thickness[1] + self.thickness[2]:
	                self.gridN.append(self.refraction[2])
	            if self.thickness[0] + self.thickness[1] + 
    self.thickness[2] <= i and i < self.thickness[0] + 
     self.thickness[1] + self.thickness[2] + self.thickness[3]:
	                self.gridN.append(self.refraction[3])
	            if self.thickness[0] + self.thickness[1] + 
     self.thickness[2] + self.thickness[3] <= i and i < self.thickness[0] + 
    self.thickness[1] + self.thickness[2] +self.thickness[3] + self.thickness[4]:

	                self.gridN.append(self.refraction[4])


  The matrix to compute the maximum  of refractive index

    self.Mtr = [[0]*(self.matrix_dimension + 1) for x in range(self.matrix_dimension + 1)]
	        for j in range(self.matrix_dimension + 1):
	            for k in range(self.matrix_dimension + 1):
	                if j == k:
	                    self.Mtr[j][k] = (self.gridN[j] ** 2) - 2 / (self.deltaArb) ** 2
	                elif j == k - 1 or j == k + 1:
	                    self.Mtr[j][k] = 1 / self.deltaArb ** 2

 Finding the maximum value of the refractive index as the maximum eigenvalue of the matrix

    neffective = [x for x in range(self.matrix_dimension + 1)]
	        self.neffect = [x for x in range(self.matrix_dimension + 1)]
	        matric = linalg.eig(self.Mtr)                            
	        neffectiv = matric[0]                                    
	        for k in range(self.matrix_dimension + 1):                   
	            self.neffect[k] = (cmath.sqrt(neffectiv[k])).real            
	    
	        neff_max = max(self.neffect)                             
	        self.index_max = self.neffect.index(neff_max)

 Composition a tridiagonal matrix and finding proracing coefficients  

    self.Matr = [[0]*(self.matrix_dimension + 1) for x in range(self.matrix_dimension + 1)]
	        for j in range(self.matrix_dimension + 1):
	            for k in range(self.matrix_dimension + 1):
	                if j == k:
	                    self.Matr[j][k] = self.gridN[j]**2 - self.neffect[self.index_max]**2 - 2/self.deltaArb**2
	                elif j == k - 1 or j == k + 1:
	                    self.Matr[j][k] = 1 / self.deltaArb ** 2

    self.init = initPoint
	        self.Matr[self.init][self.init] = 1
	        self.aalp = [0 for x in range(self.matrix_dimension + 1)]
	        self.aalp[self.matrix_dimension] = float(-self.Matr[self.matrix_dimension]   float(self.Matr[self.matrix_dimension][self.matrix_dimension])
	        for i in range(self.matrix_dimension - 1, self.init, -1):
	            self.aalp[i] = float(-self.Matr[i][i-1]) / float(self.Matr[i][i] + self.Matr[i][i+1] * self.aalp[i+1])

Forward sweep of tridiagonal matrix algorithm

    self.X = [0 for x in range(self.matrix_dimension - self.init + 1)]
	        self.X[0] = self.aalp[self.init+1] * self.Matr[self.init][self.init]
	        for j in range(1,self.matrix_dimension-self.init +1):
	            self.X[j] = self.aalp[j+self.init]* self.X[j-1]

Reverse sweep of tridiagonal matrix algorithm 

     self.Y = [0 for x in range(self.init + 2)]
	        self.Y[self.init ] =  self.X[0]
	        self.Y[self.init + 1] = self.X[1]
	        for j in range(self.init - 1,-1,-1):
	            self.Y[j] = float((-1/self.Matr[j+1][j])) * float((self.Matr[j+1][j+1] * self.Y[j+1] +
    self.Matr[j+1][j+2] * self.Y[j+2]))


    Composes final solutionя
    self.U = [0 for x in range(self.matrix_dimension + 1)]
	        for i in range(self.init + 1):
	            self.U[i] = self.Y[i]
	        for j in range(self.init + 1 , self.matrix_dimension + 1):
	            self.U[j] = self.X[j - self.init]

   
Normalizes the solution

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



###Module plotting the dependence of the field amplitude and refractive index on the coordinate from the surface of the heterostructure (laserSrtusture)

The graph of the dependence of refractive index on the coordinate

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

 The graph of the field distribution from the coordinates
    
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
