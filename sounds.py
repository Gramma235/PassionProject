#  Здесь находятся все звуки.

import pygame
from os import path

wid = 480
hei = 320
fps = 30

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((wid, hei))
pygame.display.set_caption("Bone Knight")
clock = pygame.time.Clock()

sound_dir = path.join(path.dirname(__file__), 'sounds')
volume = 0.5
audio = []

channel0 = pygame.mixer.Channel(0)
channel1 = pygame.mixer.Channel(1)
channel2 = pygame.mixer.Channel(2)
channel3 = pygame.mixer.Channel(3)
channel4 = pygame.mixer.Channel(4)
channel5 = pygame.mixer.Channel(5)
channel6 = pygame.mixer.Channel(6)
channel7 = pygame.mixer.Channel(7)

skeleton_sound = pygame.mixer.Sound(path.join(sound_dir, 'sounds/Skeleton/walk.mp3'))
audio.append(skeleton_sound)
attack_sound = pygame.mixer.Sound(path.join(sound_dir, 'sounds/Skeleton/attack.mp3'))
audio.append(attack_sound)
fly_sound = pygame.mixer.Sound(path.join(sound_dir, 'sounds/Flying_eye/fly.mp3'))
audio.append(fly_sound)
bite_sound = pygame.mixer.Sound(path.join(sound_dir, 'sounds/Flying_eye/attack.mp3'))
audio.append(bite_sound)
flying_eye_death_sound = pygame.mixer.Sound(path.join(sound_dir, 'sounds/Flying_eye/death.mp3'))
audio.append(flying_eye_death_sound)
mushroom_attack_sound = pygame.mixer.Sound(path.join(sound_dir, 'sounds/Mushroom/mushroom_attack.mp3'))
audio.append(mushroom_attack_sound)
mushroom_death_sound = pygame.mixer.Sound(path.join(sound_dir, 'sounds/Mushroom/mushroom_death.mp3'))
audio.append(mushroom_death_sound)
bow_sound = pygame.mixer.Sound(path.join(sound_dir, 'sounds/Summoned_Archer/bow.mp3'))
audio.append(bow_sound)
arrow_sound = pygame.mixer.Sound(path.join(sound_dir, 'sounds/Summoned_archer/arrow.mp3'))
audio.append(arrow_sound)
switch_sound = pygame.mixer.Sound(path.join(sound_dir, 'sounds/switch.mp3'))
audio.append(switch_sound)
choice_sound = pygame.mixer.Sound(path.join(sound_dir, 'sounds/choice.mp3'))
audio.append(choice_sound)

for i in audio:
    i.set_volume(volume)
