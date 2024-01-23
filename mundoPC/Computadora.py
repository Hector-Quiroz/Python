class Computadora:
    contadorComputadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contadorComputadoras += 1
        self._idComputadora = Computadora.contadorComputadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    # Getters
    @property
    def nombre(self):
        return self._nombre

    @property
    def monitor(self):
        return self._monitor

    @property
    def teclado(self):
        return self._teclado

    @property
    def raton(self):
         return self._raton

    # Setters
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    def monitor(self, monitor):
        self._monitor = monitor

    @teclado.setter
    def teclado(self, teclado):
        self._teclado = teclado

    @raton.setter
    def raton(self, raton):
        self._raton = raton

    def __str__(self):
        return f"""
        Computadora {self._nombre} {self._idComputadora} ->
        {self._monitor} |
        {self._teclado} |
        {self._raton}   |
        """

if __name__ == '__main__':
    from mundoPC.Monitor import Monitor
    from mundoPC.Teclado import Teclado
    from mundoPC.Raton import Raton

    monitor1 = Monitor('HP', 27)
    teclado1 = Teclado('USB', 'SG')
    raton1 = Raton('USBC', 'Yeyian')

    pc1 = Computadora('PrimerPC', monitor1, teclado1, raton1)

    print(pc1)