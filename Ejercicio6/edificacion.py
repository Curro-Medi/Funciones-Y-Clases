class edificacion:
    
    def __init__(self, altura, constructora, valor_suelo, ubicacion):
        self.__altura = altura #privado
        self.__constructora = constructora
        self.__valor_suelo = valor_suelo
        self.__ubicacion = ubicacion
        

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self,altura):
        self.__altura = altura
        
    @property
    def constructora(self):
        return self.__constructora

    @constructora.setter
    def constructora(self,constructora):
        self.__constructora = constructora
        
    @property
    def valor_suelo(self):
        return self.__valor_suelo

    @valor_suelo.setter
    def valor_suelo(self,valor_suelo):
        self.__valor_suelo = valor_suelo

    @property
    def ubicacion(self):
        return self.__ubicacion
    
    @ubicacion.setter
    def ubicacion(self,ubicacion):
        self.__ubicacion = ubicacion
    
    
    def descripcion(self):
    
        cadena="Altura -> "+ str(self.__altura)+",\nConstructora -> "+self.__constructora+ ",\nUbicacion -> "+self.__ubicacion+",\nValor del suelo -> "+str(self.__valor_suelo)
        return cadena


class piso(edificacion):
    
    def __init__(self,altura, constructora, valor_suelo, ubicacion, metros_construidos, num_habitaciones , num_banios, precio, planta, num_piso, puerta):
        super().__init__( altura, constructora, valor_suelo, ubicacion)
        self.__metros_construidos = metros_construidos 
        self.__num_habitaciones = num_habitaciones
        self.__num_banios = num_banios
        self.__precio = precio
        self.__planta = planta
        self.__num_piso = num_piso
        self.__puerta = puerta

    @property
    def metros_construidos(self):
        return self.__metros_construidos
    
    @metros_construidos.setter
    def ubicacion(self,metros_construidos):
        self.__metros_construidos = metros_construidos


    @property
    def num_habitaciones(self):
        return self.__num_habitaciones
    
    @num_habitaciones.setter
    def num_habitaciones(self,num_habitaciones):
        self.__num_habitaciones = num_habitaciones
        

    @property
    def num_banios(self):
        return self.__num_banios
    
    @num_banios.setter
    def num_banios(self,num_banios):
        self.__num_banios = num_banios
       
    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self,precio):
        self.__precio = precio
        
    @property
    def planta(self):
        return self.__planta
    
    @planta.setter
    def planta(self,planta):
        self.__planta = planta
        
        
    @property
    def num_piso(self):
        return self.__num_piso
    
    @num_piso.setter
    def num_piso(self,num_piso):
        self.__num_piso = num_piso
        
    
    @property
    def puerta(self):
        return self.__puerta
    
    @puerta.setter
    def puerta(self,puerta):
        self.__puerta = puerta
        

    def descripcionpiso(self):
        super().descripcion()
        
        cadena2=super().descripcion()+"Metros construidos -> "+str(self.__metros_construidos)+",\nNumero de habitaciones -> "+str(self.__num_habitaciones)+",\nNumero de banios -> "+str(self.__num_banios)+",\nPrecio -> "+str(self.__precio)+",\nPlanta -> "+str(self.__planta)+",\nNumero de piso -> "+str(self.__num_piso)+",\nPuerta -> "+str(self.__puerta)
        return cadena2
    
    
    
    
    
    
    




