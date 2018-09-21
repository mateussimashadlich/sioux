import imagens
from boneco import Boneco
from objeto import Objeto
class Barreira(Objeto):

	def __init__(self,ambiente,vida,pos_x,pos_y,image):
		Objeto.__init__(self,ambiente,pos_x,pos_y,image)
		self.vida = vida

	def perder_vida(self,dano):
		self.vida -= dano

