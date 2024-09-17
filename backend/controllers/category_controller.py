"""
Controlador para el manejo de las categorías de llantas.

Autor: IA Punto: Soluciones Integrales de Tecnología y Marketing
Proyecto para: INDUSTRIAS PICO S.A.S
Dirección: MEng. Sergio Lankaster Rondón Melo
Colaboración: Ing. Francisco Garnica
Fecha de creación: 2024-09-17
"""

from models.category import Category

class CategoryController:
    def __init__(self):
        self.category_model = Category()

    def add_category(self, nombre):
        """
        Agrega una nueva categoría.

        Args:
            nombre: Nombre de la categoría.
        """
        self.category_model.add_category(nombre)

    def get_all_categories(self):
        """
        Obtiene todas las categorías registradas.

        Returns:
            Una lista de tuplas, donde cada tupla contiene el ID y el nombre de una categoría.
        """
        return self.category_model.get_all_categories()

    def get_category_by_id(self, category_id):
        """
        Obtiene una categoría por su ID.

        Args:
            category_id: El ID de la categoría a buscar.

        Returns:
            Una tupla con los datos de la categoría si se encuentra, None en caso contrario.
        """
        return self.category_model.get_category_by_id(category_id)

    def update_category(self, category_id, nuevo_nombre):
        """
        Actualiza el nombre de una categoría.

        Args:
            category_id: El ID de la categoría a actualizar.
            nuevo_nombre: El nuevo nombre de la categoría.
        """
        self.category_model.update_category(category_id, nuevo_nombre)

    def delete_category(self, category_id):
        """
        Elimina una categoría.

        Args:
            category_id: El ID de la categoría a eliminar.
        """
        self.category_model.delete_category(category_id)
        
    def find_categories(self, search_term):
        """
        Busca categorías en la base de datos que coincidan con el término de búsqueda.

        Args:
            search_term: El término de búsqueda (parte del nombre de la categoría).

        Returns:
            Una lista de tuplas, donde cada tupla contiene el ID y el nombre de una categoría que coincide con la búsqueda.
        """
        try:
            self.category_model.cursor.execute('SELECT * FROM categorias WHERE nombre LIKE ?', ('%' + search_term + '%',))
            categories = self.category_model.cursor.fetchall()
            return categories
        except Exception as e:
            print(f"Error al buscar categorías: {e}")
            return []