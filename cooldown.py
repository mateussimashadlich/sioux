from objeto import Objeto
import imagens

class Cooldown(Objeto):


	def __init__(self,ambiente,pos_x,pos_y):
		self.cd_ready = ambiente.image.load('imagens/cd/ready.png').convert_alpha()
		self.cd = [ambiente.image.load('imagens/cd/cd_01.png'),ambiente.image.load( 'imagens/cd/cd_02.png'),\
				   ambiente.image.load('imagens/cd/cd_03.png'), ambiente.image.load('imagens/cd/cd_04.png'),\
				   ambiente.image.load('imagens/cd/cd_05.png'), ambiente.image.load('imagens/cd/cd_06.png'),\
				   ambiente.image.load('imagens/cd/cd_07.png'), ambiente.image.load('imagens/cd/cd_08.png'), \
				   ambiente.image.load('imagens/cd/cd_09.png'), ambiente.image.load('imagens/cd/cd_10.png'),\
				   ambiente.image.load('imagens/cd/cd_11.png'), ambiente.image.load('imagens/cd/cd_12.png'),\
				   ambiente.image.load('imagens/cd/cd_13.png'), ambiente.image.load('imagens/cd/cd_14.png'),\
				   ambiente.image.load('imagens/cd/cd_15.png'), ambiente.image.load('imagens/cd/cd_16.png'),\
				   ambiente.image.load('imagens/cd/cd_17.png'), ambiente.image.load('imagens/cd/cd_18.png'),\
				   ambiente.image.load('imagens/cd/cd_19.png')]
		Objeto.__init__(self,ambiente,pos_x,pos_y,self.cd_ready)

		self.cont_img = 0
		self.ativo = False
		self.intervalo = self.ambiente.time.get_ticks()
		
	def animar(self):
		if self.cont_img <= (len(self.cd)-1):
			self.image = self.cd[self.cont_img]
			self.cont_img += 1
		else:
			self.image = self.cd_ready
			self.cont_img = 0
			self.ativo = False
			
		
	