"""
Clase derivada Automovil que hereda de Vehiculo.
Demuestra herencia, polimorfismo y agrega funcionalidades específicas.
"""

from models.vehiculo import Vehiculo  # Importa la clase base Vehiculo

class Automovil(Vehiculo):  # Herencia de Vehiculo
    def __init__(self, marca, modelo, año, tipo_combustible, num_puertas):  # Constructor de Automovil
        """
        Constructor de Automovil.
        Llama al constructor de la clase base y agrega atributos específicos.
        """
        super().__init__(marca, modelo, año)  # Llamada al constructor de la clase base
        self.__tipo_combustible = tipo_combustible  # Atributo privado
        self.__num_puertas = num_puertas   # Atributo privado
        self.__nivel_combustible = 50  # Porcentaje inicial
    
    # GETTERS Y SETTERS ESPECÍFICOS
    def get_tipo_combustible(self):   #
        return self.__tipo_combustible
    
    def get_num_puertas(self):
        return self.__num_puertas
    
    def get_nivel_combustible(self):
        return self.__nivel_combustible
    
    def cargar_combustible(self, cantidad):
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
        return f"{info_base} | Combustible: {self.__tipo_combustible} | Puertas: {self.__num_puertas}"
    
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
    
    def tocar_bocina(self):
        """Método específico de Automovil"""
        return "¡Beep! ¡Beep!"