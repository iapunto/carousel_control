"""
Controlador para el manejo de las marcas de llantas.

Autor: IA Punto: Soluciones Integrales de Tecnología y Marketing
Proyecto para: INDUSTRIAS PICO S.A.S
Dirección: MEng. Sergio Lankaster Rondón Melo
Colaboración: Ing. Francisco Garnica
Fecha de creación: 2024-09-17
"""

from models.brand import Brand

class BrandController:
    def __init__(self):
        self.brand_model = Brand()

    def add_brand(self, nombre):
        """
        Agrega una nueva marca.

        Args:
            nombre: Nombre de la marca.
        """
        self.brand_model.add_brand(nombre)

    def get_all_brands(self):
        """
        Obtiene todas las marcas registradas.

        Returns:
            Una lista de tuplas, donde cada tupla contiene el ID y el nombre de una marca.
        """
        return self.brand_model.get_all_brands()

    def get_brand_by_id(self, brand_id):
        """
        Obtiene una marca por su ID.

        Args:
            brand_id: El ID de la marca a buscar.

        Returns:
            Una tupla con los datos de la marca si se encuentra, None en caso contrario.
        """
        return self.brand_model.get_brand_by_id(brand_id)

    def update_brand(self, brand_id, nuevo_nombre):
        """
        Actualiza el nombre de una marca.

        Args:
            brand_id: El ID de la marca a actualizar.
            nuevo_nombre: El nuevo nombre de la marca.
        """
        self.brand_model.update_brand(brand_id, nuevo_nombre)

    def delete_brand(self, brand_id):
        """
        Elimina una marca.

        Args:
            brand_id: El ID de la marca a eliminar.
        """
        self.brand_model.delete_brand(brand_id)
        
        def find_brands(self, search_term):
            """
            Busca marcas en la base de datos que coincidan con el término de búsqueda.

            Args:
                search_term: El término de búsqueda (parte del nombre de la marca).

            Returns:
                Una lista de tuplas, donde cada tupla contiene el ID y el nombre de una marca que coincide con la búsqueda.
            """
            try:
                self.brand_model.cursor.execute('SELECT * FROM marcas WHERE nombre LIKE ?', ('%' + search_term + '%',))
                brands = self.brand_model.cursor.fetchall()
                return brands
            except Exception as e:
                print(f"Error al buscar marcas: {e}")
                return []