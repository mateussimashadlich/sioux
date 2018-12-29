
from boneco import Boneco

class Colono_espada(Boneco):


	def __init__(self,ambiente,vida,dano,vel_x,vel_y,intervalo_ataque,\
		pos_x,pos_y,lane):

		self.colono_espada = ambiente.image.load('imagens/colono_espada/colono_espada_00.png')
		self.colono_espada_caminhando = [ambiente.image.load('imagens/colono_espada/colono_espada_01.png'),
										 ambiente.image.load('imagens/colono_espada/colono_espada_02.png')]
		self.colono_golpeando = [ambiente.image.load('imagens/colono_espada/colono_golpeando_00.png'),
								 ambiente.image.load('imagens/colono_espada/colono_golpeando_01.png')]
		self.barco = ambiente.image.load('imagens/barcos/barco_01.png')

		Boneco.__init__(self,ambiente,vida,vel_x,vel_y,intervalo_ataque,\
			pos_x,pos_y,self.colono_espada)
		self.dano = dano
		self.cont_caminhar = 0
		self.cont_golpear = 0
		self.clock_tempo_de_golpear = self.ambiente.time.get_ticks() 
		self.clock_golpear = self.ambiente.time.get_ticks()
		self.atacar_barreira = False
		self.image = self.barco.convert_alpha()
		self.vel_x = -0.05
		self.lane = lane

	def atacar(alvo):
		pass


	def animar(self):
		if self.rect.x > 820:
			pass
		else:

			self.animacao_caminhando()

	def animacao_caminhando(self):

		if self.cont_caminhar <= (len(self.colono_espada_caminhando)-1):
			self.image = self.colono_espada_caminhando[self.cont_caminhar].convert_alpha()
			self.cont_caminhar += 1

		else:
			self.image = self.colono_espada.convert_alpha()
			self.cont_caminhar = 0

	def animacao_golpeando(self):

		if self.cont_golpear <= (len(self.colono_golpeando)-1):
			self.image = self.colono_golpeando[self.cont_golpear].convert_alpha()
			self.cont_golpear += 1
		else:
			self.image = self.colono_golpeando[0].convert_alpha()
			self.cont_golpear = 0		

	def animacao_parado(self):
		self.image = self.colono_espada.convert_alpha()


