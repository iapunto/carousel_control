"""
Controlador para el manejo del inventario de llantas.

Autor: IA Punto: Soluciones Integrales de Tecnología y Marketing
Proyecto para: INDUSTRIAS PICO S.A.S
Dirección: MEng. Sergio Lankaster Rondón Melo
Colaboración: Ing. Francisco Garnica
Fecha de creación: 2023-09-13
Última modificación: 2024-09-17
"""

from models.inventory import Inventory
from models.category import Category
from models.brand import Brand

class InventoryController:
    def __init__(self, inventory, carousel_controller):
        self.inventory = inventory
        self.carousel_controller = carousel_controller

    def add_tire(self, categoria_id, referencia, tamaño_rin, marca_id):
        """
        Agrega una llanta al inventario y la coloca en un bucket disponible.

        Args:
            categoria_id: ID de la categoría de la llanta.
            referencia: Referencia única de la llanta.
            tamaño_rin: Tamaño del rin de la llanta (ahora es TEXT).
            marca_id: ID de la marca de la llanta.
        """
        try:
            # Validar que la categoría y la marca existan
            if not self.validate_category_id(categoria_id):
                raise ValueError(f"La categoría con ID {categoria_id} no existe.")
            if not self.validate_brand_id(marca_id):
                raise ValueError(f"La marca con ID {marca_id} no existe.")

            ubicacion = self.inventory.find_available_bucket()
            if ubicacion:
                self.inventory.add_tire(categoria_id, referencia, tamaño_rin, marca_id, ubicacion)
                self.carousel_controller.send_command(1, ubicacion)  # Mueve el carrusel
                print(f"Llanta agregada al inventario en el bucket {ubicacion}.")
            else:
                print("Alerta: No hay espacio disponible en el carrusel. La llanta se agregará al inventario sin ubicación asignada.")
                self.inventory.add_tire(categoria_id, referencia, tamaño_rin, marca_id, None)
        except Exception as e:
            print(f"Error al agregar la llanta: {e}")

    def find_tire(self, search_term):
        """
        Busca una llanta en el inventario por referencia, marca o categoría.

        Args:
            search_term: El término de búsqueda (referencia, marca o categoría).

        Returns:
            Una lista de tuplas con los datos de las llantas encontradas, o una lista vacía si no se encuentra ninguna.
        """
        try:
            tires = self.inventory.find_tire(search_term)
            if tires:
                print(f"Llantas encontradas para el término de búsqueda '{search_term}':")
                for tire in tires:
                    self.print_tire_details(tire)
            else:
                print(f"No se encontraron llantas para el término de búsqueda '{search_term}'.")
            return tires
        except Exception as e:
            print(f"Error al buscar llantas: {e}")
            return []

    def check_and_assign_pending_tires(self):
        """
        Verifica si hay llantas sin ubicación asignada y les asigna un bucket si hay espacio disponible.
        """
        try:
            pending_tires = self.inventory.get_tires_without_location()
            for tire in pending_tires:
                ubicacion = self.inventory.find_available_bucket()
                if ubicacion:
                    self.inventory.update_tire(tire[2], {'ubicacion': ubicacion})
                    print(f"Llanta con referencia '{tire[2]}' asignada al bucket {ubicacion}.")
        except Exception as e:
            print(f"Error al asignar llantas pendientes: {e}")

    def move_carousel_to_tire(self, referencia):
        """
        Mueve el carrusel al bucket donde se encuentra una llanta.

        Args:
            referencia: La referencia de la llanta a buscar.
        """
        ubicacion = self.inventory.find_tire_location(referencia)
        if ubicacion:
            self.carousel_controller.send_command(1, ubicacion) 
        else:
            print("Llanta no encontrada en el inventario o no está en el carrusel.")

    def remove_tire_from_inventory(self, referencia):
        """
        Elimina una llanta del inventario y libera su espacio en el carrusel.

        Args:
            referencia: La referencia de la llanta a eliminar.
        """
        try:
            tire = self.inventory.get_tire_details(referencia)
            if tire:
                ubicacion = tire[5]
                if ubicacion is not None:
                    # Mueve el carrusel al bucket para descargar la llanta
                    self.carousel_controller.send_command(1, ubicacion)

                    # Actualiza la ubicación de la llanta a NULL y la fecha de salida
                    self.inventory.update_tire(referencia, {'ubicacion': None, 'fecha_salida': 'datetime(\'now\')'}) 
                    print(f"Llanta con referencia '{referencia}' eliminada del inventario y del bucket {ubicacion}.")
                else:
                    self.inventory.delete_tire(referencia)
                    print(f"Llanta con referencia '{referencia}' eliminada del inventario (no estaba en el carrusel).")
            else:
                print("Llanta no encontrada en el inventario.")
        except Exception as e:
            print(f"Error al eliminar la llanta: {e}")


    def print_tire_details(self, tire):
        """
        Imprime los detalles de una llanta de forma legible.
        """
        category_model = Category() 
        brand_model = Brand()        

        categoria_nombre = category_model.get_category_by_id(tire[1])[1] 
        marca_nombre = brand_model.get_brand_by_id(tire[4])[1] 

        print(f"  ID: {tire[0]}")
        print(f"  Categoría: {categoria_nombre}")
        print(f"  Referencia: {tire[2]}")
        print(f"  Tamaño de rin: {tire[3]}")
        print(f"  Marca: {marca_nombre}")
        print(f"  Ubicación: {tire[5]}")
        print(f"  Fecha de ingreso: {tire[6]}")
        print(f"  Fecha de salida: {tire[7]}")

    def find_tire_by_reference(self, referencia):
        """
        Busca una llanta en el inventario por su referencia.
        """
        tire = self.inventory.get_tire_details(referencia)
        if tire:
            self.print_tire_details(tire) 
            return tire
        else:
            print("Llanta no encontrada en el inventario.")
            return None

    def find_tires_by_brand(self, marca_id):
        """
        Busca llantas en el inventario por su marca.

        Args:
            marca_id: El ID de la marca a buscar.
        """
        try:
            self.inventory.cursor.execute('SELECT * FROM inventario WHERE marca_id = ?', (marca_id,))
            tires = self.inventory.cursor.fetchall()
            if tires:
                print(f"Llantas encontradas para la marca con ID {marca_id}:")
                for tire in tires:
                    self.print_tire_details(tire)
            else:
                print(f"No se encontraron llantas para la marca con ID {marca_id}.")
        except Exception as e:
            print(f"Error al buscar llantas por marca: {e}")

    def find_tires_by_category(self, categoria_id):
        """
        Busca llantas en el inventario por su categoría.

        Args:
            categoria_id: El ID de la categoría a buscar.
        """
        try:
            self.inventory.cursor.execute('SELECT * FROM inventario WHERE categoria_id = ?', (categoria_id,))
            tires = self.inventory.cursor.fetchall()
            if tires:
                print(f"Llantas encontradas para la categoría con ID {categoria_id}:")
                for tire in tires:
                    self.print_tire_details(tire)
            else:
                print(f"No se encontraron llantas para la categoría con ID {categoria_id}.")
        except Exception as e:
            print(f"Error al buscar llantas por categoría: {e}")
    
    def validate_category_id(self, categoria_id):
        """
        Verifica si una categoría con el ID dado existe en la base de datos.

        Args:
            categoria_id: El ID de la categoría a validar.

        Returns:
            True si la categoría existe, False en caso contrario.
        """
        try:
            # Realiza una consulta para contar cuántos registros tienen el category_id dado
            self.inventory.cursor.execute('SELECT COUNT(*) FROM categorias WHERE id = ?', (categoria_id,))
            count = self.inventory.cursor.fetchone()[0]
            return count > 0  # Devuelve True si hay al menos un registro con ese ID
        except Exception as e:
            print(f"Error al validar el ID de categoría: {e}")
            return False
        
    def validate_brand_id(self, marca_id):
        """
        Verifica si una marca con el ID dado existe en la base de datos.

        Args:
            marca_id: El ID de la marca a validar.

        Returns:
            True si la marca existe, False en caso contrario.
        """
        try:
            # Realiza una consulta para contar cuántos registros tienen el marca_id dado
            self.inventory.cursor.execute('SELECT COUNT(*) FROM marcas WHERE id = ?', (marca_id,))
            count = self.inventory.cursor.fetchone()[0]
            return count > 0  # Devuelve True si hay al menos un registro con ese ID
        except Exception as e:
            print(f"Error al validar el ID de marca: {e}")
            return False
    
    def update_tire(self, referencia, nuevos_datos):
        """
        Actualiza los datos de una llanta en el inventario.

        Args:
            referencia: La referencia de la llanta a actualizar.
            nuevos_datos: Un diccionario con los nuevos valores para los campos a actualizar.
                          Ejemplo: {'ubicacion': 5, 'fecha_salida': '2024-09-17 10:30:00'}
        """
        try:
            # Validar que la llanta exista
            tire = self.inventory.get_tire_details(referencia)
            if not tire:
                raise ValueError(f"La llanta con referencia '{referencia}' no existe en el inventario.")

            # Validar que la nueva categoría y marca existan (si se están actualizando)
            if 'categoria_id' in nuevos_datos:
                if not self.validate_category_id(nuevos_datos['categoria_id']):
                    raise ValueError(f"La categoría con ID {nuevos_datos['categoria_id']} no existe.")
            if 'marca_id' in nuevos_datos:
                if not self.validate_brand_id(nuevos_datos['marca_id']):
                    raise ValueError(f"La marca con ID {nuevos_datos['marca_id']} no existe.")

            # Construir la cláusula SET de la consulta SQL
            set_clause = ', '.join([f"{campo} = ?" for campo in nuevos_datos.keys()])
            values = list(nuevos_datos.values()) + [referencia]

            # Ejecutar la consulta UPDATE
            self.inventory.cursor.execute(f'UPDATE inventario SET {set_clause} WHERE referencia = ?', values)
            self.conn.commit()
            print(f"Llanta con referencia '{referencia}' actualizada exitosamente.")

            # Si se actualizó la ubicación, mover el carrusel si es necesario
            if 'ubicacion' in nuevos_datos and nuevos_datos['ubicacion'] is not None:
                self.carousel_controller.send_command(1, nuevos_datos['ubicacion'])

        except Exception as e:
            print(f"Error al actualizar la llanta: {e}")