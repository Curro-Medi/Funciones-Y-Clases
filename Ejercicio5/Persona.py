class persona:
    
    def __init__(self, nombre, edad, lugar_residencia):
        self.__nombre = nombre #privado
        self.__edad = edad
        self.__lugar_residencia = lugar_residencia
        

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre
        
    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self,edad):
        self.__edad = edad
        
    @property
    def lugar_residencia(self):
        return self.__lugar_residencia

    @lugar_residencia.setter
    def lugar_residencia(self,lugar_residencia):
        self.__lugar_residencia = lugar_residencia
        
    def descripcion(self):
        cadena=""
        cadena="Persona ->"+ self.__nombre+",\nEdad ->"+str(self.__edad)+",\nLugar de Residencia ->"+self.__lugar_residencia
        return cadena
    
    
class empleado(persona):
        
    def __init__(self, nombre, edad, lugar_residencia,salario,antiguedad):
        super().__init__(nombre, edad, lugar_residencia)
        self.__salario = salario
        self.__antiguedad = antiguedad
            
    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self,salario):
        self.__salario = salario
        
    @property
    def antiguedad(self):
        return self.__antiguedad

    @antiguedad.setter
    def antiguedad(self,antiguedad):
        self.__antiguedad = antiguedad
    
    def descripcionempleado(self):
        super().descripcion()
        #cadena2=""
        #cadena2="Persona ->"+super().__nombre+",\nEdad ->"+str(super().__edad)+",\nLugar de residencia ->"+super().__lugar_residencia+",\nSalario"+self.__salario+",\nAntiguedad"+self.__antiguedad+"."
        cadena3 = super().descripcion()+",\nSalario ->"+str(self.__salario)+ ",\nAntiguedad ->"+str(self.__antiguedad)
        return cadena3