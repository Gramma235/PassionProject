# Здесь находятся абсолютно все спрайты и шрифт.

import pygame
from os import path

wid = 480
hei = 320
fps = 30

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)

pygame.init()
screen = pygame.display.set_mode((wid, hei))
pygame.display.set_caption("Bone Knight")
clock = pygame.time.Clock()

textures_dir = path.join(path.dirname(__file__), 'textures')

idleright = [pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/idleright/Skeleton1.png')).convert(),
             pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/idleright/Skeleton2.png')).convert(),
             pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/idleright/Skeleton3.png')).convert(),
             pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/idleright/Skeleton4.png')).convert()]
idleleft = [pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/idleleft/Skeleton1.png')).convert(),
            pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/idleleft/Skeleton2.png')).convert(),
            pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/idleleft/Skeleton3.png')).convert(),
            pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/idleleft/Skeleton4.png')).convert()]
walkright = [pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/walkright/Skeleton1.png')).convert(),
             pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/walkright/Skeleton2.png')).convert(),
             pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/walkright/Skeleton3.png')).convert(),
             pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/walkright/Skeleton4.png')).convert(),
             pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/walkright/Skeleton5.png')).convert(),
             pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/walkright/Skeleton6.png')).convert(),
             pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/walkright/Skeleton7.png')).convert(),
             pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/walkright/Skeleton8.png')).convert(),
             pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/walkright/Skeleton9.png')).convert(),
             pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/walkright/Skeleton10.png')).convert(),
             pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/walkright/Skeleton11.png')).convert(),
             pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/walkright/Skeleton12.png')).convert()]
walkleft = [pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/walkleft/Skeleton1.png')).convert(),
            pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/walkleft/Skeleton2.png')).convert(),
            pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/walkleft/Skeleton3.png')).convert(),
            pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/walkleft/Skeleton4.png')).convert(),
            pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/walkleft/Skeleton5.png')).convert(),
            pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/walkleft/Skeleton6.png')).convert(),
            pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/walkleft/Skeleton7.png')).convert(),
            pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/walkleft/Skeleton8.png')).convert(),
            pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/walkleft/Skeleton9.png')).convert(),
            pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/walkleft/Skeleton10.png')).convert(),
            pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/walkleft/Skeleton11.png')).convert(),
            pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/walkleft/Skeleton12.png')).convert()]
attackright = [pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/attackright/Skeleton1.png')).convert(),
               pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/attackright/Skeleton2.png')).convert(),
               pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/attackright/Skeleton3.png')).convert(),
               pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/attackright/Skeleton4.png')).convert(),
               pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/attackright/Skeleton5.png')).convert(),
               pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/attackright/Skeleton6.png')).convert(),
               pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/attackright/Skeleton7.png')).convert(),
               pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/attackright/Skeleton8.png')).convert(),
               pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/attackright/Skeleton9.png')).convert(),
               pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/attackright/Skeleton10.png')).convert(),
               pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/attackright/Skeleton11.png')).convert(),
               pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/attackright/Skeleton12.png')).convert()]
attackleft = [pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/attackleft/Skeleton1.png')).convert(),
              pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/attackleft/Skeleton2.png')).convert(),
              pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/attackleft/Skeleton3.png')).convert(),
              pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/attackleft/Skeleton4.png')).convert(),
              pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/attackleft/Skeleton5.png')).convert(),
              pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/attackleft/Skeleton6.png')).convert(),
              pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/attackleft/Skeleton7.png')).convert(),
              pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/attackleft/Skeleton8.png')).convert(),
              pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/attackleft/Skeleton9.png')).convert(),
              pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/attackleft/Skeleton10.png')).convert(),
              pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/attackleft/Skeleton11.png')).convert(),
              pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/attackleft/Skeleton12.png')).convert()]
hitright = pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/hitright/Skeleton2.png')).convert()
hitleft = pygame.image.load(path.join(textures_dir, 'Sprites/skeleton/hitleft/Skeleton2.png')).convert()

flyingeyeidleright = [
    pygame.image.load(path.join(textures_dir, 'Sprites/Flying_eye/idleright/Flying_eye1.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Flying_eye/idleright/Flying_eye2.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Flying_eye/idleright/Flying_eye3.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Flying_eye/idleright/Flying_eye4.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Flying_eye/idleright/Flying_eye5.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Flying_eye/idleright/Flying_eye6.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Flying_eye/idleright/Flying_eye7.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Flying_eye/idleright/Flying_eye8.png')).convert(), ]
flyingeyeidleleft = [
    pygame.image.load(path.join(textures_dir, 'Sprites/Flying_eye/idleleft/Flying_eye1.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Flying_eye/idleleft/Flying_eye2.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Flying_eye/idleleft/Flying_eye3.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Flying_eye/idleleft/Flying_eye4.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Flying_eye/idleleft/Flying_eye5.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Flying_eye/idleleft/Flying_eye6.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Flying_eye/idleleft/Flying_eye7.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Flying_eye/idleleft/Flying_eye8.png')).convert()]
flyingeyeattackright = [
    pygame.image.load(path.join(textures_dir, 'Sprites/Flying_eye/attackright/Flying_eye1.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Flying_eye/attackright/Flying_eye2.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Flying_eye/attackright/Flying_eye3.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Flying_eye/attackright/Flying_eye4.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Flying_eye/attackright/Flying_eye5.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Flying_eye/attackright/Flying_eye6.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Flying_eye/attackright/Flying_eye7.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Flying_eye/attackright/Flying_eye8.png')).convert(), ]
flyingeyeattackleft = [
    pygame.image.load(path.join(textures_dir, 'Sprites/Flying_eye/attackleft/Flying_eye1.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Flying_eye/attackleft/Flying_eye2.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Flying_eye/attackleft/Flying_eye3.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Flying_eye/attackleft/Flying_eye4.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Flying_eye/attackleft/Flying_eye5.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Flying_eye/attackleft/Flying_eye6.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Flying_eye/attackleft/Flying_eye7.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Flying_eye/attackleft/Flying_eye8.png')).convert()]
flyingeyedeathright = [
    pygame.image.load(path.join(textures_dir, 'Sprites/Flying_eye/Deathright/Flying_eye1.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Flying_eye/Deathright/Flying_eye2.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Flying_eye/Deathright/Flying_eye3.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Flying_eye/Deathright/Flying_eye4.png')).convert()]
flyingeyedeathleft = [
    pygame.image.load(path.join(textures_dir, 'Sprites/Flying_eye/Deathleft/Flying_eye1.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Flying_eye/Deathleft/Flying_eye2.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Flying_eye/Deathleft/Flying_eye3.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Flying_eye/Deathleft/Flying_eye4.png')).convert()]

mushroomidleright = [pygame.image.load(path.join(textures_dir, 'Sprites/Mushroom/idleright/Mushroom1.png')).convert(),
                     pygame.image.load(path.join(textures_dir, 'Sprites/Mushroom/idleright/Mushroom2.png')).convert(),
                     pygame.image.load(path.join(textures_dir, 'Sprites/Mushroom/idleright/Mushroom3.png')).convert(),
                     pygame.image.load(path.join(textures_dir, 'Sprites/Mushroom/idleright/Mushroom4.png')).convert(),
                     pygame.image.load(path.join(textures_dir, 'Sprites/Mushroom/idleright/Mushroom5.png')).convert(),
                     pygame.image.load(path.join(textures_dir, 'Sprites/Mushroom/idleright/Mushroom6.png')).convert(),
                     pygame.image.load(path.join(textures_dir, 'Sprites/Mushroom/idleright/Mushroom7.png')).convert(),
                     pygame.image.load(path.join(textures_dir, 'Sprites/Mushroom/idleright/Mushroom8.png')).convert(), ]
mushroomidleleft = [pygame.image.load(path.join(textures_dir, 'Sprites/Mushroom/idleleft/Mushroom1.png')).convert(),
                    pygame.image.load(path.join(textures_dir, 'Sprites/Mushroom/idleleft/Mushroom2.png')).convert(),
                    pygame.image.load(path.join(textures_dir, 'Sprites/Mushroom/idleleft/Mushroom3.png')).convert(),
                    pygame.image.load(path.join(textures_dir, 'Sprites/Mushroom/idleleft/Mushroom4.png')).convert(),
                    pygame.image.load(path.join(textures_dir, 'Sprites/Mushroom/idleleft/Mushroom5.png')).convert(),
                    pygame.image.load(path.join(textures_dir, 'Sprites/Mushroom/idleleft/Mushroom6.png')).convert(),
                    pygame.image.load(path.join(textures_dir, 'Sprites/Mushroom/idleleft/Mushroom7.png')).convert(),
                    pygame.image.load(path.join(textures_dir, 'Sprites/Mushroom/idleleft/Mushroom8.png')).convert()]
mushroomattackright = [
    pygame.image.load(path.join(textures_dir, 'Sprites/Mushroom/attackright/Mushroom1.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Mushroom/attackright/Mushroom2.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Mushroom/attackright/Mushroom3.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Mushroom/attackright/Mushroom4.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Mushroom/attackright/Mushroom5.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Mushroom/attackright/Mushroom6.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Mushroom/attackright/Mushroom7.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Mushroom/attackright/Mushroom8.png')).convert(), ]
mushroomattackleft = [pygame.image.load(path.join(textures_dir, 'Sprites/Mushroom/attackleft/Mushroom1.png')).convert(),
                      pygame.image.load(path.join(textures_dir, 'Sprites/Mushroom/attackleft/Mushroom2.png')).convert(),
                      pygame.image.load(path.join(textures_dir, 'Sprites/Mushroom/attackleft/Mushroom3.png')).convert(),
                      pygame.image.load(path.join(textures_dir, 'Sprites/Mushroom/attackleft/Mushroom4.png')).convert(),
                      pygame.image.load(path.join(textures_dir, 'Sprites/Mushroom/attackleft/Mushroom5.png')).convert(),
                      pygame.image.load(path.join(textures_dir, 'Sprites/Mushroom/attackleft/Mushroom6.png')).convert(),
                      pygame.image.load(path.join(textures_dir, 'Sprites/Mushroom/attackleft/Mushroom7.png')).convert(),
                      pygame.image.load(path.join(textures_dir, 'Sprites/Mushroom/attackleft/Mushroom8.png')).convert()]
mushroomdeathright = [pygame.image.load(path.join(textures_dir, 'Sprites/Mushroom/Deathright/Mushroom1.png')).convert(),
                      pygame.image.load(path.join(textures_dir, 'Sprites/Mushroom/Deathright/Mushroom2.png')).convert(),
                      pygame.image.load(path.join(textures_dir, 'Sprites/Mushroom/Deathright/Mushroom3.png')).convert(),
                      pygame.image.load(path.join(textures_dir, 'Sprites/Mushroom/Deathright/Mushroom4.png')).convert()]
mushroomdeathleft = [pygame.image.load(path.join(textures_dir, 'Sprites/Mushroom/Deathleft/Mushroom1.png')).convert(),
                     pygame.image.load(path.join(textures_dir, 'Sprites/Mushroom/Deathleft/Mushroom2.png')).convert(),
                     pygame.image.load(path.join(textures_dir, 'Sprites/Mushroom/Deathleft/Mushroom3.png')).convert(),
                     pygame.image.load(path.join(textures_dir, 'Sprites/Mushroom/Deathleft/Mushroom4.png')).convert()]

archeridleright = [
    pygame.image.load(path.join(textures_dir, 'Sprites/Summoned_Archer/idleright/Archer1.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Summoned_Archer/idleright/Archer2.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Summoned_Archer/idleright/Archer3.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Summoned_Archer/idleright/Archer4.png')).convert()]
archeridleleft = [pygame.image.load(path.join(textures_dir, 'Sprites/Summoned_Archer/idleleft/Archer1.png')).convert(),
                  pygame.image.load(path.join(textures_dir, 'Sprites/Summoned_Archer/idleleft/Archer2.png')).convert(),
                  pygame.image.load(path.join(textures_dir, 'Sprites/Summoned_Archer/idleleft/Archer3.png')).convert(),
                  pygame.image.load(path.join(textures_dir, 'Sprites/Summoned_Archer/idleleft/Archer4.png')).convert()]
archerattackright = [
    pygame.image.load(path.join(textures_dir, 'Sprites/Summoned_Archer/attackright/Archer1.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Summoned_Archer/attackright/Archer2.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Summoned_Archer/attackright/Archer3.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Summoned_Archer/attackright/Archer4.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Summoned_Archer/attackright/Archer5.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Summoned_Archer/attackright/Archer6.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Summoned_Archer/attackright/Archer7.png')).convert()]
archerattackleft = [
    pygame.image.load(path.join(textures_dir, 'Sprites/Summoned_Archer/attackleft/Archer1.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Summoned_Archer/attackleft/Archer2.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Summoned_Archer/attackleft/Archer3.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Summoned_Archer/attackleft/Archer4.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Summoned_Archer/attackleft/Archer5.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Summoned_Archer/attackleft/Archer6.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Summoned_Archer/attackleft/Archer7.png')).convert()]
archerdeathright = [
    pygame.image.load(path.join(textures_dir, 'Sprites/Summoned_Archer/deathright/Archer1.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Summoned_Archer/deathright/Archer2.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Summoned_Archer/deathright/Archer3.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Summoned_Archer/deathright/Archer4.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Summoned_Archer/deathright/Archer5.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Summoned_Archer/deathright/Archer6.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Summoned_Archer/deathright/Archer7.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Summoned_Archer/deathright/Archer8.png')).convert()]
archerdeathleft = [
    pygame.image.load(path.join(textures_dir, 'Sprites/Summoned_Archer/deathleft/Archer1.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Summoned_Archer/deathleft/Archer2.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Summoned_Archer/deathleft/Archer3.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Summoned_Archer/deathleft/Archer4.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Summoned_Archer/deathleft/Archer5.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Summoned_Archer/deathleft/Archer6.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Summoned_Archer/deathleft/Archer7.png')).convert(),
    pygame.image.load(path.join(textures_dir, 'Sprites/Summoned_Archer/deathleft/Archer8.png')).convert()]
arrow = pygame.image.load(path.join(textures_dir, 'Sprites/Summoned_Archer/Arrow.png')).convert()

background = pygame.image.load(path.join(textures_dir, 'background.png')).convert()
menu_background = pygame.image.load(path.join(textures_dir, 'menu_background.png')).convert()
icon = pygame.image.load(path.join(textures_dir, 'icon.png')).convert()
icon.set_colorkey(WHITE)
font = pygame.font.Font(path.join(textures_dir, 'Fonts/main.ttf'), 30)
hpfont = pygame.font.Font(path.join(textures_dir, 'Fonts/main.ttf'), 15)
pygame.display.set_icon(icon)
