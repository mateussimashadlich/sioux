import imagens
from boneco import Boneco

class Colono_atirador(Boneco):


	def __init__(self,ambiente,vida,vel_x,vel_y,intervalo_ataque,\
		pos_x,pos_y,lane):
		Boneco.__init__(self,ambiente,vida,vel_x,vel_y,intervalo_ataque,\
			pos_x,pos_y,imagens.colono_atirador)
		self.cont_caminhar = 0
		self.cont_atirar = 0
		self.atacar_barreira = False
		print(self.image.get_width())
		self.image = self.ambiente.image.load(imagens.barcos[0]).convert_alpha()
		self.vel_x = -0.1
		self.lane = lane
		self.dano = 1 

		
	def atirar():
		pass

	def animar(self):
		if self.rect.x < 1100 and self.rect.x > 900:
			self.clock_atirar = self.ambiente.time.get_ticks()
			self.vel_x = -0.3

		elif self.rect.x < 820:
			self.animacao_caminhando()


	def animar_morte(self):
		self.image = self.ambiente.image.load(imagens.colono_atirador_morto).convert_alpha()
		
	def animacao_caminhando(self):

		if self.cont_caminhar <= (len(imagens.colono_atirador_caminhando) -1):
			self.image = self.ambiente.image.load(imagens.colono_atirador_caminhando[self.cont_caminhar]).convert_alpha()
			self.cont_caminhar += 1
		else:
			self.image = self.ambiente.image.load(imagens.colono_atirador_caminhando[0]).convert_alpha()
			self.cont_caminhar = 0

	def animacao_atirando(self):

		if self.cont_atirar <= (len(imagens.colono_atirando)-1):
			self.image = self.ambiente.image.load(imagens.colono_atirando[self.cont_atirar]).convert_alpha()
			self.cont_atirar += 1
		else:
			self.image = self.ambiente.image.load(imagens.colono_atirando[0]).convert_alpha()
			self.cont_atirar = 0		

	def animacao_parado(self):
		self.image = self.ambiente.image.load(imagens.colono_atirador).convert_alpha()
