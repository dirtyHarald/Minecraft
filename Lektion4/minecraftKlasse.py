from mcpi.minecraft import Minecraft
mc = Minecraft.create()

class minecraftKlasse():

	def __init__(self):
		self.Standort = mc.player.getPos()
		self.x = self.Standort.x
		self.y = self.Standort.y
		self.z = self.Standort.z
		self.baustoff = 12
		self.wasser = 8
		self.luft = 0

	def ausgeben(self):
		mc.postToChat( "X: " + str( self.x ) + " Y: " + str( self.y ) + " Z: " + str( self.z ) )