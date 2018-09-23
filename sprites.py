import pygame
from indio import Indio
from tiro import Tiro
from lanca import Lanca
from colono_atirador import Colono_atirador
from colono_espada import Colono_espada
from cabana import Cabana


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

	def add_object_aliados(group,objecto):
		
		group.add(objecto)
		self.aliados.add(objecto)

	def add_object_eixo(self,group,objecto):
		
		group.add(objecto)
		self.eixo.add(objecto)

	def interacoes(self,ambiente):
		
		self.interacoes_tiros(ambiente)
		self.interacoes_colonos_atirador(ambiente)
		self.interacoes_colonos_espada(ambiente)
		self.interacoes_lancas(ambiente)
		self.interacoes_corvo(ambiente)

	def interacoes_corvo(self,ambiente):

		for corvo in self.corvo:

			if corvo.rect.x < 0:
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
					
					if indio.vida <= 0:
						indio.kill()

					tiro.kill()

			if colisao_barreiras:
				for barreira in colisao_barreiras:
					barreira.perder_vida(tiro.dano)
					
					if barreira.vida <= 0:
						barreira.kill()
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
						#colono.animar_morte()
						colono.kill()
					
					lanca.kill()

			if colisao_corvo:
				for corvo in colisao_corvo:
					corvo.kill()
		
			#if lanca.rect.y < ambiente.screen.get_height:
			#	lanca.kill()
			
			else:
				lanca.movimentar()
			if lanca.rect.y > 600:
				lanca.kill()			

	def interacoes_colonos_atirador(self,ambiente):

		for colono in self.colonos_atirador:
			#colisao_colonos_atirador = ambiente.sprite.spritecollide(colono,self.cabanas,False,ambiente.sprite.collide_mask)
			
			if colono.clock_atirar + colono.intervalo_ataque < self.ambiente.time.get_ticks():
				colono.animacao_atirando()
				self.tiros.add(Tiro(self.ambiente,1,-4.5,(colono.rect.x-colono.image.get_width()/4),(colono.rect.y+colono.image.get_height()/5.3)))
				self.todos_objetos.add(self.tiros)
				colono.clock_atirar = self.ambiente.time.get_ticks()

			if colono.rect.x < 0:
				print('Perdeu')
				return exit()
				
			

			#elif len(self.barreiras) != 0:
			if self.barreiras:
				for barreira in self.barreiras: 
					if colono.rect.x - barreira.rect.x < 200 and \
						colono.rect.y > barreira.rect.y and colono.rect.y < (barreira.rect.y + barreira.image.get_size()[1]):
						colono.vel_x = 0
						colono.atacar_barreira = True

					
					else:
						colono.vel_x = -2
						colono.atacar_barreira = False
						#colono.movimentar()
						print('blalalalal')
			
			if not self.barreiras:
				colono.vel_x = -2
				colono.atacar_barreira = False
				print('blalalalal')

			
			colono.movimentar()
			if not colono.atacar_barreira:
				colono.animar()

				

	def interacoes_colonos_espada(self,ambiente):

		for colono in self.colonos_espada:
			colisao_colonos_espada = ambiente.sprite.spritecollide(colono,self.barreiras,False,ambiente.sprite.collide_mask)
			
			if colisao_colonos_espada:
				for cabana in colisao_colonos_espada:
					colono.colisao = True
					colono.vel_x = 0
					if colono.clock_tempo_de_golpear + 250 < self.ambiente.time.get_ticks():
						colono.animacao_golpeando()
						colono.clock_tempo_de_golpear = self.ambiente.time.get_ticks()

					if colono.clock_golpear + colono.intervalo_ataque < self.ambiente.time.get_ticks():
						colono.clock_golpear = self.ambiente.time.get_ticks()
						#colono.animacao_golpeando()
						cabana.perder_vida(colono.dano)
						
					if cabana.vida <= 0:
						cabana.kill()
						colono.vel_x = -2
						colono.colisao = False
			
			if colono.rect.x < 0:
				colono.kill()
			
			else:
				colono.movimentar()
				if not colono.colisao:
					colono.animar()
				#colono.image = self.ambiente.transform.rotate(colono.image,45)















		
		