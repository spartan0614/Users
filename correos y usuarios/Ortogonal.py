#import Cabecera
#import Lateral
import NodoOrtogonal
ort = NodoOrtogonal

class Ortogonal(object):
	def __init__(self):
		self.c = Cabecera
		self.l = Lateral

	def Insertar(self,x ,y, nombre):
		nuevo = ort.NodoOrtogonal(x, y, nombre)

		if c.Existe(x) == False:
			c.Insertar(x)

		if l.Existe(y) == False:
			l.Insertar(y)

		auxC = NodoCabecera
		auxL = NodoLateral
		auxC = c.Busqueda(x)
		auxL = l.Busqueda(y)

		auxC.columna.Insertar(nuevo)
		auxL.fila.Insertar(nuevo)

	def Llenar(self, x, y, nombre):
		self.Insertar(x,y, nombre)


