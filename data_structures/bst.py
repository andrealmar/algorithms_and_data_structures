# coding=utf8
from __future__ import print_function


class Node:

	def __init__(self, label):
		self.label = label #possui uma chave KEY, que no caso aqui eh o label
		
		#precisamos ter os apontadores para os filhos da direita e da esquerda
		self.left = None #apontador para o filho da esquerda
		self.right = None #apontador para o filho da direita

	#metodo que retorna o nó
	def getLabel(self):
		return self.label

	#metodo que seta o nó
	def setLabel(self, label):
		self.label = label
    
    #metodo que retorna o nó da esquerda
	def getLeft(self):
		return self.left

	# metodo que seta o nó da esquerda
	def setLeft(self, left):
		self.left = left

	# metodo que retorna o nó da direita
	def getRight(self):
		return self.right

	# metodo que seta o nó da direita
	def setRight(self, right):
		self.right = right


class BinarySearchTree:

	def __init__(self):
		self.root = None

	def insert(self, label):

		#cria um novo nó
		node = Node(label)

		#verifica se a arvore está vazia. Se estiver vazia o nó que está sendo inserido é que será a raiz
		if self.empty():
			self.root = node
		else:
			#arvore nao está vazia, insere recursivamente
			dad_node = None

			#começa sempre do node, se eh maior vai para direita, se eh menor vai para a esquerda
			curr_node = self.root

			while True:

				# se o nó corrente for diferente de None, eu continuo percorrendo a árvore binãria de busca
				if curr_node != None:

					# tenho que guardar a referência do pai
					dad_node = curr_node

					#verifica se vai para a esquerda ou direita
					if node.getLabel() < curr_node.getLabel():
						#vai para a esquerda
						curr_node = curr_node.getLeft()
					else:
						# vai para a direita
						curr_node = curr_node.getRight()
				else:

					#se o curr_node = None, então encontrou aonde inserir

					# se o filho que estiver sendo inserido for MENOR que o pai, insira à esquerda do pai
					if node.getLabel() < dad_node.getLabel():
						dad_node.setLeft(node)
					# senão, se o filho que estiver sendo inserido for MAIOR que o pai, insira à direita do pai
					else:
						dad_node.setRight(node)

					break #sai do loop

	# verifica se a árvore está vazia. Verifica se a raiz for None então retorna True (ela estã vazia) senão, ela não está vazia
	def empty(self):
		if self.root == None:
			return True
		else:
			return False

	# mostra em pre-ordem (raiz --> esq --> dir)
	def show(self, curr_node):
		if curr_node != None:
			print('%d' % curr_node.getLabel(), end=" ") # to use end=' ' you must: from __future__ import print_function
			self.show(curr_node.getLeft())
			self.show(curr_node.getRight())

	def getRoot(self):
		return self.root

	def remove(self, label):
		pass

		'''
		remoção tem 3 casos
		caso 1 - qdo o nó a ser removido nao tem filhos (nó folha). Basta setar a ligação do pai para None/Null
		caso 2 - qdo o nó a ser removido tem somente UM filho. basta colocar o nó filho no lugar do Pai
		caso 3 - qdo o nó a ser removido possui DOIS filhos(Filho a esquerda e à direita). nesse caso basta pegar o menor 
		         elemento da sub-árvore à direita
		'''

		dad_node = None # parent
		curr_node = self.root # raiz

		while curr_node != None:

			#verifica se encontrou o nó a ser removido
			if label == curr_node.getLabel():
				# caso 1 - qdo o nó a ser removido nao tem filhos (nó folha). Basta setar a ligação do pai para None/Null
				if curr_node.getLeft == None and curr_node.getRight() == None:
					#verifica se eh a raiz. Significa que só tem um nó. 
					if dad_node == None:
						self.root = None
					else:
						#verifica se eh filho à esquerda ou à direita
						if dad_node.getLeft == curr_node:
							dad_node.setLeft(None)
						elif dad_node.getRight() == curr_node:
							dad_node.setRight(None)


				# caso 2 - qdo o nó a ser removido tem somente UM filho. basta colocar o nó filho no lugar do Pai
				elif (curr_node.getLeft() == None and curr_node.getRight() != None) or (curr_node.getLeft() != None and curr_node.getRight() == None):
					#verifica se o nó a ser removido é a raiz
					if dad_node == None:
						#verifica se o filho de curr_node é filho à esquerda
						if curr_node.getLeft() != None:
							self.root = curr_node.getLeft()
						else: #senão o filho de curr_node eh filho à direita
							self.root = curr_node.getRight()
					else:
						#se não for a raiz...
						pass

'''	

t = BinarySearchTree()
t.insert(8)
t.insert(3)
t.insert(1)
t.insert(6)
t.insert(4)
t.insert(7)
t.insert(10)
t.insert(14)
t.insert(13)

t.show(t.getRoot())

LÓGICA
-----------------------------------
if value to be inserted < this key

  go left

else go right

if insertion point is found

  create new vertex/node

----------------------------------

'''