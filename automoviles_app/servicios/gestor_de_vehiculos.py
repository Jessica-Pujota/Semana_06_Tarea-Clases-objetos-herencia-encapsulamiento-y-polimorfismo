"""
Servicio para gestionar múltiples vehículos.
Demuestra el uso de listas y polimorfismo en tiempo de ejecución.
"""

class GestorVehiculos:
    def __init__(self):
        """Constructor que inicializa una lista vacía de vehículos"""
        self.__vehiculos = []  # Lista privada de vehículos
    
    def agregar_vehiculo(self, vehiculo):
        """
        Agrega un vehículo a la lista.
        Parámetro: Objeto de tipo Vehiculo o sus derivados.
        """
        self.__vehiculos.append(vehiculo)
        return f"Vehículo agregado: {vehiculo.get_marca()} {vehiculo.get_modelo()}"
    
    def listar_vehiculos(self):
        """Lista todos los vehículos usando polimorfismo"""
        if not self.__vehiculos:
            return "No hay vehículos registrados"
        
        resultado = "=== LISTA DE VEHÍCULOS ===\n"
        for i, vehiculo in enumerate(self.__vehiculos, 1):
            # POLIMORFISMO: Llamada al método obtener_informacion()
            # que se comporta diferente según el tipo de vehículo
            resultado += f"{i}. {vehiculo.obtener_informacion()}\n"
        return resultado
    
    def realizar_viaje_todos(self, distancia):
        """
        Realiza un viaje con todos los vehículos.
        Demuestra polimorfismo en el método viajar().
        """
        resultados = "=== RESULTADOS DE VIAJES ===\n"
        for vehiculo in self.__vehiculos:
            resultados += f"- {vehiculo.get_marca()}: {vehiculo.viajar(distancia)}\n"
        return resultados
    
    def obtener_estadisticas(self):
        """Calcula estadísticas de todos los vehículos"""
        if not self.__vehiculos:
            return "No hay vehículos para analizar"
        
        total_km = sum(v.get_kilometraje() for v in self.__vehiculos)
        promedio_km = total_km / len(self.__vehiculos)
        
        return f"""
        === ESTADÍSTICAS ===
        Total de vehículos: {len(self.__vehiculos)}
        Kilometraje total: {total_km} km
        Kilometraje promedio: {promedio_km:.2f} km
        """