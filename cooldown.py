from objeto import Objeto
import imagens

class Cooldown(Objeto):


	def __init__(self,ambiente,pos_x,pos_y):
		Objeto.__init__(self,ambiente,pos_x,pos_y,imagens.cd_ready)
		self.cont_img = 0
		self.ativo = False
		self.intervalo = self.ambiente.time.get_ticks()
		
	def animar(self):
		if self.cont_img <= (len(imagens.cd)-1):
			self.image = self.ambiente.image.load(imagens.cd[self.cont_img])
			self.cont_img += 1
		else:
			self.image = self.ambiente.image.load(imagens.cd_ready)
			self.cont_img = 0
			self.ativo = False
			
		
	