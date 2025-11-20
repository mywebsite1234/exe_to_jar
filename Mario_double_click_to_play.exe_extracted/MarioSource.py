# Source Generated with Decompyle++
# File: Mario_executable.pyc (Python 3.11)

from pygame import *
from random import *
import os
import sys

def resource_path(relative_path):
    ''' Get absolute path to resource, works for dev and for PyInstaller '''
    base_path = sys._MEIPASS
# WARNING: Decompyle incomplete


def text(message, x, y, font_color, font_size, font_type = (resource_path('font.otf'),)):
    font_type = font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    window.blit(text, (x, y))

init()
fireball_set = 0
mari = 0
mm = 0
move = 0
fire = 0
no_fire = 0
mixer.music.load(resource_path('mario_theme.mp3'))
mixer.music.play(-1)
mixer.music.set_volume(0.01)
ouchs = mixer.Sound(resource_path('ouchs.mp3'))
bye = mixer.Sound(resource_path('goomba-destroy.wav'))
mx = 43
my = 80
big = 0
game = 1
time_set = 0
fire_time1 = time.get_ticks()
fire_time2 = time.get_ticks()
end = mixer.Sound(resource_path('game-over.mp3'))
jump = mixer.Sound(resource_path('stomp.wav'))
sound = 0
jump_count = 30
score = 0
goomba_direction = 0
csound = mixer.Sound(resource_path('coin-sound.wav'))
power = mixer.Sound(resource_path('power-up.wav'))
win = mixer.Sound(resource_path('mario-win.mp3'))
goomba_bye = 0
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
mario_blue = (116, 147, 246)
question_cooldown = 0
width = 1000
height = 495
map = [
    'b    h      h     h                                                                                                                                                    ',
    'b                                                                                                                                                                      ',
    'b                                                                                                                                                                      ',
    'b                                                                                                                                                                      ',
    'b                                                                                                                                                                      ',
    'b                                                                                                                                                                      ',
    'b                                                                             g  g                                                                                     ',
    'b          ...u..     .?.                                                    .........                                     s                                           ',
    'b  m                                                                                                                      ss                                           ',
    'b                    .                        ..  .                                                                      sss                                           ',
    'b                   ...                      ...  ..                      .f.                                           ssss                                           ',
    'b               ...   ..                    ....  ...                                                                  sssss           c                               ',
    'b    h                                     .....  ....         ?????                                                  ssssss                                           ',
    'b  t =      ==g    p      ==g     =       ......  .....                                                   gg         sssssss       l   #                               ',
    'b-----------------------------------------------  --------------------  -------------   -------------------------------------------------------------------------------',
    'b-----------------------------------------------  --------------------  -------------   -------------------------------------------------------------------------------',
    'b-----------------------------------------------  --------------------  -------------   -------------------------------------------------------------------------------']

class Ground(sprite.Sprite):
    
    def __init__(self, x, y, id):
        sprite.Sprite.__init__(self)
        self.image = image.load(resource_path('ground.png')).convert()
        self.rect = self.image.get_rect()
        self.rect.center = [
            x,
            y]
        self.id = id

    
    def update(self):
        global move
        keys = key.get_pressed()
        if keys[K_RIGHT] and move == 1:
            pass
        if keys[K_LEFT] or move == 1:
            0 = self.rect, self.rect.x -= 10, .x
            return None
        return self.rect, self.rect.x -= 10, .x



class Castle(sprite.Sprite):
    
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load(resource_path('mario-castle.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = [
            x,
            y]

    
    def update(self):
        global move
        keys = key.get_pressed()
        if keys[K_RIGHT] and move == 1:
            pass
        if keys[K_LEFT] or move == 1:
            0 = self.rect, self.rect.x -= 10, .x
            return None
        return self.rect, self.rect.x -= 10, .x



class Stair(sprite.Sprite):
    
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load(resource_path('stair.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = [
            x,
            y]

    
    def update(self):
        global move
        keys = key.get_pressed()
        if keys[K_RIGHT] and move == 1:
            pass
        if keys[K_LEFT] or move == 1:
            0 = self.rect, self.rect.x -= 10, .x
            return None
        return self.rect, self.rect.x -= 10, .x



class Fireball(sprite.Sprite):
    
    def __init__(self, x, y, dir):
        sprite.Sprite.__init__(self)
        self.image = image.load(resource_path('fireball.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = [
            x,
            y]
        self.direction = dir
        self.fall_speed = 2
        self.on_ground = False

    
    def upload(self):
        if no_fire == 1:
            self.kill()
        print('test')

    
    def update(self):
        sprite.spritecollide(self, ground_group, False) = self, self.fall_speed += 0.5, .fall_speed
        for w in bricks:
            self.rect.bottom = w.rect.top
            self.fall_speed = 2
            self.on_ground = True
            if self.on_ground == True:
                False = self.rect, self.rect.y -= 40, .y
        if no_fire == 1:
            self.kill
            return None
        return self.rect, self.rect.x += 5, .x if self.direction == 'right' else self.rect, self.rect.x -= 5, .x



class Barrier(sprite.Sprite):
    
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load(resource_path('barrier.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = [
            x,
            y]



class Fbarrier(sprite.Sprite):
    
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load(resource_path('barrier.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = [
            x,
            y]

    
    def update(self):
        global move
        keys = key.get_pressed()
        if keys[K_RIGHT] and move == 1:
            pass
        if keys[K_LEFT] or move == 1:
            0 = self.rect, self.rect.x -= 10, .x
            return None
        return self.rect, self.rect.x -= 10, .x



class Flower(sprite.Sprite):
    
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load(resource_path('fire_flower.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = [
            x,
            y]

    
    def update(self):
        global move, fire
        keys = key.get_pressed()
        if keys[K_RIGHT] and move == 1:
            pass
        if keys[K_LEFT] and move == 1:
            0 = self.rect, self.rect.x -= 10, .x
        if sprite.spritecollide(self, mario_group, False):
            self.kill()
            fire = 1
            return None



class Goomba(sprite.Sprite):
    
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load(resource_path('goomba.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = [
            x,
            y]
        self.direction = -3
        self.speed = 5
        self.fall_speed = 2
        self.generate = randint(1, 2)

    
    def update(self):
        global move, goomba_bye, game, sound
        keys = key.get_pressed()
        if keys[K_RIGHT] and move == 1:
            pass
        if keys[K_LEFT] and move == 1:
            0 = self.rect, self.rect.x -= 10, .x
        sprite.spritecollide(self, ground_group, False) = self, self.fall_speed += 0.5, .fall_speed
        for w in bricks:
            if w.id == 0:
                self.rect.bottom = w.rect.top
                self.fall_speed = 0
            if mario.rect.collidepoint(self.rect.centerx, self.rect.top) or sprite.spritecollide(self, fireball_group, True):
                self.kill()
                mixer.Sound.play(bye)
                goomba_bye += 1
            elif mario.rect.collidepoint(self.rect.left, self.rect.centery) or mario.rect.collidepoint(self.rect.right, self.rect.centery):
                mario.image = image.load(resource_path('ouch.png')).convert_alpha()
                if sound == 0:
                    game = 0
                    sound += 1
                mario.kill()
        if abs(self.rect.x - mario.rect.x) < 600:
            if sprite.spritecollide(self, obstacle_group, False):
                pass
            return None
        return self.rect, self.rect.y += self.fall_speed, .y



class Mushroom(sprite.Sprite):
    
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load(resource_path('mushroom.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = [
            x,
            y]

    
    def update(self):
        global move
        keys = key.get_pressed()
        if keys[K_RIGHT] and move == 1:
            pass
        if keys[K_LEFT] or move == 1:
            0 = self.rect, self.rect.x -= 10, .x
            return None
        return self.rect, self.rect.x -= 10, .x



class Fquestion(sprite.Sprite):
    
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load(resource_path('question.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = [
            x,
            y]
        self.state = True
        self.id = randint(1, 2)

    
    def update(self):
        global move, flower
        keys = key.get_pressed()
        if self.state == True:
            if keys[K_RIGHT] and move == 1:
                pass
            if keys[K_LEFT] and move == 1:
                0 = self.rect, self.rect.x -= 10, .x
        if self.state == False and keys[K_RIGHT] and move == 1:
            pass
        if self.rect.colliderect(mario.rect) or self.state == True:
            Flower(self.rect.centerx, self.rect.top - 13) = self.rect, self.rect.x -= 5, .x
            flower_group.add(flower)
            self.image = image.load(resource_path('empty.png')).convert_alpha()
            self.state = False
            obstacle_group.add(self)
            return None
        return self.rect, self.rect.x -= 5, .x



class Question(sprite.Sprite):
    
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load(resource_path('question.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = [
            x,
            y]
        self.state = True
        self.id = randint(1, 2)

    
    def update(self):
        global move
        keys = key.get_pressed()
        if self.state == True:
            if keys[K_RIGHT] and move == 1:
                pass
            if keys[K_LEFT] and move == 1:
                0 = self.rect, self.rect.x -= 10, .x
        if self.state == False and keys[K_RIGHT] and move == 1:
            pass
        if self.rect.colliderect(mario.rect) or self.state == True:
            Coin(self.rect.centerx, self.rect.top - 13) = self.rect, self.rect.x -= 5, .x
            coin_group.add(coin)
            self.image = image.load(resource_path('empty.png')).convert_alpha()
            self.state = False
            obstacle_group.add(self)
            return None
        return self.rect, self.rect.x -= 5, .x



class Mquestion(sprite.Sprite):
    
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load(resource_path('question.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = [
            x,
            y]
        self.state = True
        self.id = randint(1, 2)

    
    def update(self):
        global move
        keys = key.get_pressed()
        if self.state == True:
            if keys[K_RIGHT] and move == 1:
                pass
            if keys[K_LEFT] and move == 1:
                0 = self.rect, self.rect.x -= 10, .x
        if self.state == False and keys[K_RIGHT] and move == 1:
            pass
        if self.rect.colliderect(mario.rect) or self.state == True:
            Mushroom(self.rect.centerx, self.rect.top - 13) = self.rect, self.rect.x -= 5, .x
            mushroom_group.add(mushroom)
            self.image = image.load(resource_path('empty.png')).convert_alpha()
            self.state = False
            obstacle_group.add(self)
            return None
        return self.rect, self.rect.x -= 5, .x



class Brick(sprite.Sprite):
    
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load(resource_path('mario-brick.png')).convert()
        self.rect = self.image.get_rect()
        self.rect.center = [
            x,
            y]
        self.id = 0

    
    def update(self):
        global move
        keys = key.get_pressed()
        if keys[K_RIGHT] and move == 1:
            pass
        if keys[K_LEFT] or move == 1:
            0 = self.rect, self.rect.x -= 10, .x
            return None
        return self.rect, self.rect.x -= 10, .x



class Tnt(sprite.Sprite):
    
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load(resource_path('tnt.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = [
            x,
            y]

    
    def update(self):
        global move
        keys = key.get_pressed()
        if keys[K_RIGHT] and move == 1:
            pass
        if keys[K_LEFT] or move == 1:
            0 = self.rect, self.rect.x -= 10, .x
            return None
        return self.rect, self.rect.x -= 10, .x



class Coin(sprite.Sprite):
    
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load(resource_path('coin2.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = [
            x,
            y]

    
    def update(self):
        global move, score
        keys = key.get_pressed()
        if keys[K_RIGHT] and move == 1:
            pass
        if keys[K_LEFT] and move == 1:
            0 = self.rect, self.rect.x -= 10, .x
        if sprite.spritecollide(self, mario_group, False):
            self.kill()
            mixer.Sound.play(csound)
            score += 1
            return None



class Mario(sprite.Sprite):
    
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load(resource_path('mario1.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = [
            x,
            y]
        self.direction = 'down'
        self.make_jump = False
        self.fall_speed = 2
        self.on_ground = False
        self.mx = 36
        self.my = 48

    
    def update(self):
        global no_fire, game, game, fire_time2, no_fire, time_set, fire_time1, move, move, fireball_set, big, time_set, mari, mm, mari, mm, mari, mm, fire
        keys = key.get_pressed()
        if sprite.spritecollide(self, testing_group, False):
            no_fire = 1
            fireball_group.empty()
            game = 3
        if self.rect.y >= height:
            game = 0
        fire_time2 = time.get_ticks()
        if sprite.spritecollide(self, fquestion_group, False):
            no_fire = 1
        if fire_time2 - fire_time1 >= 500:
            time_set = 1
            fire_time1 = fire_time2
        if self.rect.centerx >= width / 2:
            move = 1
        if keys[K_LEFT] and move == 1:
            move = 0
        if fire == 1:
            self.image = image.load(resource_path('fire_mario.png')).convert_alpha()
            fireball_set = fire
        if sprite.spritecollide(self, mushroom_group, True):
            1 = self, self.fall_speed += 0.5, .fall_speed
            self.mx = 36
            self.my = 60
            mixer.Sound.play(power)
        if sprite.spritecollide(self, tnt_group, False):
            self.image = image.load(resource_path('ouch.png')).convert_alpha()
            mixer.Sound.play(ouchs)
        keys = key.get_pressed()
        if fireball_set == 1 and keys[K_LCTRL] | keys[K_LSHIFT] and time_set == 1:
            fireball = Fireball(self.rect.centerx, self.rect.centery, self.direction)
            fireball_group.add(fireball)
            time_set = 0
        bricks = sprite.spritecollide(self, obstacle_group, False)
        for w in bricks:
            self.rect.bottom = w.rect.top
            self.fall_speed = 2
            self.on_ground = True
            keys = key.get_pressed()
            if fire == 0:
                mari = 0
                mm = 0
                mari = resource_path('mario1.png')
                mm = resource_path('mario1-left.png')
        if fire == 1:
            mari = resource_path('fire_mario.png')
            mm = resource_path('fire_mario-left.png')
            fire = 3
            transform.scale(self.image, (36, 60))
        if move == 0:
            if keys[K_RIGHT]:
                pass
            if keys[K_LEFT]:
                pass
        if move == 1:
            if keys[K_RIGHT] and self.direction != 'right':
                image.load(mari).convert_alpha() = self.rect, self.rect.y += self.fall_speed, .y if self.direction != 'right' else self.rect, self.rect.x += 10, .x if self.direction != 'left' else self.rect, self.rect.x -= 10, .x
                self.direction = 'right'
                self.image = transform.scale(self.image, (self.mx, self.my))
            if keys[K_LEFT] and self.direction != 'left':
                self.image = image.load(mm).convert_alpha()
                self.direction = 'left'
                self.image = transform.scale(self.image, (self.mx, self.my))
                self.rect.update(self.rect.x, self.rect.y, self.mx, self.my)
        bricks = sprite.spritecollide(self, obstacle_group, False)
        for w in bricks:
            if self.direction == 'left':
                self.rect.left = w.rect.right
            if self.direction == 'right':
                self.rect.right = w.rect.left
            if self.on_ground == True or keys[K_UP]:
                self.direction = 'up'
                mixer.Sound.play(jump)
                False = self.rect, self.rect.y -= 80, .y
                return None
            return None
            return None

    
    def jump(self):
        global jump_count, jump_count
        if jump_count >= -30:
            jump_count -= 3 = self.rect, self.rect.y -= jump_count / 2, .y
            return None
        jump_count = None
        self.make_jump = False


size_window = (width, height)
window = display.set_mode(size_window)
display.set_caption('Mario')
game_icon = image.load(resource_path('mario_icon.png')).convert_alpha()
display.set_icon(game_icon)
firework_group = sprite.Group()
stair_group = sprite.Group()
castle_group = sprite.Group()
fireball_group = sprite.Group()
fquestion_group = sprite.Group()
flower_group = sprite.Group()
testing_group = sprite.Group()
goomba_group = sprite.Group()
mushroom_group = sprite.Group()
obstacle_group = sprite.Group()
ground_group = sprite.Group()
question_group = sprite.Group()
mario_group = sprite.Group()
coin_group = sprite.Group()
tnt_group = sprite.Group()
size = 30
x = 0
y = 0
# WARNING: Decompyle incomplete
