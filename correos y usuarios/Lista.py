class Lista:
	def __init__(self):
		self.cabeza = None

	def Agregar(self, indice, palabra):
		nuevo = NodoLista(indice, palabra)
		if self.cabeza == None:
			self.cabeza = nuevo
		else:
			aux = self.cabeza
			while aux.siguiente != None:
				aux = aux.siguiente
		aux.siguiente = nuevo		
	
	def Buscar(self, k):
		aux = self.cabeza
		if aux != None:
			while aux.siguiente != None:
				if ( aux.palabra == k) :
					return aux
				aux = aux.siguiente
			if ( aux.palabra == k ) :
				return aux
		return None
			 	
	def Eliminar(self, p):
		