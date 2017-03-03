class Pila(object):
	def __init__(self):
		self.cima = None

	def Insertar(self, numero):
		nuevo = Nodo(numero)
		nuevo.siguiente = self.cima;
		self.cima = nuevo;

	def Quitar(self)
		if not getVacia:
			print "La pila está vacia"
		aux = self.cima.numero
		self.cima = cima.siguiente
		return aux

	def getVacia(self):
		if self.cima == None:
			return True