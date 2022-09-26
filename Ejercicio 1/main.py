from arbol import Arbol

if __name__ == "__main__":
    unArbol = Arbol()
    '''
    num = input("\nIngrese un elemento al arbol:")
    while num != "salir":
        unArbol.Insertar(unArbol.getRaiz(),int(num))
        num = input("\nIngrese otro elemento al arbol, 'salir' para finalizar:")
    unArbol.Inorder(unArbol.getRaiz())
    '''
    unArbol.Insertar(unArbol.getRaiz(),5)
    unArbol.Insertar(unArbol.getRaiz(),7)
    unArbol.Insertar(unArbol.getRaiz(),8)
    unArbol.Insertar(unArbol.getRaiz(),6)
    unArbol.Insertar(unArbol.getRaiz(),3)
    unArbol.Insertar(unArbol.getRaiz(),2)
    unArbol.Insertar(unArbol.getRaiz(),4)
    unArbol.Insertar(unArbol.getRaiz(),1)
    unArbol.Insertar(unArbol.getRaiz(),10)
    unArbol.Inorder(unArbol.getRaiz())
    num = int(input("\nIngrese el numero a eliminar:"))
    unArbol.suprimir(unArbol.getRaiz(),num)
    unArbol.Inorder(unArbol.getRaiz())
    num = int(input("\nIngrese el numero a buscar entre los nodos:"))
    nodoEnc = unArbol.buscar(unArbol.getRaiz(), num)
    print("\nLa direccion de memoria del nodo buscado es:{} y el valor es:{}".format(nodoEnc, nodoEnc.getItem()))
    unArbol.Nodoterminal(unArbol.getRaiz())