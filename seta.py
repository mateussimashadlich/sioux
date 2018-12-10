import imagens
from objeto import Objeto

class Seta(Objeto):


	def __init__(self,ambiente,pos_x,pos_y):
		Objeto.__init__(self,ambiente,pos_x,pos_y,imagens.seta[0])

	def animar(self):
		if self.cont <= (len(imagens.seta)-1):
			self.image = self.ambiente.image.load(imagens.seta[self.cont])
			self.cont += 1
		else:
			self.cont = 0
			self.image = self.ambiente.image.load(imagens.seta[0])
