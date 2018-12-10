import pygame
import random
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
from seta import Seta
from mss import mss
import peewee
import cProfile


class Main:
	

	def inicializar_jogo(self):

		self.ambiente = pygame
		self.ambiente.init()
		self.sprites = Sprites(pygame)
		self.inputs = Inputs(self.ambiente)
		self.clock_soldados_atiradores = self.ambiente.time.get_ticks()
		self.clock_soldados_espada = self.ambiente.time.get_ticks()
		self.clock_corvo = self.ambiente.time.get_ticks()
		self.paused = False
		self.cont_background = 0
		self.width = 1280
		self.height = 768
		self.device_screen = self.ambiente.display.Info()
		print(self.device_screen.current_w)	
		self.screen = self.ambiente.display.set_mode([self.width,self.height],self.ambiente.FULLSCREEN | self.ambiente.DOUBLEBUF)
		self.background_imgs = imagens.mapa
		self.background_image = self.ambiente.image.load(imagens.mapa[0]).convert()	
		self.indio = Indio(self.ambiente,3,1000,0,510)
		self.cd = Cooldown(self.ambiente,20,490)
		self.barra = Barra(self.ambiente,10,650)
		self.lanca = Lanca(self.ambiente,1,0,0,20,510,0,90)
		self.barreira1 = Barreira(self.ambiente,2,400,300,'top',imagens.barreira)
		self.barreira2 = Barreira(self.ambiente,3,400,500,'bot',imagens.barreira)
		self.sprites.barreiras.add(self.barreira1,self.barreira2)
		self.sprites.indio.add(self.indio)
		self.sprites.todos_objetos.add(self.sprites.indio,self.barra,self.sprites.barreiras)
		self.clock_mapa = self.ambiente.time.get_ticks()
		self.time = self.ambiente.time.get_ticks()
		self.seta_menu = Seta(self.ambiente,350,200)
		self.ambiente.font.init()
		self.fonte = self.ambiente.font.SysFont('Comic Sans MS',30)
	
	def atualizar_background(self):
		#self.screen.blit(self.ambiente.image.load(self.background[self.cont_background]),[0,0])
		if self.clock_mapa + 500 < self.ambiente.time.get_ticks():

			if self.background_imgs[self.cont_background] != self.background_imgs[-1]:
				self.cont_background += 1
			else:
				self.cont_background = 0

			self.background_image = self.ambiente.image.load(self.background_imgs[self.cont_background]).convert() 
			self.clock_mapa = self.ambiente.time.get_ticks()

	def atualizar_objetos(self):

		self.atualizar_background()
		#self.screen.blit(self.ambiente.image.load(self.background[self.cont_background]).convert(),[0,0])	
		self.screen.blit(self.background_image,[0,0])
		self.screen.blit(self.lanca.image,self.lanca.rect)
		self.screen.blit(self.indio.img_vida,[10,10])
		self.screen.blit(self.ambiente.image.load(imagens.torre),[10,566])
		self.screen.blit(self.cd.image,self.cd.rect)
		self.screen.blit(self.fonte.render('Score: ' + str(self.sprites.score),False,(255,0,0,0)),(1080,20))
		self.sprites.todos_objetos.draw(self.screen)
		self.ambiente.display.flip()


	def respawn_soldados(self,lane1,lane2):

		lanes = [lane1,lane2]
		random.shuffle(lanes)

		if self.clock_soldados_espada + self.time_respawn_espada < self.ambiente.time.get_ticks():
			if lanes[1] == 'bot':
				colono_espada = Colono_espada(self.ambiente,1,1,-0.08,0,2500,self.width,525,lanes[1])
			else:
				colono_espada = Colono_espada(self.ambiente,1,1,-0.08,0,2500,self.width,300,lanes[1])
			self.sprites.colonos_espada.add(colono_espada)
			self.sprites.eixo.add(colono_espada)
			self.sprites.todos_objetos.add(self.sprites.colonos_espada,self.sprites.eixo)
			self.clock_soldados_espada = self.ambiente.time.get_ticks()
			self.time_respawn_espada = random.randrange(5000,6500)

		if self.clock_soldados_atiradores + self.time_respawn_atirador < self.ambiente.time.get_ticks():
			if lanes[0] == 'bot' and lanes[1] == lanes[0]:
				colono_atirador = Colono_atirador(self.ambiente,1,-0.08,0,2500,self.width,300,'top')
			elif lanes[0] == 'top' and lanes[1] == lanes[0]:
				colono_atirador = Colono_atirador(self.ambiente,1,-0.08,0,2500,self.width,525,'bot')
			elif lanes[0] == 'top':
				colono_atirador = Colono_atirador(self.ambiente,1,-0.08,0,2500,self.width,300,lanes[0])
			else:
				colono_atirador = Colono_atirador(self.ambiente,1,-0.08,0,2500,self.width,525,lanes[0])
				
			self.sprites.colonos_atirador.add(colono_atirador)
			self.sprites.eixo.add(colono_atirador)
			self.sprites.todos_objetos.add(self.sprites.colonos_atirador,self.sprites.eixo)
			self.clock_soldados_atiradores = self.ambiente.time.get_ticks()
			self.time_respawn_atirador = random.randrange(6000,8500)
	
		'''
		if self.clock_soldados + time2 < self.ambiente.time.get_ticks():
				colono_atirador = Colono_atirador(self.ambiente,1,-0.08,0,2500,self.width,525,lanes[0])
				colono_espada = Colono_espada(self.ambiente,1,1,-0.08,0,2500,self.width,320,lanes[1])
				self.sprites.colonos_atirador.add(colono_atirador)
				self.sprites.colonos_espada.add(colono_espada)
				self.sprites.eixo.add(colono_atirador,colono_espada)
				self.sprites.todos_objetos.add(self.sprites.colonos_atirador,self.sprites.colonos_espada,self.sprites.eixo)
				self.clock_soldados_atiradores = self.ambiente.time.get_ticks()
		'''
	def respawn_corvo(self,time):

		if self.clock_corvo + time < self.ambiente.time.get_ticks():
			corvo = Corvo(self.ambiente,1,-0.6,0,600000,1280,100)
			self.sprites.corvo.add(corvo)
			self.sprites.todos_objetos.add(self.sprites.corvo)
			self.clock_corvo = self.ambiente.time.get_ticks()
	
	def paused(self):

		paused = True

		while paused:
			for event in pygame.event.get():
				if event.type == self.ambiente.KEYDOWN:
					if event.key == self.ambiente.K_x:
						self.paused = False
						self.ambiente.time.wait(1)

	def salvar_pontos(self):
		fonte = self.ambiente.font.SysFont('Comic Sans MS',30)
		scorecolumn = fonte.render('Pontuação',False,(0,0,0))
		idcolumn = fonte.render('Posição',False,(0,0,0))
		self.screen.blit(idcolumn,(500,20))
		self.screen.blit(scorecolumn,(650,20))
		pos_y = 70
		positions = [1,2,3,4,5,6,7,8,9,10]
		scores = []
		for i in Player.select():
			#self.ambiente.draw.rect(self.background_image,(255,255,255),1200)
			scores.append(i.score)
			scores = sorted(scores,reverse=True) #Decrescente
		for position in positions:
			idsurface = fonte.render(str(position),False,(255,0,0))
			self.screen.blit(idsurface,(500,pos_y))
			pos_y += 65
			
		pos_y = 70	
		for score in scores:
			scoresurface = fonte.render(str(score),False,(255,0,0))
			self.screen.blit(scoresurface,(650,pos_y))
			pos_y += 65
			if score == scores[9]:
				break
			self.ambiente.display.flip()


	def menu(self):
		self.option = 0
		paused_menu = True
		escolha = False
		self.screen.blit(self.ambiente.image.load(imagens.menu_background),[0,0])
		self.screen.blit(self.seta_menu.image,self.seta_menu.rect)
		self.ambiente.display.flip()
		while paused_menu:
			self.ambiente.event.get()
			self.seta_menu.animar()
			self.ambiente.display.flip()
			#self.ambiente.screen.blit(imagens.menu,[0,0]) A implementar !!
			for event in self.ambiente.event.get():
				if event.type == self.ambiente.KEYUP:
					if event.key == self.ambiente.K_DOWN and self.option < 3 and escolha == False:
						self.option += 1
						self.seta_menu.rect.y += 120
						self.screen.blit(self.ambiente.image.load(imagens.menu_background),[0,0])
						self.screen.blit(self.seta_menu.image,self.seta_menu.rect)			
						print("aisss")
						print('option kdown',self.option)
					
					elif event.key == self.ambiente.K_UP and self.option > 0 and escolha == False:
						self.option -= 1
						self.seta_menu.rect.y -= 120
						self.screen.blit(self.ambiente.image.load(imagens.menu_background),[0,0])
						self.screen.blit(self.seta_menu.image,self.seta_menu.rect)	
						print('jjsasa')
						print('option kup', self.option)
					
					elif event.key == self.ambiente.K_ESCAPE and escolha == True:
						self.screen.blit(self.ambiente.image.load(imagens.menu_background),[0,0])
						self.screen.blit(self.seta_menu.image,self.seta_menu.rect)
						escolha = False
					

					#JOGAR
					elif event.key == self.ambiente.K_RETURN and self.option == 0 and escolha == False:
						self.ambiente.time.wait(500)
						paused_menu = False
						if self.paused == False:
							self.iniciar()

					#TOP10
					elif event.key == self.ambiente.K_RETURN and self.option == 2 and escolha == False:
						self.screen.blit(self.ambiente.image.load(imagens.mapa[0]),[0,0])
						self.ambiente.time.wait(500)
						self.salvar_pontos()
						
						escolha = True
					
					#SAIR
					
					elif event.key == self.ambiente.K_RETURN and self.option == 3 and escolha == False:
						Player.create(score=self.sprites.score)
						return exit()

					
					#INSTRUÇÕES
					'''
					elif event.key == self.ambiente.K_RETURN and self.option == 2 and escolha == False:
						self.ambiente.time.wait(1000)
						self.screen.blit(self.ambiente.image.load(imagens.instrucoes),(0,0))
						self.ambiente.display.flip()
						escolha = True
					'''
		
					

					



						


	def iniciar(self):

		self.time_respawn_espada = random.randrange(5000,6500)
		self.time_respawn_atirador = random.randrange(5000,8000)

		self.inicializar_jogo()
		self.ambiente.key.set_repeat(5,10)
		self.ambiente.mixer.music.load('sounds/runtothehills8bits.mp3')
		self.ambiente.mixer.music.play()
		self.ambiente.mixer.music.set_volume(0.1)
		paused_menu = False
		
		while not paused_menu:
			self.ambiente.event.get()
			self.respawn_soldados('bot','top')
			self.respawn_corvo(randint(4000,10000))
			self.atualizar_objetos()
			if self.sprites.interacoes(self.ambiente) == 'Perdeu':
				self.menu()
			if self.inputs.checar_entradas(self.barra,self.lanca,self.sprites.lancas,self.cd,self.sprites.todos_objetos) == 'pause':
				self.paused = True
				self.menu()
			if not self.ambiente.mixer.music.get_busy():
				self.ambiente.mixer.music.rewind()
			
			if self.indio.vida == 0:
				self.indio.kill()
				self.lanca.kill()
				Player.create(score=self.sprites.score)
				self.atualizar_objetos()
				game_over = True
				while game_over:
					self.ambiente.time.wait(1000)
					game_over = False
					self.menu()
					#self.ambiente.screen.blit(imagens.game_over,[0,0]) A implementar !!
					for event in self.ambiente.event.get():
						if event.type == self.ambiente.KEYDOWN:
							if event.key == self.ambiente.K_RETURN:
								game_over = False
								self.ambiente.time.wait(1000)
								self.menu()
								


db = peewee.SqliteDatabase('sioux.db')

class Player(peewee.Model):

	score = peewee.IntegerField()

	class Meta:
		database = db

db.create_tables([Player])

			

main = Main()
main.iniciar()
'''
except Exception as error:
	with mss() as sct:
		filename = sct.shot()
		print(filename)
		print(error)
'''



	 

