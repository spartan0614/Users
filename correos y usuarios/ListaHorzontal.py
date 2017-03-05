import NodoOrtogonal

class ListaHorizontal(object):
	def __init__(self):
		self.primero = None
		self.ultimo = None
		self.nuevo = NodoOrtogonal

	def Insertar(self, nuevo):
		nuevo = NodoOrtogonal(x, y, nombre)
		if self.primero == None:
			self.primero = self.ultimo = nuevo;
		else:
			if nuevo.x < self.primero.x:
				self.InsertarFrente(nuevo)
			elif nuevo.x > ultimo.x:
				self.InsertarFinal(nuevo)
			else:
				self.InsertarMedio(nuevo)


	def InsertarFrente(self, nuevo):
		self.primero.izquierda = nuevo
		nuevo.derecha = self.primero
		self.primero = self.primero.izquierda

	def InsertarFinal(self, nuevo):
		self.ultimo.derecha = nuevo
		nuevo.izquierda = self.ultimo
		self.ultimo = self.ultimo.derecha

	def InsertarMedio(self, nuevo):
		aux = NodoOrtogonal
		aux2 = NodoOrtogonal
		aux = self.primero

		while aux.x < nuevo.x:
			aux = aux.derecha

		aux2 = aux.izquierda
		aux2.derecha = nuevo
		aux.izquierda = nuevo
		nuevo.derecha = aux
		nuevo.izquierda = aux2

	def Recorrer(self):
		aux = NodoOrtogonal
		aux = self.primero
		while aux != None:
			print aux.x
			aux = aux.derecha		