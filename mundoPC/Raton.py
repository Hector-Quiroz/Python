from mundoPC.DispositivoEntrada import DispositivoEntrada

class Raton(DispositivoEntrada):
    contadorRatones = 0

    def __init__(self, tipoEntrada, marca):
        super().__init__(tipoEntrada, marca)
        Raton.contadorRatones += 1
        self._idRaton = Raton.contadorRatones

    def __str__(self):
        return f'Raton {self._idRaton} -> Tipo Entrada: {self._tipoEntrada}, Marca: {self._marca}'