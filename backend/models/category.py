"""
Modelo para la tabla 'categorias' en la base de datos.

Autor: IA Punto: Soluciones Integrales de Tecnología y Marketing
Proyecto para: INDUSTRIAS PICO S.A.S
Dirección: MEng. Sergio Lankaster Rondón Melo
Colaboración: Ing. Francisco Garnica
Fecha de creación: 2024-09-17
"""

import sqlite3

class Category:
    def __init__(self, db_name='inventario.db'):
        """
        Inicializa el modelo de categorías y crea la tabla si no existe.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """
        Crea la tabla 'categorias' si no existe.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS categorias (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL UNIQUE
            )
        ''')
        self.conn.commit()

    def add_category(self, nombre):
        """
        Agrega una nueva categoría.

        Args:
            nombre: Nombre de la categoría.
        """
        try:
            self.cursor.execute('INSERT INTO categorias (nombre) VALUES (?)', (nombre,))
            self.conn.commit()
            print(f"Categoría '{nombre}' agregada exitosamente.")
        except sqlite3.IntegrityError:
            print(f"Error: La categoría '{nombre}' ya existe.")
        except Exception as e:
            print(f"Error al agregar la categoría: {e}")

    def get_all_categories(self):
        """
        Obtiene todas las categorías registradas.

        Returns:
            Una lista de tuplas, donde cada tupla contiene el ID y el nombre de una categoría.
        """
        try:
            self.cursor.execute('SELECT * FROM categorias')
            categories = self.cursor.fetchall()
            return categories
        except Exception as e:
            print(f"Error al obtener las categorías: {e}")
            return []

    def get_category_by_id(self, category_id):
        """
        Obtiene una categoría por su ID.

        Args:
            category_id: El ID de la categoría a buscar.

        Returns:
            Una tupla con los datos de la categoría si se encuentra, None en caso contrario.
        """
        try:
            self.cursor.execute('SELECT * FROM categorias WHERE id = ?', (category_id,))
            category = self.cursor.fetchone()
            return category
        except Exception as e:
            print(f"Error al obtener la categoría por ID: {e}")
            return None

    def update_category(self, category_id, nuevo_nombre):
        """
        Actualiza el nombre de una categoría.

        Args:
            category_id: El ID de la categoría a actualizar.
            nuevo_nombre: El nuevo nombre de la categoría.
        """
        try:
            self.cursor.execute('UPDATE categorias SET nombre = ? WHERE id = ?', (nuevo_nombre, category_id))
            self.conn.commit()
            print(f"Categoría con ID {category_id} actualizada exitosamente.")
        except sqlite3.IntegrityError:
            print(f"Error: La categoría '{nuevo_nombre}' ya existe.")
        except Exception as e:
            print(f"Error al actualizar la categoría: {e}")

    def delete_category(self, category_id):
        """
        Elimina una categoría.

        Args:
            category_id: El ID de la categoría a eliminar.
        """
        try:
            self.cursor.execute('DELETE FROM categorias WHERE id = ?', (category_id,))
            self.conn.commit()
            print(f"Categoría con ID {category_id} eliminada exitosamente.")
        except Exception as e:
            print(f"Error al eliminar la categoría: {e}")

    def __del__(self):
        """
        Cierra la conexión a la base de datos al destruir el objeto.
        """
        self.conn.close()