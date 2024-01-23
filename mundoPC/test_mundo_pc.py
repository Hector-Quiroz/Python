from mundoPC.Monitor import Monitor
from mundoPC.Teclado import Teclado
from mundoPC.Raton import Raton
from mundoPC.Computadora import Computadora
from mundoPC.Orden import Orden

# Computadora 1
monitor1 = Monitor('HP', 27)
teclado1 = Teclado('USB', 'SG')
raton1 = Raton('USBC', 'Yeyian')
pc1 = Computadora('PrimerPC', monitor1, teclado1, raton1)

# Computadora 2
monitor2 = Monitor('Yeyian', 24)
teclado2 = Teclado('USB', 'Razer')
raton2 = Raton('USB', 'LG')
pc2 = Computadora('SegundaPC', monitor2, teclado2, raton2)

# Coleccion de computadoras
carrito = [pc1, pc2]
order1 = Orden(carrito)

# Impresion de `Orden`
print(order1)
print('agregarComputadora()'.center(50,'-'))

# Computadora 3
monitor3 = Monitor('SG', 30)
teclado3 = Teclado('USBC', 'LG')
raton3 = Raton('USB', 'Razer')

# Probando funcion `agregarComputadora`
pc3 = Computadora('agregarPC', monitor3, teclado3, raton3)
order1.agregarComputadora(pc3)
print(order1, 'Ejecución exitosa'.center(50,'*'))

# Héctor Quiroz