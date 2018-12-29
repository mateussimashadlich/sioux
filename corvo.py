
from boneco import Boneco



class Corvo(Boneco):

	def __init__(self,ambiente,vida,vel_x,vel_y,intervalo_ataque,\
		pos_x,pos_y):
		self.corvo = [ambiente.image.load('imagens/corvo/corvo1.png').convert_alpha(),
					  ambiente.image.load('imagens/corvo/corvo2.png').convert_alpha()]
		self.cont_voar = 0
		Boneco.__init__(self,ambiente,vida,vel_x,vel_y,intervalo_ataque,\
		pos_x,pos_y,self.corvo[0])


	def animar(self):

		if self.cont_voar <= (len(self.corvo) -1):
			self.image = self.corvo[self.cont_voar]
			self.cont_voar += 1
		else:
			self.image = self.corvo[0]
			self.cont_voar = 0

