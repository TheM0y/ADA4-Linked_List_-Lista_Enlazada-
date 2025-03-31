from MyLinkedList import MiListaEnlazada

lista = MiListaEnlazada()
num_datos = int(input("¿Cuántos datos desea ingresar? "))
for _ in range(num_datos):
    dato = input("Ingrese un dato: ")
    lista.insertar(dato)

lista.imprimir()
