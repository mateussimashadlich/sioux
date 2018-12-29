import imagens
from objeto import Objeto

class Barra(Objeto):


	def __init__(self,ambiente,pos_x,pos_y):
		self.barra = [ambiente.image.load('imagens/barra/barra00.png'),
					  ambiente.image.load('imagens/barra/barra01.png'),
					  ambiente.image.load('imagens/barra/barra02.png'), \
					  ambiente.image.load('imagens/barra/barra03.png'),
					  ambiente.image.load('imagens/barra/barra04.png'),
					  ambiente.image.load('imagens/barra/barra05.png'), \
					  ambiente.image.load('imagens/barra/barra06.png'),
					  ambiente.image.load('imagens/barra/barra07.png'),
					  ambiente.image.load('imagens/barra/barra08.png'), \
					  ambiente.image.load('imagens/barra/barra09.png'),
					  ambiente.image.load('imagens/barra/barra10.png'),
					  ambiente.image.load('imagens/barra/barra11.png'), \
					  ambiente.image.load('imagens/barra/barra12.png'),
					  ambiente.image.load('imagens/barra/barra13.png'),
					  ambiente.image.load('imagens/barra/barra14.png'), \
					  ambiente.image.load('imagens/barra/barra15.png'),
					  ambiente.image.load('imagens/barra/barra16.png'),
					  ambiente.image.load('imagens/barra/barra17.png'), \
					  ambiente.image.load('imagens/barra/barra18.png'),
					  ambiente.image.load('imagens/barra/barra19.png'),
					  ambiente.image.load('imagens/barra/barra20.png'), \
					  ambiente.image.load('imagens/barra/barra21.png'),
					  ambiente.image.load('imagens/barra/barra22.png'),
					  ambiente.image.load('imagens/barra/barra23.png'), \
					  ambiente.image.load('imagens/barra/barra24.png'),
					  ambiente.image.load('imagens/barra/barra25.png'),
					  ambiente.image.load('imagens/barra/barra26.png'), \
					  ambiente.image.load('imagens/barra/barra27.png'),
					  ambiente.image.load('imagens/barra/barra28.png'),
					  ambiente.image.load('imagens/barra/barra29.png')]
		Objeto.__init__(self,ambiente,pos_x,pos_y,self.barra[0])
		self.energia = 0
		self.cont_img = 0
		self.cont_img2 = 0
	
	def aumentar_energia(self,valor):
		self.energia += valor

	def zerar_energia(self):

		self.energia = 0
		self.cont_img = 0
		self.image = self.barra[self.cont_img]
		
	def animar(self):
		if self.cont_img <= (len(self.barra)-1):
			self.image = self.barra[self.cont_img]
			self.cont_img += 1
		else:
			self.cont_img = 0
			
			




		