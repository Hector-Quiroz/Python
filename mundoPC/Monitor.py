class Monitor:
    contadorMonitores = 0

    def __init__(self, marca, tamanio):
        Monitor.contadorMonitores += 1
        self._idMonitor = Monitor.contadorMonitores
        self._marca = marca
        self._tamanio = tamanio

    # Getters
    @property
    def marca(self):
        return self._marca

    @property
    def tamanio(self):
        return self._tamanio

    # Setters
    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @tamanio.setter
    def tamanio(self, tamanio):
        self._tamanio = tamanio


    def __str__(self):
        return f'Monitor {self._idMonitor} -> {self._marca}, Tamaño: {self._tamanio}'