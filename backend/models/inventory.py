"""
Modelo para la tabla 'inventario' en la base de datos.

Autor: IA Punto: Soluciones Integrales de Tecnología y Marketing
Proyecto para: INDUSTRIAS PICO S.A.S
Dirección: MEng. Sergio Lankaster Rondón Melo
Colaboración: Ing. Francisco Garnica
Fecha de creación: 2023-09-13
Última modificación: 2024-09-17
"""

import sqlite3

class Inventory:
    def __init__(self, db_name='inventario.db'):
        """
        Inicializa el modelo de inventario y crea la tabla si no existe.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """
        Crea la tabla 'inventario' si no existe.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS inventario (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                categoria_id INTEGER NOT NULL,
                referencia TEXT NOT NULL UNIQUE,
                tamaño_rin TEXT NOT NULL,
                marca_id INTEGER NOT NULL,
                ubicacion INTEGER,
                fecha_ingreso TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                fecha_salida TIMESTAMP,
                FOREIGN KEY(categoria_id) REFERENCES categorias(id),
                FOREIGN KEY(marca_id) REFERENCES marcas(id)
            )
        ''')
        self.conn.commit()

    def add_tire(self, categoria_id, referencia, tamaño_rin_id, marca_id, ubicacion=None):
        """
        Agrega una llanta al inventario.

        Args:
            categoria_id: ID de la categoría de la llanta.
            referencia: Referencia única de la llanta.
            tamaño_rin_id: ID del tamaño de rin de la llanta.
            marca_id: ID de la marca de la llanta.
            ubicacion: Número de bucket donde se almacena la llanta (opcional, NULL por defecto).
        """
        try:
            self.cursor.execute('''
                INSERT INTO inventario (categoria_id, referencia, tamaño_rin_id, marca_id, ubicacion) 
                VALUES (?, ?, ?, ?, ?)
            ''', (categoria_id, referencia, tamaño_rin_id, marca_id, ubicacion))
            self.conn.commit()
            print("Llanta agregada al inventario exitosamente.")
        except sqlite3.IntegrityError:
            print(f"Error: La referencia '{referencia}' ya existe en el inventario.")
        except Exception as e:
            print(f"Error al agregar la llanta: {e}")

    def find_tire(self, referencia):
        """
        Busca una llanta en el inventario por su referencia.

        Args:
            referencia: La referencia de la llanta a buscar.

        Returns:
            Una tupla con los datos de la llanta si se encuentra, None en caso contrario.
        """
        try:
            self.cursor.execute('SELECT * FROM inventario WHERE referencia = ?', (referencia,))
            tire = self.cursor.fetchone()
            return tire
        except Exception as e:
            print(f"Error al buscar la llanta: {e}")
            return None

    def update_tire(self, referencia, nuevos_datos):
        """
        Actualiza los datos de una llanta en el inventario.

        Args:
            referencia: La referencia de la llanta a actualizar.
            nuevos_datos: Un diccionario con los nuevos valores para los campos a actualizar.
                          Ejemplo: {'ubicacion': 5, 'fecha_salida': '2024-09-17 10:30:00'}
        """
        try:
            set_clause = ', '.join([f"{campo} = ?" for campo in nuevos_datos.keys()])
            values = list(nuevos_datos.values()) + [referencia]
            self.cursor.execute(f'UPDATE inventario SET {set_clause} WHERE referencia = ?', values)
            self.conn.commit()
            print(f"Llanta con referencia '{referencia}' actualizada exitosamente.")
        except Exception as e:
            print(f"Error al actualizar la llanta: {e}")

    def delete_tire(self, referencia):
        """
        Elimina una llanta del inventario.

        Args:
            referencia: La referencia de la llanta a eliminar.
        """
        try:
            self.cursor.execute('DELETE FROM inventario WHERE referencia = ?', (referencia,))
            self.conn.commit()
            print(f"Llanta con referencia '{referencia}' eliminada exitosamente.")
        except Exception as e:
            print(f"Error al eliminar la llanta: {e}")

    def __del__(self):
        """
        Cierra la conexión a la base de datos al destruir el objeto.
        """
        self.conn.close()