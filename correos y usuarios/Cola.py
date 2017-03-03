import Nodo
cn = Nodo

class Cola(object):
	def __init__(self):
		self.cabeza = None
		self.fin    = None

	def Insertar(self, numero):
            nuevo = cn.Nodo(numero)
            if self.cabeza == None:
		self.cabeza = nuevo
		self.fin = nuevo
	    else:
		self.fin.siguiente = nuevo
                self.fin = nuevo

	def Quitar(self):
		aux = Nodo
		aux = None
		if getVacio() != None:
			aux = self.cabeza
			self.cabeza = self.cabeza.siguiente
		
		return aux

	def getVacio(self):
		if self.cabeza == None:
			return True

	def ImprimirCola(self):
		temporal = self.cabeza
		while temporal!=None:
			print(temporal.numero)
			temporal = temporal.siguiente

	


