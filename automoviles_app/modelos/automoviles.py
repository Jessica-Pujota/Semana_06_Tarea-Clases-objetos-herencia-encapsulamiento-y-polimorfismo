"""
Clase derivada Automovil que hereda de Vehiculo.
Demuestra herencia, polimorfismo y agrega funcionalidades específicas.
"""

from modelos.vehiculos import Vehiculo  # Importa la clase base Vehiculo

class Automovil(Vehiculo):  # Herencia de Vehiculo
    def __init__(self, marca, modelo, año, tipo_combustible):  # Constructor de Automovil
        """
        Constructor de Automovil.
        Llama al constructor de la clase base y agrega atributos específicos.
        """
        super().__init__(marca, modelo, año)  # Llamada al constructor de la clase base
        self.__tipo_combustible = tipo_combustible  # Atributo privado
        self.__nivel_combustible = 50  # Porcentaje inicial
    
    # GETTERS Y SETTERS ESPECÍFICOS
    def get_tipo_combustible(self):   # Devuelve el tipo de combustible
        return self.__tipo_combustible    # Devuelve el tipo de combustible
    
    def get_nivel_combustible(self):   # Devuelve el nivel de combustible
        return self.__nivel_combustible
    
    def cargar_combustible(self, cantidad):   # Carga combustible
        
        """Método específico para cargar combustible"""
        if 0 <= cantidad <= 100:   
            self.__nivel_combustible = min(100, self.__nivel_combustible + cantidad)
            return f"Combustible cargado. Nivel actual: {self.__nivel_combustible}%"
        return "Cantidad inválida"
    
    # POLIMORFISMO: Sobrescritura de métodos
    def obtener_informacion(self):
        """
        Sobrescribe el método de la clase base para incluir información específica.
        Ejemplo de polimorfismo.
        """
        info_base = super().obtener_informacion()
        return f"{info_base} | Combustible: {self.__tipo_combustible}"

    def viajar(self, distancia):
        """
        Sobrescribe el método viajar para considerar el consumo de combustible.
        Polimorfismo con comportamiento específico.
        """
        consumo = distancia * 0.1  # Consumo: 10% por 100 km
        if consumo <= self.__nivel_combustible:
            self.__nivel_combustible -= consumo
            # Llama al método de la clase base usando super()
            resultado_base = super().viajar(distancia)
            return f"{resultado_base} | Combustible restante: {self.__nivel_combustible:.1f}%"
        return "Combustible insuficiente para el viaje"
    
    # MÉTODOS ESPECÍFICOS DE AUTOMÓVIL
    def abrir_maletero(self):
        """Método específico de Automovil"""
        return "Maletero abierto"
    
    def tocar_bocina(self):  # Método específico de Automovil
        """Método específico de Automovil"""
        return "¡Beep! ¡Beep!"