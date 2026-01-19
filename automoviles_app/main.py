"""
Archivo principal para ejecutar la aplicación.
Demuestra la creación de instancias y el funcionamiento del sistema.
"""

from modelos.vehiculos import Vehiculo   # Importa la clase Vehiculo    
from modelos.automoviles import Automovil    # Importa la clase Automovil
from servicios.gestor_de_vehiculos import GestorVehiculos   # Importa el gestor de vehículos
    
def main():    
    """Función principal que demuestra todos los conceptos de POO"""
    
    print("=== DEMOSTRACIÓN DE CONCEPTOS DE POO ===\n")
    
    # 1. CREACIÓN DE INSTANCIAS
    print("1. CREANDO INSTANCIAS DE CLASES:")
    
    # Instancia de la clase base Vehiculo
    vehiculo_base = Vehiculo("Toyota", "Generic", 2020)
    print(f"   Vehículo base creado: {vehiculo_base.obtener_informacion()}")
    
    # Instancias de la clase derivada Automovil
    auto1 = Automovil("Toyota", "Corolla", 2022, "Gasolina", 4)
    auto2 = Automovil("Ford", "Mustang", 2023, "Eléctrico", 2)
    print(f"   Automovil 1: {auto1.obtener_informacion()}")
    print(f"   Automovil 2: {auto2.obtener_informacion()}")
    
    # 2. DEMOSTRACIÓN DE ENCAPSULACIÓN
    print("\n2. DEMOSTRACIÓN DE ENCAPSULACIÓN:")
    
    # Acceso mediante getters
    print(f"   Marca del auto1 (getter): {auto1.get_marca()}")
    print(f"   Año del auto1 (getter): {auto1.get_año()}")
    
    # Uso de setters con validación
    print(f"   Kilometraje inicial auto1: {auto1.get_kilometraje()} km")
    auto1.set_kilometraje(15000)
    print(f"   Kilometraje después de setter: {auto1.get_kilometraje()} km")
    
    # Intento de establecer valor inválido
    print("   Intentando disminuir kilometraje:")
    auto1.set_kilometraje(10000)  # Esto mostrará un mensaje de error
    
    # 3. DEMOSTRACIÓN DE HERENCIA Y POLIMORFISMO
    print("\n3. DEMOSTRACIÓN DE HERENCIA Y POLIMORFISMO:")
    
    # Lista polimórfica: puede contener diferentes tipos de vehículos
    lista_vehiculos = [vehiculo_base, auto1, auto2]
    
    print("   Llamada a obtener_informacion() en diferentes tipos:")
    for vehiculo in lista_vehiculos:
        # POLIMORFISMO: Mismo método, comportamientos diferentes
        print(f"   - {vehiculo.obtener_informacion()}")
    
    print("\n   Llamada a viajar() en diferentes tipos:")
    print(f"   Vehículo base: {vehiculo_base.viajar(100)}")
    print(f"   Automóvil 1: {auto1.viajar(100)}")
    
    # 4. USO DEL GESTOR DE VEHÍCULOS
    print("\n4. USANDO EL GESTOR DE VEHÍCULOS:")
    
    gestor = GestorVehiculos()
    
    # Agregar vehículos al gestor
    gestor.agregar_vehiculo(vehiculo_base)
    gestor.agregar_vehiculo(auto1)
    gestor.agregar_vehiculo(auto2)
    
    # Listar vehículos
    print(gestor.listar_vehiculos())
    
    # Realizar viajes con todos los vehículos
    print(gestor.realizar_viaje_todos(50))
    
    # Mostrar estadísticas
    print(gestor.obtener_estadisticas())
    
    # 5. DEMOSTRACIÓN DE MÉTODOS ESPECÍFICOS
    print("\n5. MÉTODOS ESPECÍFICOS DE AUTOMÓVIL:")
    print(f"   Auto1 - Tocar bocina: {auto1.tocar_bocina()}")
    print(f"   Auto1 - Abrir maletero: {auto1.abrir_maletero()}")
    print(f"   Auto1 - Cargar combustible: {auto1.cargar_combustible(30)}")
    
    # 6. ESTADO FINAL
    print("\n6. ESTADO FINAL DE LOS VEHÍCULOS:")
    print(f"   Vehículo base - Estado: {vehiculo_base.estado_vehiculo()}")
    print(f"   Auto1 - Nivel de combustible: {auto1.get_nivel_combustible()}%")
    
    print("\n=== PROGRAMA FINALIZADO ===")

if __name__ == "__main__":
    main()
    