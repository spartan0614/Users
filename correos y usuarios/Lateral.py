import NodoLateral
primero = NodoLateral
ultimo = NodoLateral

class Lateral(object):
	def __init__(self):
		self.primero = None
		self.ultimo = None

	def Insertar(self, y):
		c = NodoLateral
		nuevo = c.NodoLateral(y)
		if self.primero == None:
			self.primero = self.ultimo = nuevo
		else:
			if nuevo.y < self.primero.y:
				self.InsertarFrente(nuevo)
			elif nuevo.y > self.ultimo.y:
				self.InsertarFinal(nuevo)
			else:
				self.InsertarMedio(nuevo)

	def InsertarFrente(self, nuevo):
		o = NodoLateral
		nuevo = o.NodoLateral(y)

		self.primero.anterior = nuevo
		nuevo.siguiente = self.primero
		self.primero = self.primero.anterior

	def InsertarFinal(self, nuevo):
		r = NodoLateral
		nuevo = r.NodoLateral(y)

		self.ultimo.siguiente = nuevo
		nuevo.anterior = self.ultimo
		self.ultimo = self.ultimo.siguiente

	def InsertarMedio(self, nuevo):
		aux = NodoLateral
		aux2 = NodoLateral
		t = NodoLateral
		nuevo = t.NodoLateral(y)
		aux = self.primero

		while aux.y < nuevo.y:
			aux = aux.siguiente

		aux2 = aux.anterior
		aux2.siguiente = nuevo
		aux.anterior = nuevo
		nuevo.siguiente = aux
		nuevo.anterior = aux2	

	def Existe(self, y):
		aux = NodoLateral
		aux = self.primero
		while aux != None:
			if aux.y == y:
				return True
			elif aux.siguiente == None:
				return False
		aux = aux.siguiente
		
		return False

	def Busqueda(self, y):
		if self.Existe(y):
			aux = NodoLateral
			aux = self.primero;
			while(aux.y != y):
				aux = aux.siguiente

			return aux
		else:
			return None	

	def Recorrer(self):
		aux = NodoLateral
		aux = self.primero
		while aux != None:
			print aux.y
			aux = aux.siguiente

