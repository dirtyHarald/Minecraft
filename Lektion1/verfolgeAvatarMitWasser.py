from mcpi.minecraft import Minecraft
mc = Minecraft.create()
Wasser = 8

while True:
	positionDesAvatars = mc.player.getPos()
	x_KoordinateDesAvatars = positionDesAvatars.x
	y_KoordinateDesAvatars = positionDesAvatars.y
	z_KoordinateDesAvatars = positionDesAvatars.z
	mc.setBlock(x_KoordinateDesAvatars, y_KoordinateDesAvatars, z_KoordinateDesAvatars, Wasser)
