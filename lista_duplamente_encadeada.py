
# ------------ PROJETO DE ESTUDO DE LISTA DUPLAMENTE ENCADEADA ------------


class Node:     # Criano a Classe Nodo
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class Lista:
    def __init__ (self):    # INICIANDO A LISTA
        self.head = None
        self.tail = None

    def vazia(self):
        if self.head is None:
            return True
        return False
        
    def addEnd(self, data):
        novo_nodo = Node(data)

        if self.head is None:       # EM CASO DE LISTA VAZIA
            self.head = novo_nodo
            self.tail = novo_nodo
            return
        else:
            novo_nodo.previous = self.tail
            self.tail.next = novo_nodo
            self.tail = novo_nodo

    def mostrarLista(self):
        conteudo = self.head

        if conteudo is None:
            print("LISTA VAZIA")

        while conteudo:
            print(conteudo.data)
            conteudo = conteudo.next
        print("--- FIM DA LISTA ---")

l = Lista()
l.addEnd(3)
l.addEnd(2)
l.addEnd(1)
l.addEnd(5)

l.mostrarLista()
        

        
