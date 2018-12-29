import pygame
from indio import Indio
from tiro import Tiro
from lanca import Lanca
from colono_atirador import Colono_atirador
from colono_espada import Colono_espada
from cabana import Cabana
from barreira import Barreira


class Sprites:

	def __init__(self,ambiente):
		
		self.ambiente = ambiente
		self.colonos_atirador = self.ambiente.sprite.Group()
		self.colonos_espada = self.ambiente.sprite.Group()
		self.cabanas = self.ambiente.sprite.Group()
		self.indio = self.ambiente.sprite.Group()
		self.lancas = self.ambiente.sprite.Group()
		self.corvo = self.ambiente.sprite.Group()
		self.tiros = self.ambiente.sprite.Group()
		self.aliados = self.ambiente.sprite.Group()
		self.eixo = self.ambiente.sprite.Group()
		self.barreiras = self.ambiente.sprite.Group()
		self.todos_objetos = self.ambiente.sprite.Group()
		self.todos_objetos.add(self.tiros)
		self.num_barreiras = 2
		self.score = 0

	def add_object_aliados(group,objecto):
		
		group.add(objecto)
		self.aliados.add(objecto)

	def add_object_eixo(self,group,objecto):
		
		group.add(objecto)
		self.eixo.add(objecto)

	def interacoes(self,ambiente):
		
		self.interacoes_tiros(ambiente)
		if self.interacoes_colonos_atirador(ambiente) == 'Perdeu' or self.interacoes_colonos_espada(ambiente) == 'Perdeu':
			return 'Perdeu'
		self.interacoes_lancas(ambiente)
		self.interacoes_corvo(ambiente)

	def interacoes_corvo(self,ambiente):
		for corvo in self.corvo:

			if corvo.rect.x <= 0:
				corvo.kill()
				
				
			else:
				corvo.movimentar()
				corvo.animar()	


	def interacoes_tiros(self,ambiente):

		for tiro in self.tiros:	

			colisao_indio = ambiente.sprite.spritecollide(tiro,self.indio,False,ambiente.sprite.collide_mask)
			colisao_barreiras = ambiente.sprite.spritecollide(tiro,self.barreiras,False,ambiente.sprite.collide_mask)

			if colisao_indio:
				for indio in colisao_indio:
					indio.perder_vida(tiro.dano)


			if colisao_barreiras:
				for barreira in colisao_barreiras:
					barreira.perder_vida(tiro.dano)
					
					if barreira.vida <= 0:
						for colono in self.eixo:
							if colono.lane == barreira.lane:
								colono.atacar_barreira = False
								colono.vel_x = -0.1 
						barreira.kill()
						self.num_barreiras -= 1

					tiro.kill()

			if tiro.rect.x < 0:
				tiro.kill()

			else:
				tiro.movimentar()

	def interacoes_lancas(self,ambiente):

		for lanca in self.lancas:
			colisao_eixo = ambiente.sprite.spritecollide(lanca,self.eixo,False,ambiente.sprite.collide_mask)
			colisao_corvo = ambiente.sprite.spritecollide(lanca,self.corvo,False,ambiente.sprite.collide_mask)
			if colisao_eixo:
				for colono in colisao_eixo:
					colono.perder_vida(lanca.dano)
					
					if colono.vida <= 0:
						colono.kill()
						self.score += 5
					lanca.kill()

			if colisao_corvo:
				for corvo in colisao_corvo:
					corvo.kill()
					self.score += 10
					if self.num_barreiras < 2:
						for barreira in self.barreiras:
							print(barreira)
							if barreira.rect.y == 300:
								print('zzzzzzzzzzzzzzzzzzz')
								self.barreiras.add(Barreira(ambiente,2,400,500,'bot'))

							elif barreira.rect.y == 500:
								print('xxxxxxxxxxxxxxxxxxxxxxx')
								self.barreiras.add(Barreira(ambiente,3,400,300,'top'))
						else:
							self.barreiras.add(Barreira(ambiente,3,400,300,'top'))
							
						self.todos_objetos.add(self.barreiras)
						self.num_barreiras += 1

			else:
				lanca.movimentar()
			if lanca.rect.y > 600:
				lanca.kill()			

	def interacoes_colonos_atirador(self,ambiente):

		for colono in self.colonos_atirador:
			#colisao_colonos_atirador = ambiente.sprite.spritecollide(colono,self.cabanas,False,ambiente.sprite.collide_mask)
			if colono.rect.x < 820:
				if colono.clock_atirar + colono.intervalo_ataque < self.ambiente.time.get_ticks():
					colono.animacao_atirando()
					self.tiros.add(Tiro(self.ambiente,1,-4.5,(colono.rect.x-colono.image.get_width()/4),(colono.rect.y+colono.image.get_height()/5.3)))
					self.todos_objetos.add(self.tiros)
					colono.clock_atirar = self.ambiente.time.get_ticks()


			if colono.rect.x == 0:
				return 'Perdeu'
		

			
			if self.barreiras: ## Se existirem barreiras:
				for barreira in self.barreiras:
					if colono.lane == barreira.lane: ## Se ambos se encontram na mesma linha
						if colono.rect.x - barreira.rect.x < 200 and colono.rect.x - barreira.rect.x > 64:
							colono.vel_x = 0	
							colono.atacar_barreira = True

			
			colono.movimentar()

			if not colono.atacar_barreira:
				colono.animar()

				

	def interacoes_colonos_espada(self,ambiente):

		
		for colono in self.colonos_espada:
			colono.movimentar()		
			colisao_barreira = ambiente.sprite.spritecollide(colono,self.barreiras,False,ambiente.sprite.collide_mask)
			colisao_atiradores = ambiente.sprite.spritecollide(colono,self.colonos_atirador,False,ambiente.sprite.collide_mask)
			if colisao_barreira:
				colono.atacar_barreira = True
				colono.vel_x = 0
				if colono.clock_tempo_de_golpear + 250 < self.ambiente.time.get_ticks():
					colono.animacao_golpeando()
					colono.clock_tempo_de_golpear = self.ambiente.time.get_ticks()

				elif colono.clock_golpear + colono.intervalo_ataque < self.ambiente.time.get_ticks():
					colono.clock_golpear = self.ambiente.time.get_ticks()
					for barreira in colisao_barreira:
						barreira.perder_vida(colono.dano)
						if barreira.vida <= 0:
							for colono in self.eixo:
								if colono.lane == barreira.lane:
									colono.atacar_barreira = False
									colono.vel_x = -0.1 
							barreira.kill()
							self.num_barreiras -= 1
						print('Tamanho da lista', (self.barreiras))
						print('barreiras', self.barreiras)	

			#Caso um colono sobreponha o outro
			elif colisao_atiradores:
				for atirador in colisao_atiradores:
					if atirador.rect.x > colono.rect.x:
						atirador.rect.x += 0.4
					else:	
						colono.rect.x += 0.4
			
			elif colono.rect.x <= 0:
				colono.kill()


			if colono.rect.x <= 0:
				return 'Perdeu'

			else:
				if not colono.atacar_barreira:
					colono.animar()


















		
		
