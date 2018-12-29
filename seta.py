
from objeto import Objeto

class Seta(Objeto):


	def __init__(self,ambiente,pos_x,pos_y):
		self.seta = [ambiente.image.load('imagens/seta/seta_00.png'),
					 ambiente.image.load('imagens/seta/seta_01.png'),
					 ambiente.image.load('imagens/seta/seta_02.png'), \
					 ambiente.image.load('imagens/seta/seta_03.png'),
					 ambiente.image.load('imagens/seta/seta_04.png'),
					 ambiente.image.load('imagens/seta/seta_05.png')]
		Objeto.__init__(self,ambiente,pos_x,pos_y,self.seta[0])

	def animar(self):
		if self.cont <= (len(self.seta)-1):
			self.image = self.seta[self.cont]
			self.cont += 1
		else:
			self.cont = 0
			self.image = self.seta[0]
