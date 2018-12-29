from boneco import Boneco


class Indio(Boneco):

	def __init__(self,ambiente,vida,intervalo_ataque,pos_x,pos_y):
		self.indio = ambiente.image.load('imagens/indio_0º.png').convert_alpha()
		self.vida_0 = ambiente.image.load('imagens/vidas/vida_0.png').convert_alpha()
		self.vida_1 = ambiente.image.load('imagens/vidas/vida_1.png').convert_alpha()
		self.vida_2 = ambiente.image.load('imagens/vidas/vida_2.png').convert_alpha()
		self.vida_3 = ambiente.image.load('imagens/vidas/vida_3.png').convert_alpha()
		Boneco.__init__(self,ambiente,vida,0,0, intervalo_ataque,pos_x,pos_y,self.indio)
		self.angulo_lanca = 0
		self.img_vida = self.vida_3

	def atirar_lanca(self):
		pass

	def perder_vida(self,dano_sofrido):
		self.vida -= dano_sofrido

		if self.vida == 2:
			self.img_vida = self.vida_2.convert_alpha()
		elif self.vida == 1:
			self.img_vida = self.vida_1.convert_alpha()
		else:
			self.img_vida = self.vida_0.convert_alpha()