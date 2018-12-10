import imagens
from boneco import Boneco

class Colono_espada(Boneco):


	def __init__(self,ambiente,vida,dano,vel_x,vel_y,intervalo_ataque,\
		pos_x,pos_y,lane):
		Boneco.__init__(self,ambiente,vida,vel_x,vel_y,intervalo_ataque,\
			pos_x,pos_y,imagens.colono_espada)
		self.dano = dano
		self.cont_caminhar = 0
		self.cont_golpear = 0
		self.clock_tempo_de_golpear = self.ambiente.time.get_ticks() 
		self.clock_golpear = self.ambiente.time.get_ticks()
		self.atacar_barreira = False
		self.image = self.ambiente.image.load(imagens.barcos[1]).convert_alpha()
		self.vel_x = -0.1
		self.lane = lane

	def atacar(alvo):
		pass


	def animar(self):
		if self.rect.x > 820:
			pass
		else:
			self.vel_x = -0.4
			self.animacao_caminhando()

	def animacao_caminhando(self):

		if self.cont_caminhar <= (len(imagens.colono_espada_caminhando)-1):
			self.image = self.ambiente.image.load(imagens.colono_espada_caminhando[self.cont_caminhar]).convert_alpha()
			self.cont_caminhar += 1

		else:
			self.image = self.ambiente.image.load(imagens.colono_espada).convert_alpha()
			self.cont_caminhar = 0

	def animacao_golpeando(self):

		if self.cont_golpear <= (len(imagens.colono_golpeando)-1):
			self.image = self.ambiente.image.load(imagens.colono_golpeando[self.cont_golpear]).convert_alpha()
			self.cont_golpear += 1
		else:
			self.image = self.ambiente.image.load(imagens.colono_golpeando[0]).convert_alpha()
			self.cont_golpear = 0		

	def animacao_parado(self):
		self.image = imagens.colono_espada.convert_alpha()


