import pygame
from sprites import Sprites
from inputs import Inputs
import imagens
from colono_atirador import Colono_atirador
from colono_espada import Colono_espada
from indio import Indio
from lanca import Lanca
from barra import Barra
from corvo import Corvo
from barreira import Barreira
from random import randint
from cooldown import Cooldown
class Main:

	
	ambiente = pygame
	ambiente.init()
	sprites = Sprites(pygame)
	inputs = Inputs(ambiente)
	clock_soldados = ambiente.time.get_ticks()
	clock_corvo = ambiente.time.get_ticks()
	relogio = ambiente.time.Clock()
	

	def inicializar_jogo(self):

		self.width = 800
		self.height = 600
		self.device_screen = self.ambiente.display.Info()
		print(self.device_screen.current_w)	
		self.screen = self.ambiente.display.set_mode([self.width,self.height])
		self.background = self.ambiente.image.load('imagens/mapa.png')
	

		self.indio = Indio(self.ambiente,3,1000,0,390)
		self.cd = Cooldown(self.ambiente,20,380)

		self.barra = Barra(self.ambiente,10,540)
		self.lanca = Lanca(self.ambiente,1,0,0,20,390,0,90)
		self.barreira1 = Barreira(self.ambiente,2,400,180,imagens.barreira)
		self.barreira2 = Barreira(self.ambiente,3,400,380,imagens.barreira)
		self.sprites.barreiras.add(self.barreira1,self.barreira2)
		self.sprites.indio.add(self.indio)
		self.sprites.todos_objetos.add(self.sprites.indio,self.barra,self.sprites.barreiras)
	
	def atualizar_objetos(self):

		self.screen.blit(self.background,[0,0])	
		self.screen.blit(self.lanca.image,self.lanca.rect)
		self.screen.blit(self.indio.img_vida,[10,10])
		self.screen.blit(self.ambiente.image.load(imagens.torre),[10,446])
		self.screen.blit(self.cd.image,self.cd.rect)
		self.sprites.todos_objetos.draw(self.screen)
		self.ambiente.display.flip()


	def respawn_soldados(self,time):
		
		if self.clock_soldados + time < self.ambiente.time.get_ticks():
			colono_atirador = Colono_atirador(self.ambiente,1,-2,0,2500,self.width,465)
			colono_espada = Colono_espada(self.ambiente,1,1,-2,0,2500,self.width,160)
			self.sprites.colonos_atirador.add(colono_atirador)
			self.sprites.colonos_espada.add(colono_espada)
			self.sprites.eixo.add(colono_atirador,colono_espada)
			self.sprites.todos_objetos.add(self.sprites.colonos_atirador,self.sprites.colonos_espada,self.sprites.eixo)
			self.clock_soldados = self.ambiente.time.get_ticks()
	
	def respawn_corvo(self,time):

		if self.clock_corvo + time < self.ambiente.time.get_ticks():
			corvo = Corvo(self.ambiente,1,-3,0,600000,800,40)
			self.sprites.corvo.add(corvo)
			self.sprites.todos_objetos.add(self.sprites.corvo)
			self.clock_corvo = self.ambiente.time.get_ticks()
	
	def iniciar(self):

		self.inicializar_jogo()
		self.ambiente.key.set_repeat(5,10)
		#self.respawn(2000)
		while True:
			#print('clock_tick',self.relogio.tick())
			#print('clock_fps',self.relogio.get_fps())
			#print('corvo',self.sprites.corvo)
			#print('barreira1',self.barreira1.image.get_size()[1])
			#print('barreira1 y',self.barreira1.rect.y)
			self.ambiente.event.get()
			self.respawn_soldados(randint(5000,6000))
			self.respawn_corvo(randint(4000,10000))
			self.atualizar_objetos()
			self.sprites.interacoes(self.ambiente)
			self.inputs.checar_entradas(self.barra,self.lanca,self.sprites.lancas,self.cd,self.sprites.todos_objetos)
			#print(self.sprites.lancas)

			

main = Main()
main.iniciar()






	 

