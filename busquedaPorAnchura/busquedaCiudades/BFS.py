#Resolucion de busqueda en anchura 
#Lucia Scharff - 2020
#Obtenido del libro - INTELIGENCIA ARTIFICIAL. Fundamentos, práctica y aplicaciones
#Por Alberto García

from arbol import Nodo

def buscar_solucion_BFS(conexiones, estado_inicial, solucion):
    solucionado = False
    nodo_inicial = Nodo(estado_inicial)
    nodos_frontera = []
    nodos_visitados = []

    nodos_frontera.append(nodo_inicial)
    print("Puntero:")

    while (not solucionado) and len(nodos_frontera) != 0:

        nodo = nodos_frontera.pop()
        nodos_visitados.append(nodo)
        print(nodo.get_datos())
        if nodo.get_datos() == solucion:
            solucionado = True
            return nodo
        else:
            dato_nodo = nodo.get_datos()
            lista_hijos = []

            for un_hijo in conexiones[dato_nodo]:
                hijo = Nodo(un_hijo)
                lista_hijos.append(hijo)
                if (not hijo.en_lista(nodos_visitados)
                        and not hijo.en_lista(nodos_frontera)):
                    nodos_frontera.append(hijo)
                    nodo.set_hijos(lista_hijos)


if __name__ == '__main__':
    conexiones = {
        'malaga': {'salamanca', 'madrid', 'barcelona'},
        'salamanca': {'malaga', 'madrid'},
        'madrid': {'sevilla', 'salamanca', 'malaga', 'santander', 'barcelona'},
        'barcelona': {'zaragoza', 'santiago', 'madrid', 'malaga', 'valencia'},
        'sevilla': {'madrid', 'santiago'},
        'santander': {'madrid', 'santiago'},
        'valencia': {'barcelona', 'granada'},
        'granada': {'valencia'},
        'zaragoza': {'barcelona'},
        'santiago': {'sevilla', 'santander', 'barcelona'}
    }
    estado_inicial = str('malaga')
    solucion = str('santiago')
    nodo_solucion = buscar_solucion_BFS(conexiones, estado_inicial, solucion)

    resultado = []
    nodo = nodo_solucion

    while nodo.get_padre() != None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    resultado.append(estado_inicial)

    resultado.reverse()
    print("Recorrido:")
    print(resultado)