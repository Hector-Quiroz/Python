class Orden:
    contadorOrdenes = 0

    def __init__(self, computadoras):
        Orden.contadorOrdenes += 1
        self._idOrden = Orden.contadorOrdenes
        self._computadoras = computadoras

    def agregarComputadora(self, computadora):
        self._computadoras.append(computadora)

    def __str__(self):
        computadorasStr = ''
        for PC in self._computadoras:
            computadorasStr += PC.__str__()
        return f"""
            Orden {self._idOrden}:
            {computadorasStr}
            """

    # Getters
    @property
    def computadoras(self):
        return self._computadoras

    # Setters
    @computadoras.setter
    def computadoras(self, *computadoras):
        self._computadoras = computadoras