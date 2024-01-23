from dominio.Pelicula import Pelicula
from servicio.CatalogoPeliculas import CatalogoPeliculas

op = None

while op != 4:
    try:
        print('***Bienvenido***')
        print('1) Agregar película')
        print('2) Listar películas')
        print('3) Eliminar archivo de películas')
        print('4) Salir')

        op = int(input('Ingrese su opción: '))

        if op == 1:
            nombrePelicula = str(input("Digita el nombre de la pelicula: "))
            pelicula = Pelicula(nombrePelicula)
            CatalogoPeliculas.agregarPelicula(pelicula)

        elif op == 2:
            CatalogoPeliculas.listarPeliculas()

        elif op == 3:
            CatalogoPeliculas.eliminarPeliculas()

    except Exception as e:
        print(f'Ocurrio un error: {e}')
        op = None
else:
    print('Fin del programa.')