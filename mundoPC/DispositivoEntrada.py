class DispositivoEntrada:
    def __init__(self, tipoEntrada: str, marca: str):
        self._tipoEntrada = tipoEntrada
        self._marca = marca

# Getters
@property
def tipoEntrada(self):
    return self._tipoEntrada

@property
def marca(self):
    return self._marca

# Setters
@tipoEntrada.setter
def tipoEntrada(self, tipoEntrada):
    self._tipoEntrada = tipoEntrada

@marca.setter
def marca(self, marca):
    self._marca = marca