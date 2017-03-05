import NodoOrtogonal


class ListaVertical:
	def __init__(self):
		self.primero = None
		self.ultimo  = None

	def Insertar(self, nuevo):  #nuevo: tipo Nodo Ortogonal
		ort = NodoOrtogonal
		nuevo = ort.NodoOrtogonal(x, y, nombre)
		if self.primero == None:
			self.primero = self.ultimo = nuevo;
		else:
			if nuevo.y < self.primero.y:
				self.InsertarFrente(nuevo)
			elif nuevo.y > ultimo.y:
				self.InsertarFinal(nuevo)
			else:
				self.InsertarMedio(nuevo)
				

	def InsertarFrente(self, nuevo):
		o = NodoOrtogonal
		nuevo = o.NodoOrtogonal(x, y, nombre)
		self.primero.arriba = nuevo
		nuevo.abajo = self.primero
		self.primero = self.primero.arriba

	def InsertarFinal(self, nuevo):
		r = NodoOrtogonal
		nuevo = r.NodoOrtogonal(x, y, nombre)
		self.ultimo.abajo = nuevo
		nuevo.arriba = self.ultimo
		self.ultimo = self.ultimo.abajo

	def InsertarMedio(self, nuevo):
		aux = NodoOrtogonal
		aux2 = NodoOrtogonal
		t = NodoOrtogonal
		nuevo = t.NodoOrtogonal(x, y, nombre)
		aux = self.primero

		while aux.y < nuevo.y:
			aux = aux.abajo

		aux2 = aux.arriba
		aux2.abajo = nuevo
		aux.arriba = nuevo
		nuevo.abajo = aux
		nuevo.arriba = aux2
	
	def Recorrer(self):
		aux = NodoCabecera
		aux = self.primero
		while aux != None:
			print aux.y
			aux = aux.abajo			
	

	def Vacia(self):
		if self.primero ==  None:
			return True
