# Здесь расположены все классы и основной цикл игры.

from Sprites import *
from sounds import *
import sys
from time import sleep
import random

# Необходимые импорты, в том числе из других частей программы.

background_rect = background.get_rect()
arrow_sprite = pygame.sprite.Group()


# Единственная группа спрайтов, расположенная над классами.


class Player(pygame.sprite.Sprite):

    # Самый главный класс - класс Игрок.

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.health = 7  # Здоровье игрока.
        self.walkframe = 0  # Кадр анимации ходьбы.
        self.attackframe = 0  # Кадр анимации атаки.
        self.damage = 1  # Урон, который игрок получает от мобов.
        self.speedx = 0  # Скорость перемещения по оси x.
        self.speedy = 0  # Скорость перемещения по оси y.
        self.right = True  # Направление.
        self.image = idleright[0]  # Изначально игрок появляется с таким спрайтом.
        self.image.set_colorkey(WHITE)  # Удаление белого фона спрайта.
        self.rect = self.image.get_rect()
        self.rect.center = (wid / 2, hei / 2)  # Расположение игрока по центру экрана.

    def update(self):
        self.speedx = 0
        self.speedy = 0  # Обе скорости обнуляются.
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_d]:  # Первые 4 if отвечает за передвижение.
            if keystate[pygame.K_f]:  # Если одновременно зажаты кнопка ходьбы и кнопка атаки, то атака не выполняется.
                pass
            else:
                self.attackframe = 0
                self.right = True
                self.speedx = 8
                self.image = walkright[round(self.walkframe)]
                self.image.set_colorkey(WHITE)
                self.walkframe += 0.45
                if round(self.walkframe) == 12:
                    self.walkframe = 0
                skeleton_sound.play()  # Покадровое переключение анимации и проигрывание звука ходьбы без его включения в канал.
        if keystate[pygame.K_a]:
            if keystate[pygame.K_f]:
                pass
            else:
                self.attackframe = 0
                self.right = False
                self.speedx = -8
                self.image = walkleft[round(self.walkframe)]
                self.image.set_colorkey(WHITE)
                self.walkframe += 0.45
                if round(self.walkframe) == 12:
                    self.walkframe = 0
                skeleton_sound.play()
        if keystate[pygame.K_w]:
            if keystate[pygame.K_f]:
                pass
            else:
                self.attackframe = 0
                self.speedy = -8
                if self.right:
                    self.image = walkright[round(self.walkframe)]
                else:
                    self.image = walkleft[round(self.walkframe)]
                self.image.set_colorkey(WHITE)
                self.walkframe += 0.45
                if round(self.walkframe) == 12:
                    self.walkframe = 0
                skeleton_sound.play()
        if keystate[pygame.K_s]:
            if keystate[pygame.K_f]:
                pass
            else:
                self.attackframe = 0
                self.speedy = 8
                if self.right:
                    self.image = walkright[round(self.walkframe)]
                else:
                    self.image = walkleft[round(self.walkframe)]
                self.image.set_colorkey(WHITE)
                self.walkframe += 0.45
                if round(self.walkframe) == 12:
                    self.walkframe = 0
                skeleton_sound.play()
        if keystate[pygame.K_f]:  # Кнопка атаки
            self.speedy = 0
            self.speedx = 0
            if self.right:
                self.image = attackright[round(self.attackframe)]
            else:
                self.image = attackleft[round(self.attackframe)]
            self.image.set_colorkey(WHITE)
            if round(self.attackframe) == 4 or round(self.attackframe) == 8:
                channel0.play(attack_sound)
            self.attackframe += 0.25
            if round(self.attackframe) == 12:
                self.attackframe = 0
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > wid:
            self.rect.right = wid
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > hei:
            self.rect.bottom = hei

    def idle(self, frame):  # Функция, которая отвечает за проигрывание стандартной анимации.
        # Кадр берется извне.
        if self.right:
            self.image = idleright[frame]
        else:
            self.image = idleleft[frame]
        self.image.set_colorkey(WHITE)

    def check_attack(self):
        if self.attackframe == 4 or self.attackframe == 8:
            return True
        # Проверка атаки. Если игрок находится в такой стадии анимации атаки, которая является взмахом оружия, то возвращается True.

    def take_hit(self):
        self.speedx = 0
        self.speedy = 0
        self.health -= self.damage
        if self.right:
            self.image = hitright
        else:
            self.image = hitleft
        self.image.set_colorkey(WHITE)
        if self.health <= 0:
            return True
        # Получение удара. Если удар смертельный, возвращается True.


class Flying_eye(pygame.sprite.Sprite):  # Один из трех классов врагов. Первые 2 класса отличаются только внешним видом,
    # а также частотой атаки и скоростью

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.right = True
        self.attacktry = False
        self.speed = 0
        self.attackframe = 0
        self.deathframe = 0
        self.maxexistframe = 7
        self.ifattack = 0
        self.health = 2
        self.canshoot = False  # Переменная, связанная с тем, что последний враг является лучником.
        self.image = flyingeyeidleright[0]
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(10, 470), random.randint(10, 310))  # Большинство переменных повторяется у
        # других классов.

    def exist(self, existframe, playerx, playery):
        if self.health > 0:
            if not self.attacktry:
                self.speed = 4
            else:
                self.speed = 0
            if self.right:
                self.image = flyingeyeidleright[existframe]
            else:
                self.image = flyingeyeidleleft[existframe]
            self.image.set_colorkey(WHITE)
            if self.rect.x < playerx:
                self.rect.x += self.speed
                self.right = True
            elif self.rect.x > playerx:
                self.rect.x -= self.speed
                self.right = False
            if self.rect.y < playery:
                self.rect.y += self.speed
            elif self.rect.y > playery:
                self.rect.y -= self.speed
            if self.rect.right > wid:
                self.rect.right = wid
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.top < 0:
                self.rect.top = 0
            if self.rect.bottom > hei:
                self.rect.bottom = 0
            if round(existframe) == 2:
                channel1.play(fly_sound)  # Функция преследования игрока со звуком взмаха крыльев.

    def attack(self, player_group):
        if self.health > 0:
            if not self.attacktry:
                self.ifattack += 1
            else:
                self.speed = 0
                self.attackframe += 0.25
                if self.right:
                    self.image = flyingeyeattackright[round(self.attackframe)]
                    self.image.set_colorkey(WHITE)
                else:
                    self.image = flyingeyeattackleft[round(self.attackframe)]
                    self.image.set_colorkey(WHITE)
                if round(self.attackframe) == 7:
                    self.attackframe = 0
                    self.attacktry = False
                    channel2.play(bite_sound)
                    if pygame.sprite.spritecollide(enemy, player_group, False):
                        return True
            if self.ifattack == 23:  # Каждые 23 кадра врагу разрешается атаковать.
                self.attacktry = True
                self.ifattack = 0

    def take_hit(self):
        self.health -= 1  # Простейшая функция для отнятия здоровья.

    def die(self):  # Функция смерти.
        self.speed = 0
        self.health = False
        self.deathframe += 0.2
        if round(self.deathframe) == 0:
            channel3.play(flying_eye_death_sound)
        if round(self.deathframe) == 3:
            self.deathframe = 3
        else:
            if self.right:
                self.image = flyingeyedeathright[round(self.deathframe)]
                self.image.set_colorkey(WHITE)
            else:
                self.image = flyingeyedeathleft[round(self.deathframe)]
                self.image.set_colorkey(WHITE)


class Mushroom(pygame.sprite.Sprite):  # Абсолютно то же самое, но с другими значениями. Объяснять нет смысла.

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.right = True
        self.attacktry = False
        self.speed = 0
        self.attackframe = 0
        self.deathframe = 0
        self.ifattack = 0
        self.maxexistframe = 7
        self.health = 5
        self.canshoot = False
        self.image = mushroomidleright[0]
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(10, 470), random.randint(10, 310))

    def exist(self, existframe, playerx, playery):
        if self.health > 0:
            if not self.attacktry:
                self.speed = 1
            else:
                self.speed = 0
            if self.right:
                self.image = mushroomidleright[existframe]
            else:
                self.image = mushroomidleleft[existframe]
            self.image.set_colorkey(WHITE)
            if self.rect.x < playerx:
                self.rect.x += self.speed
                self.right = True
            elif self.rect.x > playerx:
                self.rect.x -= self.speed
                self.right = False
            if self.rect.y < playery:
                self.rect.y += self.speed
            elif self.rect.y > playery:
                self.rect.y -= self.speed
            if self.rect.right > wid:
                self.rect.right = wid
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.top < 0:
                self.rect.top = 0
            if self.rect.bottom > hei:
                self.rect.bottom = 0

    def attack(self, player_group):
        if self.health > 0:
            if not self.attacktry:
                self.ifattack += 1
            else:
                self.speed = 0
                self.attackframe += 0.25
                if self.right:
                    self.image = mushroomattackright[round(self.attackframe)]
                    self.image.set_colorkey(WHITE)
                else:
                    self.image = mushroomattackleft[round(self.attackframe)]
                    self.image.set_colorkey(WHITE)
                if round(self.attackframe) == 7:
                    channel2.play(mushroom_attack_sound)
                    self.attackframe = 0
                    self.attacktry = False
                    if pygame.sprite.spritecollide(enemy, player_group, False):
                        return True
            if self.ifattack == 60:
                self.attacktry = True
                self.ifattack = 0

    def take_hit(self):
        self.health -= 1

    def die(self):
        self.speed = 0
        self.health = False
        self.deathframe += 0.2
        if round(self.deathframe) == 0:
            channel3.play(mushroom_death_sound)
        if round(self.deathframe) == 3:
            self.deathframe = 3
        else:
            if self.right:
                self.image = mushroomdeathright[round(self.deathframe)]
                self.image.set_colorkey(WHITE)
            else:
                self.image = mushroomdeathleft[round(self.deathframe)]
                self.image.set_colorkey(WHITE)


class Arrow(pygame.sprite.Sprite):  # Стрела для третьего врага.

    def __init__(self, x, y, arrow_dir):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.rotate(arrow, (arrow_dir + 1) * -90)
        # Спрайт вращается в зависимости от направления.
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.hittarget = False
        if arrow_dir == 1:
            self.speedx = -20
            self.speedy = 0
        elif arrow_dir == 2:
            self.speedx = 0
            self.speedy = -20
        elif arrow_dir == 3:
            self.speedx = 20
            self.speedy = 0
        elif arrow_dir == 4:
            self.speedx = 0
            self.speedy = 20
        # А также двигается в сторону, указаную тем же направлением.

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy


class Summoned_Archer(pygame.sprite.Sprite):  # Самый интересный враг. Стоит на месте и призывает стрелы.

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.right = True
        self.attacktry = False
        self.speed = 0
        self.attackframe = 0
        self.deathframe = 0
        self.ifattack = 0
        self.maxexistframe = 3
        self.health = 3
        self.canshoot = True  # Тот самый показатель.
        self.arrow_dir = 1
        self.image = archeridleright[0]
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, 440), random.randint(40, 280))

    def exist(self, existframe, playerx, playery):  # Функция передвижения укорочена. Неиспользуемый аргумент
        # нужен в связи с тем, что у всех врагов одинаковые функции.
        if self.health > 0:
            if self.rect.centerx > playerx:
                self.right = False
            else:
                self.right = True
            if self.right:
                self.image = archeridleright[round(existframe)]
            else:
                self.image = archeridleleft[round(existframe)]
            self.image.set_colorkey(WHITE)

    def attack(self, player_group):
        if self.health > 0:
            if not self.attacktry:
                self.ifattack += 1
            else:
                self.speed = 0
                self.attackframe += 0.25
                if self.right:
                    self.image = archerattackright[round(self.attackframe)]
                    self.image.set_colorkey(WHITE)
                else:
                    self.image = archerattackleft[round(self.attackframe)]
                    self.image.set_colorkey(WHITE)
                if round(self.attackframe) == 6:
                    self.attackframe = 0
                    self.attacktry = False
                    return True
                elif round(self.attackframe) == 0:
                    channel1.play(bow_sound)
            if self.ifattack == 10:
                self.attacktry = True
                self.ifattack = 0

    def shoot(self, player_group):  # Эксклюзивная функция, которая испоьзуется в случае, когда canshoot = True.
        global archerarrow
        if self.arrow_dir == 1:
            archerarrow = Arrow(self.rect.centerx - 50, self.rect.centery, self.arrow_dir)
        elif self.arrow_dir == 2:
            archerarrow = Arrow(self.rect.centerx, self.rect.centery - 50, self.arrow_dir)
        elif self.arrow_dir == 3:
            archerarrow = Arrow(self.rect.centerx + 50, self.rect.centery, self.arrow_dir)
        elif self.arrow_dir == 4:
            archerarrow = Arrow(self.rect.centerx, self.rect.centery + 90, self.arrow_dir)
        # Если выпускать стрелы из центра спрайта, можно задеть игрока, когда это не требуется.
        # Поэтому стрелы появляются слегка поодаль.
        arrow_sprite.add(archerarrow)
        archerarrow.update()
        channel2.play(arrow_sound)
        self.arrow_dir += 1
        if self.arrow_dir == 5:
            self.arrow_dir = 1

    def take_hit(self):
        self.health -= 1

    def die(self):
        self.speed = 0
        self.health = False
        self.deathframe += 0.4
        if round(self.deathframe) == 7:
            self.deathframe = 3
        else:
            if self.right:
                self.image = archerdeathright[round(self.deathframe)]
                self.image.set_colorkey(WHITE)
            else:
                self.image = archerdeathleft[round(self.deathframe)]
                self.image.set_colorkey(WHITE)


class Menu:  # Игровое меню, которое позволяет начинать игру, выходить из нее и выбират сложность.

    def __init__(self, punkts=None):
        if punkts is None:
            punkts = [160, 80, u'Punkt', GRAY, WHITE, 0]  # У каждого пункта есть 6 показателей: Расположене по 2 осям,
            # название, активный цвет, стандартный цвет, номер.
        self.punkts = punkts
        self.difficulty = 0

    def draw(self, screen, font, punkt_num):
        for i in self.punkts:
            if punkt_num == i[5]:
                screen.blit(font.render(i[2], True, i[3]), (i[0], i[1]))
            else:
                screen.blit(font.render(i[2], True, i[4]), (i[0], i[1]))
            # Стандартный цвет меняется на активный при выборе пункта.


    def show(self):
        pygame.mixer.music.load(path.join(sound_dir, 'music/menu_music.mp3'))
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(loops=-1)
        menu_running = True
        punkt = 0
        while menu_running:
            screen.fill(BLACK)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        if 0 <= punkt < 2:
                            punkt += 1
                            switch_sound.play()
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        if 2 >= punkt > 0:
                            punkt -= 1
                            switch_sound.play()
                    if event.key == pygame.K_RETURN:
                        if punkt == 0:
                            choice_sound.play()
                            sleep(0.42)
                            menu_running = False
                            pygame.mixer.music.stop()
                            pygame.mixer.music.load(path.join(sound_dir, 'music/battle_music.mp3'))
                            pygame.mixer.music.set_volume(0.5)
                            pygame.mixer.music.play(loops=-1)
                        elif punkt == 1:
                            choice_sound.play()
                            if self.difficulty == 0:
                                punkts[1][2] = u'Сложность: Нормальная'
                                # Здоровье игрока: 5
                                # Получаемый урон: 2
                                # Здоровье врагов: Увеличено на 1
                                # Здоровье игрока восполняется через каждые 5 врагов
                                punkts[1][0] = 70
                                self.difficulty = 1
                            elif self.difficulty == 1:
                                punkts[1][2] = u'Сложность: Сложная'
                                punkts[1][0] = 80
                                self.difficulty = 2
                                # Здоровье игрока: 3
                                # Получаемый урон: 2
                                # Здоровье врагов: Увеличено на 2
                                # Здоровье игрока восполняется через каждые 10 врагов
                            elif self.difficulty == 2:
                                punkts[1][2] = u'Сложность: Безумие'
                                punkts[1][0] = 80
                                self.difficulty = 3
                                # Здоровье игрока: 1
                                # Получаемый урон: 1
                                # Здоровье врагов: 10
                                # Здоровье игрока не восполняется
                            elif self.difficulty == 3:
                                punkts[1][2] = u'Сложность: Лёгкая'
                                punkts[1][0] = 90
                                self.difficulty = 0
                                # Здоровье игрока: 7
                                # Получаемый урон: 1
                                # Здоровье врагов: стандартное
                                # Здоровье игрока восполняется через каждые 3 врага
                        elif punkt == 2:
                            choice_sound.play()
                            sleep(0.42)
                            sys.exit()
            screen.blit(menu_background, background_rect)
            self.draw(screen, font, punkt)
            pygame.display.flip()


enemy_sprite = pygame.sprite.Group()
player_sprite = pygame.sprite.Group()
player = Player()
enemy = random.choice((Flying_eye(), Mushroom(), Summoned_Archer()))  # Враг выбирается случайно.
enemy_sprite.add(enemy)
player_sprite.add(player)
healthregen = 0

punkts = [[135, 130, u'Начать игру', GRAY, WHITE, 0],  # Пункты меню.
          [95, 180, u'Сложность: Лёгкая', GRAY, WHITE, 1],
          [185, 230, u'Выйти', GRAY, WHITE, 2]]

menu = Menu(punkts)

menu.show()
if menu.difficulty == 0:  # Настройки врагов согласно сложности.
    player.health = 7
    healthregen = 3
    player.damage = 1
elif menu.difficulty == 1:
    player.health = 5
    enemy.health += 1
    healthregen = 5
    player.damage = 2
elif menu.difficulty == 2:
    player.health = 3
    enemy.health += 2
    healthregen = 10
    player.damage = 2
elif menu.difficulty == 3:
    player.health = 1
    enemy.health = 10
    healthregen = 0

running = True
idleframe = 0
score = 0
existframe = 0
deathanim = False

while running:  # Главный цикл.
    clock.tick(fps)
    player.idle(round(idleframe))
    healthcheck = 'Здоровье: ' + str(player.health)  # 3 индикатора: здоровье игрока, счет, здоровье врага.
    healthindicator = font.render(healthcheck, False, WHITE)
    scorecheck = 'Счёт: ' + str(score)
    if enemy.health:
        enemyhealth = 'Hp: ' + str(enemy.health)
    else:
        enemyhealth = 'Dead'
    enemyhealthindicator = hpfont.render(enemyhealth, False, WHITE)
    scoreindicator = font.render(scorecheck, False, WHITE)
    if player.check_attack():  # Проверка удара игрока по врагу.
        if pygame.sprite.spritecollide(player, enemy_sprite, False):
            enemy.take_hit()
            if enemy.health <= 0:
                deathanim = True
    if enemy.deathframe == 3:  # Анимация смерти врага с последующим появлением нового и его настройкой.
        deathanim = False
        enemy_sprite.remove(enemy)
        existframe = 0
        enemy = random.choice((Flying_eye(), Mushroom(), Summoned_Archer()))
        enemy_sprite.add(enemy)
        score += 1
        if menu.difficulty == 1:
            enemy.health += 1
        elif menu.difficulty == 2:
            enemy.health += 2
        elif menu.difficulty == 3:
            enemy.health = 10
        try:
            if score % healthregen == 0:
                player.health += 1
        except ZeroDivisionError:
            pass
    idleframe += 0.25
    if round(idleframe) == 4:
        idleframe = 0
    enemy.exist(round(existframe), player.rect.x, player.rect.y)
    existframe += 0.3
    if round(existframe) >= enemy.maxexistframe:
        existframe = 0
    if enemy.attack(player_sprite):  # Атака врага по игроку.
        if not enemy.canshoot:  # Если враг не умеет стрелять, то он наносит урон при столкновении.
            if player.take_hit():
                menu.show()
                enemy_sprite.remove(enemy)
                enemy = random.choice((Flying_eye(), Mushroom(), Summoned_Archer()))
                existframe = 0
                enemy_sprite.add(enemy)
                if menu.difficulty == 0:
                    player.health = 7
                    healthregen = 3
                    player.damage = 1
                elif menu.difficulty == 1:
                    player.health = 5
                    enemy.health += 1
                    healthregen = 5
                    player.damage = 2
                elif menu.difficulty == 2:
                    player.health = 3
                    enemy.health += 2
                    healthregen = 10
                    player.damage = 2
                elif menu.difficulty == 3:
                    player.health = 1
                    enemy.health = 10
                    healthregen = 0
                score = 0
        else:  # А если умеет, то стреляет.
            enemy.shoot(player_sprite)
    if deathanim:
        enemy.die()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                menu.show()
                enemy_sprite.remove(enemy)
                enemy = random.choice((Flying_eye(), Mushroom(), Summoned_Archer()))
                existframe = 0
                enemy_sprite.add(enemy)
                if menu.difficulty == 0:
                    player.health = 7
                    healthregen = 3
                    player.damage = 1
                elif menu.difficulty == 1:
                    player.health = 5
                    enemy.health += 1
                    healthregen = 5
                    player.damage = 2
                elif menu.difficulty == 2:
                    player.health = 3
                    enemy.health += 2
                    healthregen = 10
                    player.damage = 2
                elif menu.difficulty == 3:
                    player.health = 1
                    enemy.health = 10
                    healthregen = 0
                score = 0

    enemy_sprite.update()
    arrow_sprite.update()
    if pygame.sprite.groupcollide(arrow_sprite, player_sprite, True, False):  # Проверка столкновения стрелы с игроком.
        if player.take_hit():
            menu.show()
            enemy_sprite.remove(enemy)
            enemy = random.choice((Flying_eye(), Mushroom(), Summoned_Archer()))
            existframe = 0
            enemy_sprite.add(enemy)
            if menu.difficulty == 0:
                player.health = 7
                healthregen = 3
                player.damage = 1
            elif menu.difficulty == 1:
                player.health = 5
                enemy.health += 1
                healthregen = 5
                player.damage = 2
            elif menu.difficulty == 2:
                player.health = 3
                enemy.health += 2
                healthregen = 10
                player.damage = 2
            elif menu.difficulty == 3:
                player.health = 1
                enemy.health = 10
                healthregen = 0
            score = 0
    player_sprite.update()
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    screen.blit(healthindicator, (10, 10))
    screen.blit(scoreindicator, (300, 10))
    screen.blit(enemyhealthindicator, (enemy.rect.left, enemy.rect.top - 10))
    arrow_sprite.draw(screen)
    enemy_sprite.draw(screen)
    player_sprite.draw(screen)
    pygame.display.flip()
    # Прорисовка всех объектов.
