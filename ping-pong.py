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
        self.key_up = Key_up
        self.Key_down = key_down
    def update():
        keys = key.get_pressed()
        if keys[self.Key_up]:
            self.rect.y -= self.speed
        if keys[self.Key_down]:
            self.rect.y += self.speed


mw = display.set_mode ((WIDTH, HEIGHT))
mw.fill(COLOR)
display.set_caption('Пинг понг')
clock = time.Clock()

player_1 = GameSprite('Plat.png', 10, 200, 30, 90)

Run = True
while Run:
    player_1.reset()

    for e in event.get():
        if e.type == QUIT:
            Run = False
    
    display.update()
    clock.tick(FPS)
