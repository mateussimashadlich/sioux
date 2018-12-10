from objeto import Objeto
from lancamento import Lancamento
import imagens

class Lanca(Objeto):


	def __init__(self,ambiente,dano,vel_x,vel_y,pos_x,pos_y,forca,angulo=90):
		Objeto.__init__(self,ambiente,pos_x,pos_y,imagens.lanca)
		self.dano = dano
		self.vel_x = vel_x
		self.vel_y = vel_y
		self.angulo = angulo
		self.original_image = self.ambiente.image.load(imagens.lanca).convert_alpha()
		self.lancamento = Lancamento(angulo,forca)
		self.lancamento.an = self.angulo
		self.lancamento.vel_0 = vel_x
		self.cd = self.ambiente.time.get_ticks()

	def perder_vel(gravidade):
		self.pos_y -= gravidade

	def movimentar(self):
		self.lancamento.calcular()
		self.rect.x = self.lancamento.xo
		self.rect.y = self.lancamento.yo
		self.animar(self.angulo+270)
		print('voy', self.lancamento.voy)
		print("angulo",self.angulo)
		
		if self.lancamento.voy < 0 and self.angulo >= 87:
			self.animar(self.angulo+90)

		elif self.lancamento.voy < 0 and self.angulo > 65 and self.angulo < 87:
			self.animar(self.angulo+850)

		elif self.lancamento.voy < 0 and self.angulo >= 30 and self.angulo <= 65:
			self.animar(self.angulo+180)

		
		


	def animar(self,angulo):
		x, y = self.rect.center
		self.image = self.ambiente.transform.rotate(self.original_image,angulo)
		self.rect = self.image.get_rect()
		self.rect.center = (x,y)
		
		