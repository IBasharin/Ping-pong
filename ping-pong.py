from pygame import *

WIDTH, HEIGHT = 600, 480
COLOR = (0, 250, 0)
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, _image, x=0, y=0, width=50, height=50):
        super().__init__()
        self.image = transform.scale(image.load(_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

#class Player(GameSprite):
    #def update(self):
        #keys = key.get_pressed()
        #if keys[K_w] and self.rect.y < 5:
           # self.rect.y -= self.speed
        #if keys[K_s] and self.rect.y > 595:
            #self.rect.y -= self.speed

class Player(GameSprite):
    def __init__(self, _image, x=0, y=0, width=50, height=50, speed =5, Key_up=K_w, Key_down=K_s):
        super().__init__(_image, x, y, width, height)
        self.speed = speed
        self.Key_up = Key_up
        self.Key_down = Key_down
    def update(self):
        keys = key.get_pressed()
        if keys[self.Key_up]:
            self.rect.y -= self.speed
        if keys[self.Key_down]:
            self.rect.y += self.speed


mw = display.set_mode ((WIDTH, HEIGHT))
mw.fill(COLOR)
display.set_caption('Пинг понг')
clock = time.Clock()

player_1 = Player('Plat.png', 10, 200, 30, 90, 4)
player_2 = Player('Plat.png', 520, 200, 30, 90, 4, Key_up=K_k, Key_down=K_j)
Ball = Player('Plat.png', 200, 200, 50, 50, 4)

speed_y = 3
speed_x = 3


Run = True
while Run:


    for e in event.get():
        if e.type == QUIT:
            Run = False
        
    mw.fill(COLOR)
    player_1.update()
    player_2.update()
    Ball.rect.x += speed_x
    Ball.rect.y += speed_y 

    if sprite.collide_rect(player_1,Ball) or sprite.collide_rect(player_2, Ball):
        speed_x *= -1
        speed_y *= 1

    if Ball.rect.y > 440 or Ball.rect.y < 0:
        speed_y *= -1

    if Ball.rect.x < 0:
        finish = True
        #smw.blit(lose1, (200, 200))
        game_over = True
    player_1.reset()
    player_2.reset()
    Ball.reset()

    display.update()
    clock.tick(FPS)
