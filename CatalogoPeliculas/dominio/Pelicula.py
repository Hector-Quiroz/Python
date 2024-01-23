class Pelicula:
    def __init__(self, nombre: str) -> str:
        """
        Crea un objeto tipo `Pelicula`
        """
        self._nombre = nombre

    # Getter
    @property
    def nombre(self):
        return self._nombre

    # Setter
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    def __str__(self):
        return f'Pelicula: {self._nombre}.'
    
    # Prueba
    if __name__ == "__main__":
        from Pelicula import Pelicula
        x = Pelicula("Django: Sin Cadenas")
        print(x)