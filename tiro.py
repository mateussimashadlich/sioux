from objeto import Objeto


class Tiro(Objeto):


	def __init__(self,ambiente,dano,vel_x,pos_x,pos_y):
		self.tiro = ambiente.image.load('imagens/colono_atirador/tiro.png')
		Objeto.__init__(self,ambiente,pos_x,pos_y,self.tiro)
		self.dano = dano
		self.vel_x = vel_x
	
	def movimentar(self):
		self.rect.x += self.vel_x

