class CatalogoPeliculas:
    ruta_archivo = 'peliculas.txt'

    @classmethod
    def agregarPelicula(cls, Pelicula: str):
        """
        Agrega una película al fichero
        """
        with open(CatalogoPeliculas.ruta_archivo, 'a', encoding='utf8') as fichero:
            fichero.write(f'{Pelicula.nombre}\n')

    @classmethod
    def listarPeliculas(cls):
        """
        Lista las peliculas encontradas en el fichero
        """
        with open(cls.ruta_archivo, 'r', encoding='utf8') as fichero:
            print('Catalogo de Películas'.center(50, '-'))
            print(fichero.read())
    
    @classmethod
    def eliminarPeliculas(cls):
        import os
        """
        Elmina el fichero donde se almacenan las peliculas
        """
        os.remove(cls.ruta_archivo)
        print(f'Fichero eliminado: {cls.ruta_archivo}')