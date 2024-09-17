"""
Modelo para la tabla 'marcas' en la base de datos.

Autor: IA Punto: Soluciones Integrales de Tecnología y Marketing
Proyecto para: INDUSTRIAS PICO S.A.S
Dirección: MEng. Sergio Lankaster Rondón Melo
Colaboración: Ing. Francisco Garnica
Fecha de creación: 2024-09-17
"""

import sqlite3

class Brand:
    def __init__(self, db_name='inventario.db'):
        """
        Inicializa el modelo de marcas y crea la tabla si no existe.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """
        Crea la tabla 'marcas' si no existe.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS marcas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL UNIQUE
            )
        ''')
        self.conn.commit()

    def add_brand(self, nombre):
        """
        Agrega una nueva marca.

        Args:
            nombre: Nombre de la marca.
        """
        try:
            self.cursor.execute('INSERT INTO marcas (nombre) VALUES (?)', (nombre,))
            self.conn.commit()
            print(f"Marca '{nombre}' agregada exitosamente.")
        except sqlite3.IntegrityError:
            print(f"Error: La marca '{nombre}' ya existe.")
        except Exception as e:
            print(f"Error al agregar la marca: {e}")

    def get_all_brands(self):
        """
        Obtiene todas las marcas registradas.

        Returns:
            Una lista de tuplas, donde cada tupla contiene el ID y el nombre de una marca.
        """
        try:
            self.cursor.execute('SELECT * FROM marcas')
            brands = self.cursor.fetchall()
            return brands
        except Exception as e:
            print(f"Error al obtener las marcas: {e}")
            return []

    def get_brand_by_id(self, brand_id):
        """
        Obtiene una marca por su ID.

        Args:
            brand_id: El ID de la marca a buscar.

        Returns:
            Una tupla con los datos de la marca si se encuentra, None en caso contrario.
        """
        try:
            self.cursor.execute('SELECT * FROM marcas WHERE id = ?', (brand_id,))
            brand = self.cursor.fetchone()
            return brand
        except Exception as e:
            print(f"Error al obtener la marca por ID: {e}")
            return None

    def update_brand(self, brand_id, nuevo_nombre):
        """
        Actualiza el nombre de una marca.

        Args:
            brand_id: El ID de la marca a actualizar.
            nuevo_nombre: El nuevo nombre de la marca.
        """
        try:
            self.cursor.execute('UPDATE marcas SET nombre = ? WHERE id = ?', (nuevo_nombre, brand_id))
            self.conn.commit()
            print(f"Marca con ID {brand_id} actualizada exitosamente.")
        except sqlite3.IntegrityError:
            print(f"Error: La marca '{nuevo_nombre}' ya existe.")
        except Exception as e:
            print(f"Error al actualizar la marca: {e}")

    def delete_brand(self, brand_id):
        """
        Elimina una marca.

        Args:
            brand_id: El ID de la marca a eliminar.
        """
        try:
            self.cursor.execute('DELETE FROM marcas WHERE id = ?', (brand_id,))
            self.conn.commit()
            print(f"Marca con ID {brand_id} eliminada exitosamente.")
        except Exception as e:
            print(f"Error al eliminar la marca: {e}")

    def __del__(self):
        """
        Cierra la conexión a la base de datos al destruir el objeto.
        """
        self.conn.close()