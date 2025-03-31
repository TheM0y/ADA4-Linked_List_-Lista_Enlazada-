class MiListaEnlazada:
    class Nodo:
        def __init__(self, dato):
            self.dato = dato
            self.siguiente = None

    def __init__(self):
        self.cabeza = None
    
    def insertar(self, dato):
        nuevo_nodo = self.Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
    
    def imprimir(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=' -> ')
            actual = actual.siguiente
        print('None')
