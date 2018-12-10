import imagens
from boneco import Boneco
from objeto import Objeto
class Barreira(Objeto):


	def __init__(self,ambiente,vida,pos_x,pos_y,lane,image):
		Objeto.__init__(self,ambiente,pos_x,pos_y,image)
		self.vida = vida
		self.lane = lane

	def perder_vida(self,dano):
		self.vida -= dano

