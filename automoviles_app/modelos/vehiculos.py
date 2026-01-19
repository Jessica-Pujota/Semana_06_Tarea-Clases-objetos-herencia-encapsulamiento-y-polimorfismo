"""Clase base Vehiculo que demuestra encapsulación y define la estructura base para todos los vehículos del sistema"""

class Vehiculo:   #definición de la clase vehículo
    def __init__(self, marca, modelo, año):    # # Constructor de la clase      
        """Constructor de la clase base Vehiculo. Atributos privados (encapsulación) para proteger los datos."""
        
        #  Atributos protegidos y privados
        self._marca = marca  # Atributo protegido
        self._modelo = modelo   # Atributo protegido
        self.__año = año  # Atributo privado (doble guion bajo)
        self.__kilometraje = 0  # Atributo privado inicializado en 0
    
    # -------- GETTERS Y SETTERS (encapsulación)----------
    def get_marca(self):   # Método getter para obtener el valor de marca
        """Getter para marca"""
        return self._marca     # Retorna el valor del atributo protegido
    
    def set_marca(self, nueva_marca):    # Método setter para modificar marca
        """Setter para marca"""
        self._marca = nueva_marca     # Asigna nuevo valor al atributo
    
    def get_modelo(self):    # Getter para modelo
        """Getter para modelo"""
        return self._modelo   # Retorna el valor del atributo protegido
    
    def get_año(self):  # Getter para año
        """Getter para año (atributo privado)"""
        return self.__año   # Retorna el valor del año (privado)
    
    def get_kilometraje(self):  # Getter para kilometraje
        """Getter para kilometraje"""
        return self.__kilometraje   # Retorna el valor del kilometraje actual (atributo privado)
    
    def set_kilometraje(self, km):    # Setter para kilometraje
        """Setter con validación para kilometraje"""
        if km >= self.__kilometraje:   # Validación: no permitir disminuir kilometraje
            self.__kilometraje = km    # Asigna nuevo valor al kilometraje si es valido
        else:    # Si el valor no es válido (km menor al actual)
            print("Error: El kilometraje no puede disminuir")   # Mensaje de error
    
    # MÉTODOS COMUNES
    def obtener_informacion(self):   #Método para obtener informacion del vehículo
        """Método que será sobrescrito en clases derivadas (polimorfismo). Retorna información básica del vehículo."""
        
        return f"{self._marca} {self._modelo} ({self.__año})"
    
    def viajar(self, distancia):
        """Método para simular un viaje. Aumenta el kilometraje del vehículo."""
        if distancia > 0:   # Validación de distancia positiva
            self.__kilometraje += distancia
            return f"Viaje de {distancia} km realizado. Kilometraje total: {self.__kilometraje} km"
        return "Distancia debe ser positiva"   # Mensaje de error si la distancia no es positiva
    
    def estado_vehiculo(self):  # Método para analizar el estado del vehículo
        """
        Método que analiza el estado del vehículo basado en el kilometraje.
        Ejemplo de método con lógica específica.
        """
        if self.__kilometraje == 0:   # Si el kilometraje es 0
            return "Nuevo"   #Vehículo nuevo
        elif self.__kilometraje < 50000:  # Si el kilometraje es menor a 50,000
            return "Poco uso"  #Vehículo con poco uso
        elif self.__kilometraje < 150000:  # Si el kilometraje es menor a 150,000
            return "Uso moderado"  #Vehículo con uso moderado
        else:  # Si el kilometraje es 150,000 o más
            return "Alto kilometraje"  #Vehículo con alto kilometraje
        