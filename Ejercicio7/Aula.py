class Aula:
    
    def __init__(self, largo, ancho, alto, aforo_completo):
        self.__largo = largo
        self.__ancho = ancho
        self.__alto = alto
        self.__aforo_completo = aforo_completo
         

    @property
    def largo(self):
        return self.__largo

    @largo.setter
    def largo(self,largo):
        self.__largo = largo
        
        
    @property
    def ancho(self):
        return self.__ancho

    @ancho.setter
    def ancho(self,ancho):
        self.__ancho = ancho
        
        
    @property
    def alto(self):
        return self.__alto

    @alto.setter
    def alto(self,alto):
        self.__alto = alto
        
        
    @property
    def aforo_completo(self):
        return self.__aforo_completo

    @aforo_completo.setter
    def aforo_completo(self,aforo_completo):
        self.__aforo_completo = aforo_completo
        
        
        
    def descripcion(self):
    
        cadena="Largo -> "+self.__largo +",\nAncho -> "+self.__ancho+ ",\nAlto -> "+self.__alto+",\nAforo completo -> "+str(self.__aforo_completo)
        return cadena
        
        
    def completo(self):
    
        self.__aforo_completo = True
        cadena="Aforo Completo"
        return cadena
        
        
    def estado(self):
    
        if self.__aforo_completo == True:
            cadena="El Aforo esta Completo"
            
        elif self.__aforo_completo == False:
            cadena="No esta el aforo completo"
            
        return cadena
        
        
    def miauladatos(self):
    
        cadena="El largo de la clase es -> "+self.__largo +",\nY el aforo -> "+str(self.__aforo_completo)
        return cadena
        
        
class aula2(Aula):  
    
    def __init__(self,largo, ancho, alto, aforo_completo,completamos):
        super().__init__( largo, ancho, alto, aforo_completo,)
        self.__largo = largo
        self.__ancho = ancho
        self.__alto = alto
        self.__aforo_completo = aforo_completo
        self.__completamos = completamos
    
    @property
    def completamos(self):
        return self.__completamos

    @completamos.setter
    def completamos(self,completamos):
        self.__completamos = completamos
        
        
    
    @property
    def largo(self):
        return self.__largo

    @largo.setter
    def largo(self,largo):
        self.__largo = largo
        
        
    @property
    def ancho(self):
        return self.__ancho

    @ancho.setter
    def ancho(self,ancho):
        self.__ancho = ancho
        
        
    @property
    def alto(self):
        return self.__alto

    @alto.setter
    def alto(self,alto):
        self.__alto = alto
        
        
    @property
    def aforo_completo(self):
        return self.__aforo_completo

    @aforo_completo.setter
    def aforo_completo(self,aforo_completo):
        self.__aforo_completo = aforo_completo
        
        
    def estado(self):
    
        if self.__aforo_completo == True:
            completamos = "El aforo esta completo"
            
        elif self.__aforo_completo == False:
            completamos = "El aforo no esta completo"
            
        return completamos
    
    
    def descripcionaula2(self):
        super().descripcion()
        
        cadena2=super().descripcion()+self.__completamos
        return cadena2

    




