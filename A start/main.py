#Resolucion de busqueda A* / A start
#Lucia Scharff - 2020
#Obtenido del libro - INTELIGENCIA ARTIFICIAL. Fundamentos, práctica y aplicaciones
#de Alberto García



from arbol import Nodo
from math import sin, cos, acos
from functools import cmp_to_key

def compara(x, y):
  d=distancia_lineal[x.get_datos()][0]
  c1=x.get_coste()+d
  d=distancia_lineal[y.get_datos()][0]
  c2=y.get_coste()+d
  return c1-c2

def buscar_solucion_aes(conexiones, estado_inicial, solucion):
  solucionado = False
  nodos_visitados = []
  nodos_frontera = []
  nodo_inicial = Nodo(estado_inicial)
  nodo_inicial.set_coste(0)
  nodos_frontera.append(nodo_inicial)
  while(not solucionado) and len(nodos_frontera) != 0:  
    nodos_frontera = sorted(nodos_frontera, key=cmp_to_key(compara))
    nodo = nodos_frontera[0]
    nodos_visitados.append(nodos_frontera.pop(0))
    if nodo.get_datos() == solucion:
      solucionado = True 
      return nodo;
    else:
      dato_nodo = nodo.get_datos()
      lista_hijos = []
      for un_hijo in conexiones[dato_nodo]:
        hijo = Nodo(un_hijo)
        coste =conexiones[dato_nodo][un_hijo]
        hijo.set_coste(nodo.get_coste()+ coste)
        lista_hijos.append(hijo)

        if not hijo.en_lista(nodos_visitados): 
          if hijo.en_lista(nodos_frontera):
            for n in nodos_frontera:
              if n.igual(hijo) and n.get_coste() > hijo.get_coste():
                nodos_frontera.remove(n)
                nodos_frontera.append(hijo)
          else :
            nodos_frontera.append(hijo)
    
    nodo.set_hijos(lista_hijos)


if __name__ == "__main__":
  conexiones = {
    'a': {'b' : 2, 'c' : 2},
    'b': {'a': 2, 'f': 14},
    'c': {'a': 2, 'd': 4, 'g': 14},
    'd': {'c' : 4, 'e': 4,'h': 14},
    'e': {'d': 4 , 'i': 14},
    'f': {'b' : 14, 'g' : 4, 'j': 14},
    'g': {'c':14, 'f': 4, 'h': 4, 'k': 14},
    'h': {'d': 14, 'g' : 4, 'i': 4, 'n': 2.06},
    'i': {'e': 14, 'h': 4 , 'm': 14},   
    'j': {'f': 14, 'k': 4},
    'k': {'g': 14, 'j': 4 , 'l': 4},
    'l': {'n': 5.02, 'm': 4 , 'k': 4},
    'm': {'i': 14, 'l': 4},
    'n': {'h': 2.06, 'l': 5.02}
  }

  distancia_lineal = {
    'a': (33.11, 0),
    'b': (34.23, 0),
    'c': (32.34, 0),
    'd':(31.95, 0),     
    'e': (33.11, 0),
    'f': (14.29, 0),
    'g': (8.86, 0),
    'h': (7.31, 0),
    'i': (11.35, 0),   
    'j': (21.64, 0),
    'k': (18.5, 0),
    'l': (17.81, 0),
    'm': (19.82, 0),
    'n': (0, 0)
  }

estado_inicial = 'a'
solucion = 'n'
nodo_solucion = buscar_solucion_aes(conexiones, estado_inicial, solucion)

#mostrar resultado
resultado = []
nodo = nodo_solucion
while nodo.get_padre() != None:
  resultado.append(nodo.get_datos())
  nodo = nodo.get_padre()
resultado.append(estado_inicial)
resultado.reverse()
print('El automata deberia recorrer: ')
print (resultado)
print ('Coste: ' + str(nodo_solucion.get_coste()))

  
    
  
