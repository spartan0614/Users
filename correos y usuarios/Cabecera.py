import NodoCabecera
primero = NodoCabecera
ultimo = NodoCabecera

class Cabecera(object):
	def __init__(self):
		self.primero = None
		self.ultimo  = None

	def Insertar(self, x):
		nuevo = NodoCabecera(x)
		if self.primero == None:
			self.primero = self.ultimo = nuevo
		else:
			if nuevo.x < self.primero.x:
				self.InsertarFrente(nuevo)
			elif nuevo.x > self.ultimo.x:
				self.InsertarFinal(nuevo)
			else:
				self.InsertarMedio(nuevo)

	def InsertarFrente(self, nuevo):
		o = NodoCabecera
		nuevo = o.NodoCabecera(x)

		self.primero.anterior = nuevo
		nuevo.siguiente = self.primero
		self.primero = self.primero.anterior

	def InsertarFinal(self, nuevo):
		r = NodoCabecera
		nuevo = r.NodoCabecera(x)

		self.ultimo.siguiente = nuevo
		nuevo.anterior = self.ultimo
		self.ultimo = self.ultimo.siguiente

	def InsertarMedio(self, nuevo):
		aux = NodoCabecera
		aux2 = NodoCabecera
		t = NodoCabecera
		nuevo = t.NodoCabecera(x)
		aux = self.primero

		while aux.x < nuevo.x:
			aux = aux.siguiente

		aux2 = aux.anterior
		aux2.siguiente = nuevo
		aux.anterior = nuevo
		nuevo.siguiente = aux
		nuevo.anterior = aux2	

	def Existe(self, x):
		aux = NodoCabecera
		aux = self.primero
		while aux != None:
			if aux.x == x:
				return True
			elif aux.siguiente == None:
				return False
		aux = aux.siguiente
		
		return False

	def Busqueda(self, x):
		if self.Existe(x):
			aux = NodoCabecera
			aux = self.primero;
			while(aux.x != x):
				aux = aux.siguiente

			return aux
		else:
			return None	

	def Recorrer(self):
		aux = NodoCabecera
		aux = self.primero
		while aux != None:
			print aux.x
			aux = aux.siguiente
