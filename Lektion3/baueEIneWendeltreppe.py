from mcpi.minecraft import Minecraft
mc = Minecraft.create()

hoehe = 10
for schritte in range(0, hoehe):
    mc.setBlock(0 + schritte, 0 + schritte, 0, 12)