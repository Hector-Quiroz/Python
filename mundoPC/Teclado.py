from mundoPC.DispositivoEntrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    contadorTeclados = 0

    def __init__(self, tipoEntrada, marca):
        super().__init__(tipoEntrada, marca)
        Teclado.contadorTeclados += 1
        self._idTeclado = Teclado.contadorTeclados

    def __str__(self):
        return f'Teclado {self._idTeclado} -> Tipo Entrada: {self._tipoEntrada}, Marca: {self._marca}'