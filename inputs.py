
from sprites import Sprites
from copy import copy
from lanca import Lanca
class Inputs:


	def __init__(self,ambiente):
		self.ambiente = ambiente
		print('ó o ambiente ai', self.ambiente)

	def checar_entradas(self,barra,lanca,group_lancas,cd,todos_objetos):
		
		key = self.ambiente.key.get_pressed()
		
		for event in self.ambiente.event.get():	
			
			if event.type == self.ambiente.KEYDOWN:
				if key[self.ambiente.K_SPACE]:
					self.espaco(barra)
				
				elif key[self.ambiente.K_UP]:
					self.key_up(lanca)
					print('angulo',lanca.angulo)
				elif key[self.ambiente.K_DOWN]:
					self.key_down(lanca)
					print('angulo',lanca.angulo)
				elif event.key == self.ambiente.K_z:
					exit()
				elif event.key == self.ambiente.K_q:
					self.ambiente.mixer.music.pause()

				elif event.key == self.ambiente.K_e:
					self.ambiente.mixer.music.unpause()

				elif event.key == self.ambiente.K_ESCAPE:
					paused = True
					self.ambiente.time.wait(500)
					return 'pause'
					while paused:
						#self.ambiente.screen.blit(imagens.paused,[0,0]) A implementar!!
						for event in self.ambiente.event.get():
							if event.type == self.ambiente.KEYDOWN:
								if event.key == self.ambiente.K_ESCAPE:
									paused = False
									self.ambiente.time.wait(500)
								'''
								if event.key == self.ambiente.K_RETURN:
									paused_menu = True
									while paused_menu:
										#self.ambiente.screen.blit(imagens.menu,[0,0]) A implementar !!
										for event in self.ambiente.event.get():
											if event.type == self.ambiente.KEYDOWN:
												if event.key == self.ambiente.K_RETURN:
													paused_menu = False
													paused = False
								'''
				elif event.key == self.ambiente.K_x:
					self.ambiente.mixer.music.set_volume(self.ambiente.mixer.music.get_volume()-0.1)
				elif event.key == self.ambiente.K_c:
					self.ambiente.mixer.music.set_volume(self.ambiente.mixer.music.get_volume()+0.1)	




			if event.type == self.ambiente.KEYUP:
				if event.key == self.ambiente.K_SPACE:
					if lanca.cd + 500 < self.ambiente.time.get_ticks():
						cd.ativo = True
						lanca_nova = Lanca(self.ambiente,lanca.dano,barra.energia,0,lanca.rect.x,lanca.rect.y,barra.energia,lanca.angulo)
						barra.zerar_energia()
						lanca_nova.angulo = lanca.angulo
						group_lancas.add(lanca_nova)
						todos_objetos.add(group_lancas)
						lanca.cd = self.ambiente.time.get_ticks()
						
						
						
					else:
						barra.zerar_energia()
					
		if cd.ativo:
			if cd.intervalo + 26 < self.ambiente.time.get_ticks():
				cd.animar()
				cd.intervalo = self.ambiente.time.get_ticks()
					
						
					

	
	def espaco(self,barra):
		
		if barra.energia < 24:

			barra.aumentar_energia(0.8)
		
		else:
			barra.zerar_energia()

		barra.animar()
	
	def key_up(self,lanca):

		if lanca.angulo <= 87:
			lanca.angulo += 3
			lanca.animar(lanca.angulo+270)
			#print(lanca.angulo)

	def key_down(self,lanca):
		
		if lanca.angulo > 0: 
			lanca.angulo -= 3
			lanca.animar(lanca.angulo+270)
			#print(lanca.angulo)





